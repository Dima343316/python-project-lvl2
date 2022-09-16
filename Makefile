#!/usr/bin/env python
install:#Обновление
	poetry install
gendiff:#запуск скрипта
	poetry run gendiff
build:#создание билда
	poetry publish --dry-run
package-install:#package
	python3 -m pip install --user dist/*.whl
lint:#запуск flake8
	poetry run flake8 gendiff
test:#запуск тестов
	poetry run pytest -vv
test-coverage:#запуск тестов в CodeClimate
	poetry run pytests --cov=gendiff --cov-report xml
