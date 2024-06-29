install:
	poetry install

test:
	poetry run pytest --cov=gendiff --cov-report xml

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff
