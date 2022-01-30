install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m spacy download en_core_web_sm

test:
	python -m pytest -vv test_hello.py

format:
	black *.py

lint:
	pylint --disable=R,C main.py hello.py

all: install lint test