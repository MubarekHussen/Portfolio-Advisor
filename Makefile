PYTHON = python
PIP = pip

.PHONY: all install run

all: install run

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) portfolio_suggestion.py