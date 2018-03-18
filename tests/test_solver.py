import unittest

from solver import Solver
from modules.utils.block import Block
from modules.utils.location import Location


class SolverTest(unittest.TestCase):
    def test_repeating_part(self):
        self.assertEqual(True, Solver._is_repeating_part('1111'))
        self.assertEqual(True, Solver._is_repeating_part('1234567891'))
        self.assertEqual(False, Solver._is_repeating_part('1'))
        self.assertEqual(False, Solver._is_repeating_part('97531'))

    def test_get_partitions(self):
        test_partitions = {
            (3, 2): ['21'],
            (7, 2): ['43', '52', '61'],
            # (16, 3): ['745', '763'],
            (26, 5): ['86543', '87542', '87632', '87641',
                      '96542', '97532', '97541', '97631', '98432', '98531', '98621'],
            (28, 7): ['7654321'],
            (45, 9): ['987654321'],

            (31, 10): [],
            (21, 2): [],

            (14, 2, 6): ['86'],
            (9, 3, 4, 1): []
        }
        for sum_and_count, expected in test_partitions.items():
            with self.subTest(sum_and_count=sum_and_count):
                actual = Solver.get_partitions(*sum_and_count)
                actual.sort()
                self.assertSequenceEqual(expected, actual)

    def test_equals_get_block_partitions_and_get_partitions(self):
        block = Block(Location(1, 0), 16, 3, False)
        self.assertSequenceEqual(['97'], Solver.get_block_partitions(block))
        # self.assertSequenceEqual(Solver.get_block_partitions(block), Solver.get_partitions(16, 2))


if __name__ == "__main__":
    unittest.main()
