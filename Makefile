lint:
	poetry run isort . --check
	poetry run black . --check

test:
	poetry run pytest