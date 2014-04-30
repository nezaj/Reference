MAKEFLAGS = --no-print-directory --always-make --silent
MAKE = make $(MAKEFLAGS)

# ~/.virtualenvs is a typical Python default location
VENV_PATH = ~/.virtualenvs/think-complexity
VENV_ACTIVATE = . $(VENV_PATH)/bin/activate

clean:
	find . -name "*.pyc" -print -delete

nosetests:
	@echo "Running tests..."
	$(VENV_ACTIVATE) && PYTHONPATH=. nosetests tests
