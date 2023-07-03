from html_parser.context_maker.counter import Counter
import unittest


class TestCounter(unittest.TestCase):
    def test_build_successful(self):
        Counter(3)


unittest.main()
