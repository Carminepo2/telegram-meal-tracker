
MAIN = ./src/main.py
VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) ${MAIN}

dev: $(VENV)/bin/activate
	npx nodemon --exec $(PYTHON) ${MAIN}

test: $(VENV)/bin/activate
	$(PYTHON) -m unittest discover -s ./tests

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

freeze_deps:
	${PIP} freeze > requirements.txt

format:
	black .

lint:
	pylint ${MAIN}

clean:
	rm -rf __pycache__
	rm -rf $(VENV)