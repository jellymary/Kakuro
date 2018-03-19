import unittest

from modules.utils.location import Location
from modules.utils.block import Block
from modules.utils.cell import Cell


class LocationTest(unittest.TestCase):
    def test_parse(self):
        location = Location.parse(',', '0,1')
        self.assertEqual(0, location.x)
        self.assertEqual(1, location.y)


class BlockTest(unittest.TestCase):
    def setUp(self):
        self.block = Block(Location(0, 1), 12, 4, True)
        location = Location(0, 1)
        self.block[location] = Cell(True, 12, location)

    # def test_initial_block(self):
    #     self.assertSequenceEqual([None, None, None], self.block.value_cells)

    def test_get_known_values(self):
        locations =[Location(0, 2), Location(0, 3), Location(0, 4)]
        values = [2, 4, 6]
        for i in range(len(values)):
            self.block[locations[i]] = Cell(False, values[i], locations[i])
        self.assertSequenceEqual(values, self.block.get_known_values())


if __name__ == "__main__":
    unittest.main()
