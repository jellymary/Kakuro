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
        self.block.append_cell(Cell(True, 12, Location(0, 1)))

    def test_initial_block(self):
        self.assertSequenceEqual([None, None, None], self.block.value_cells)

    def test_append_cell(self):
        cell = Cell(False, 2, Location(0, 2))
        self.block.append_cell(cell)
        self.assertSequenceEqual([cell, None, None], self.block.value_cells)

    def test_get_known_values(self):
        self.block.append_cell(Cell(False, 2, Location(0, 2)))
        self.block.append_cell(Cell(False, 4, Location(0, 3)))
        self.block.append_cell(Cell(False, 6, Location(0, 4)))
        self.assertSequenceEqual([2, 4, 6], self.block.get_known_values())


if __name__ == "__main__":
    unittest.main()