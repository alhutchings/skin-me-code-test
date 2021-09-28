
.PHONY: start
start: ## Run mypy to statically check for type errors
	PYTHONPATH=src FLASK_APP=app:app FLASK_ENV=development flask run --host 0.0.0.0 --port 9000

.PHONY: test
test: ## Run mypy to statically check for type errors
	PYTHONPATH=src pytest
