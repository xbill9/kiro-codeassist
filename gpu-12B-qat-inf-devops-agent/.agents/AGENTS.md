# 🤖 Project-Scoped SRE Guidelines: AWS Neuron & vLLM Serving

## ⚡ 1. AWS Neuron Compiler Failure Cache Management
When running vLLM with AWS Neuron (`device=neuron`) on Inferentia (`inf2`) or Trainium (`trn1`) instances, the compiler caches both successful and **failed** compilation graphs (NEFFs). 

* **The Trap**: If a compilation fails once (e.g., due to out-of-memory, disk space exhaustion, or bad input shapes), the Neuron compiler caches that failure in `/var/tmp/neuron-compile-cache/` or inside `.cache/neuron/`. Subsequent launches will immediately fail with `subprocess.CalledProcessError: Command '' died with <Signals.SIGHUP: 1>` without even trying to compile!
* **Container Persistence**: Because the Docker container's root file system persists across standard restarts, any failure cached at `/var/tmp/neuron-compile-cache` inside the container persists and loops infinitely.

### Operational Guardrails & Remedies:
1. **Always Recreate the Container**: Do not rely on `docker restart` or `--restart always` policies alone to recover from compilation crashes. Stop and **remove** the container, then run a fresh container to clear any persistent container-internal `/var/tmp/neuron-compile-cache/` entries.
2. **Purge Cache Directories**: Before redeploying, explicitly purge the following directories on the host:
   ```bash
   sudo rm -rf /var/tmp/neuron-compile-cache
   sudo rm -rf /home/ubuntu/.cache/neuron/*
   ```
3. **Check Host Storage First**: Host storage exhaustion causes compilation failure and subsequent silent SSM and container failures. Reclaim space immediately via:
   ```bash
   docker volume prune -f
   docker system prune -af
   ```

---

## 🧩 2. Gemma 4 Hybrid Attention & KV Cache Head Dimension Matching
Gemma 4's hybrid attention architecture alternates standard sliding-window layers (`head_dim = 256`) and global attention layers (`head_dim = 512`). 

* **The Mismatch**: Because the model's KV Cache is allocated statically to the maximum `head_dim = 512` layer size for all layers, any updates or writes (e.g., during sliding window layers where `head_dim = 256`) can cause an XLA/HLO compilation crash due to shape and memory space mismatches (e.g., `bf16[4,4,4096,256]` versus `bf16[4,4,4096,512]`).
* **The Remedy (Dynamic Update Padding)**: When patching the `neuronx-distributed-inference` modules (specifically `utils.py`), we must apply explicit padding to any incoming updates before they are committed via slice operations:
  
  1. **`update_cache_const_indices`**:
     ```python
     if updates.shape[-1] < d_head:
         updates = torch.nn.functional.pad(updates, (0, d_head - updates.shape[-1]))
     ```
  
  2. **`dynamic_update_slice`**:
     ```python
     if update.shape[-1] < tensor.shape[-1]:
         update = torch.nn.functional.pad(update, (0, tensor.shape[-1] - update.shape[-1]))
     ```

* **The Remedy (Slicing on Retrieval)**: Conversely, when fetching the cached values in the managers (`kv_cache_manager.py`, `gpt_oss_kv_cache_manager.py`, etc.), we must slice the returned cache back from `512` to `256` for sliding-window layers (`(idx + 1) % 6 != 0`):
  ```python
  if (idx + 1) % 6 != 0:
      if k_cache.shape[-1] == 512:
          k_cache = k_cache[..., :256]
      if v_cache.shape[-1] == 512:
          v_cache = v_cache[..., :256]
  ```
