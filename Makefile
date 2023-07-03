test:
	echo "Running tests..."
	coverage run -m html_parser.test.test_maker
	coverage run -m html_parser.test.test_sanitizer
	coverage run -m html_parser.test.test_semantics

format:
	echo "Formatting..."
	black .