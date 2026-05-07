.PHONY: install serve build clean modernize

VENV := .venv
PY := $(VENV)/bin/python
MKDOCS := $(VENV)/bin/mkdocs

$(PY):
	python3 -m venv $(VENV)

install: $(PY)
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements.txt

serve: install
	$(MKDOCS) serve

build: install
	$(MKDOCS) build --strict

modernize:
	python3 scripts/modernize_course.py

clean:
	rm -rf site
