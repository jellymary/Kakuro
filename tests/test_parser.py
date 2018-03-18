import unittest

from modules.opener import Opener
from modules.parser import Parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        raw = Opener.open_file('1')
        self.kakuro = Parser.parse(raw)

    def test_correct_size(self):
        pass


if __name__ == "__main__":
    unittest.main()
