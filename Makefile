test:
	echo "Running tests..."
	python3 -m html_parser.test.test_maker
	python3 -m html_parser.test.test_sanitizer
	