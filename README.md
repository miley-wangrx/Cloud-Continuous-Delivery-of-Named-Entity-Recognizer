[![Python Application test with GitHub actions](https://github.com/miley-wangrx/microservice/actions/workflows/main.yml/badge.svg)](https://github.com/miley-wangrx/microservice/actions/workflows/main.yml)

# microservice
AWS DevOps workflow for creating a microservice

## Steps to run this project

* Create a GitHub Repo
* Open AWS Cloud Shell
* Create ssh-keys in AWS Cloud Shell
* Upload ssh-keys to Github
* Create scaffolding for project
  - Makefile

  Should look similar to the file below

  ```bash
  install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

  test:
	python -m pytest -vv test_hello.py

  format:
	black *.py

  lint:
	pylint --disable=R,C main.py hello.py

  all: install lint test
  ```

  - requirements.txt
  
  The requirements.txt should include:

  ```bash
  pytest==6.2.5
  pylint==2.12.2
  black==21.12b0
  fastapi==0.71.0
  uvicorn==0.16.0
  ```
  We can use the command "pip freeze" to see current version.
* Create a python virtual environment and source it if not created

  ```bash
  python3 -m venv ~/.microservice
  source ~/.microservice/bin/activate
  ```

* Create initial `hello.py` and `test_hello.py`

  hello.py
  ```python
  def cool(name):
    if name == "Miley":
        return "Cool!"
    return "Not cool at all.."

  print(cool("Miley"))

  def toyou(x):
    return f"hi {x}"

  def add(x):
    return x + 1

  def subtract(x):
    return x - 1
  ```

  test_hello.py
  ```python
  from hello import cool, toyou, add, subtract

  def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10

  def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x

  ### Run to see failed test
  #def test_hello_add():
  #    assert add(test_hello_add.x) == 12
  
  def test_cool():
    assert cool("Miley") == "Cool!"
    assert cool("Bubble") == "Not cool at all.."

  def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9

  ```

* Run `make all` which will install, lint and test code.
  - sample outcome:
  ![image](https://user-images.githubusercontent.com/88390268/150705648-9a3c9d14-09ca-47a9-9677-14b1a59d35ed.png)

* Setup Github Actions in `main.yml`

  ```yaml
  name: Python Application test with GitHub actions
  on: [push]
  jobs:
    build:
      runs-on: ubuntu-latest

      steps:
        - uses: actions/checkout@v2
        - name: Set up Python 3.8
          uses: actions/setup-python@v1
          with: 
            python-version: 3.8
        - name: Install dependencies
          run: |
            make install
        - name: Lint with Pylint
          run: |
            make lint
        - name: Test with Pytest
          run: |
            make test
        - name: Format code with Python black
          run: |
            make format
  ``` 

* Commit changes and push to Github

* Verify Github Actions Test Software
  ![image](https://user-images.githubusercontent.com/88390268/150706005-c09058bc-6b00-413a-b655-a16846ef9839.png)

* Run project in AWS Shell



