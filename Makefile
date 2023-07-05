test:
	echo "Running tests..."
	coverage run -m html_parser.test.test_maker
	coverage run -m html_parser.test.test_judge
	coverage run -m html_parser.test.test_sanitizer
	coverage run -m html_parser.test.test_semantics
	coverage run -m automation.test.test_browser

format:
	echo "Formatting..."
	black .