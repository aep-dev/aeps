.PHONY: lint check install help

help:
	@echo "Available targets:"
	@echo "  make install    - Install dependencies (npm install)"
	@echo "  make lint       - Format code and run all linting checks"
	@echo "  make check      - Run all linting checks without modifying files"

install:
	npm install .

lint: install
	npm run lint
	python3 scripts/fix.py --path ./aep/general/
	python3 scripts/validate_links.py

check:
	npm run check
	python3 scripts/fix.py --check --path ./aep/general/
	python3 scripts/validate_links.py