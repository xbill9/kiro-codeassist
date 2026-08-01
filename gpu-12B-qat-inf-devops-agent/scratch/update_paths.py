import os

files_to_update = [
    "/home/xbill/kiro-codeassist/gpu-12B-qat-inf-devops-agent/README.md",
    "/home/xbill/kiro-codeassist/gpu-12B-qat-inf-devops-agent/GEMINI.md"
]

replacements = {
    "gemma4-tips-aws/gpu-12B-qat-inf-devops-agent": "kiro-codeassist/gpu-12B-qat-inf-devops-agent",
    "gemma4-tips/gpu-12B-qat-L4-devops-agent": "kiro-codeassist/gpu-12B-qat-inf-devops-agent"
}

for file_path in files_to_update:
    if os.path.exists(file_path):
        print(f"Updating {file_path}...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        orig_content = content
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        if content != orig_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully updated {file_path}")
        else:
            print(f"No changes made to {file_path}")
    else:
        print(f"File not found: {file_path}")
