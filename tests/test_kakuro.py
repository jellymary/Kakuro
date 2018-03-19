import unittest

from modules.opener import Opener
from modules.parser import Parser
from modules.kakuro import Kakuro
from modules.utils.location import Location


class KakuroTest(unittest.TestCase):
    def setUp(self):
        raw = Opener.open_file('..\\modules\\fields\\1')
        self.kakuro = Parser.parse(raw)

    def test_initial(self):
        pass

    def test_find_adjacent_block(self):
        block = self.kakuro.blocks[0]
        expected = [Location(0, 1), Location(0, 2)]
        actual = [x.location for x, y in self.kakuro.find_all_adjacents_blocks(block)]
        self.assertSequenceEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
