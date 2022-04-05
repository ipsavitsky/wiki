format-check:
	black --check .
format:
	black .
typecheck:
	mypy -p wiki --no-incremental
typecheck-report:
	mypy -p wiki --html-report mypy_report