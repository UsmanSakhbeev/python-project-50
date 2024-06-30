install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

build:
	poetry build

reinstal:
	python3 -m pip install --user dist/*.whl --force-reinstall
