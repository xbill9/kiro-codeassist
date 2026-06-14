# Makefile for mcp-stdio-python

.PHONY: help all install run build test lint format type-check status pull push clean

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

all: install test lint type-check

# Target to install dependencies
install: ## Install dependencies
	@echo "Installing dependencies..."
	@python3 -m pip install --break-system-packages -r requirements.txt
	@python3 -m pip install --break-system-packages -r requirements-dev.txt

release: ## Install dependencies in release mode
	@echo "Installing dependencies..."
	@python3 -m pip install --break-system-packages -r requirements.txt

# Target to run the application
run: ## Run the application
	@echo "Running the application..."
	@python3 main.py

# Target to build the application (placeholder for future use)
build: ## Build the application
	@echo "Building the application..."
	@echo "No build steps defined for this project, currently just runs Python code."

# Target to run tests
test: ## Run tests
	@echo "Running tests..."
	@python3 -m pytest test_logging.py test_greet.py

# Target to lint the code
lint: ## Lint the code
	@echo "Linting the code..."
	@flake8 .

# Target to format the code
format: ## Format the code
	@echo "Formatting the code..."
	@black .

# Target to type-check the code
type-check: ## Type-check the code
	@echo "Type-checking the code..."
	@mypy .

# Target to show git status
status: ## Show git status
	@echo "Showing git status..."
	@git status

# Target to pull latest changes from git
pull: ## Pull latest changes from git
	@echo "Pulling latest changes from git..."
	@git pull

# Target to push changes to git
push: ## Push changes to git
	@echo "Pushing changes to git..."
	@git push

clean: ## Clean up temporary/compiled files
	@echo "Cleaning up..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pyte*" -exec rm -rf {} +

