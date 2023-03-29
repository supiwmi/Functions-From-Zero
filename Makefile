install: 
	pip install --upgrade pip &&\
		pip install -r requirement.txt
	
test:
	python -m pytest -vv test_hello.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test