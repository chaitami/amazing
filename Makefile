PYTHON		= python3
MAIN		= a_maze_ing.py
CONFIG		= config.txt

# ── Install dependencies ─────────────────────────────────────────────
install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# ── Run the main script ──────────────────────────────────────────────
run:
	$(PYTHON) $(MAIN) $(CONFIG)

# ── Run in debug mode (pdb) ──────────────────────────────────────────
debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

# ── Remove temporary / cache files ───────────────────────────────────
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# ── Lint (mandatory flags) ───────────────────────────────────────────
lint:
	flake8 .
	mypy . \
		--warn-return-any \
		--warn-unused-ignores \
        --ignore-missing-imports \
        --disallow-untyped-defs \
        --check-untyped-defs

# ── Lint strict (optional, enhanced checking) ────────────────────────
lint-strict:
	flake8 .
	mypy . --strict

.PHONY: install run debug clean lint lint-strict