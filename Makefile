env:
	virtualenv env 

init:
	pip install -r requirements.txt

test:
	python -m pytest --cov=wordsearch
