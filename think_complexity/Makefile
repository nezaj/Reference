MAKEFLAGS = --no-print-directory --always-make --silent
MAKE = make $(MAKEFLAGS)

# ~/.virtualenvs is a typical Python default location
VENV_PATH = ~/.virtualenvs/think-complexity
VENV_ACTIVATE = . $(VENV_PATH)/bin/activate

clean:
	find . -name "*.pyc" -print -delete
	rm -rfv $(VENV_PATH)

check:
	$(MAKE) virtualenv
	$(MAKE) pylint pep8 nosetests

virtualenv:
	test -d $(VENV_PATH) || virtualenv $(VENV_PATH)
	$(VENV_ACTIVATE) && python setup.py --quiet develop

pylint:
	@echo "Running pylint..."
	$(VENV_ACTIVATE) && \
	PYTHONPATH=src pylint src/graphs && \
	pylint src/analysis && \
	PYTHONPATH=src pylint src/tests && \
	pylint src/*.py

pep8:
	@echo "Running pep8..."
	$(VENV_ACTIVATE) && pep8 src

nosetests:
	@echo "Running tests..."
	$(VENV_ACTIVATE) && PYTHONPATH=src nosetests src/tests
