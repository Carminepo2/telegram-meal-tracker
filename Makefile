VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) main.py

dev: $(VENV)/bin/activate
	npx nodemon --exec $(PYTHON) main.py

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

freeze_deps:
	${PIP} freeze > requirements.txt

format:
	black .

lint:
	pylint main.py

clean:
	rm -rf __pycache__
	rm -rf $(VENV)