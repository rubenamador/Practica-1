init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	coverage run sample/core.py
	coverage report -m