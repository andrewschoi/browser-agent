from html_parser.context_maker.judge import Judge
import unittest


class TestJudge(unittest.TestCase):
    def test_build_successful(self):
        Judge(3)


unittest.main()
