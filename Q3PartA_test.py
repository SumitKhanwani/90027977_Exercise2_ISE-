import unittest
from Q3PartA import move_direction

class MoveDirectionTestCase(unittest.TestCase):
    def test_valid_positions_and_directions(self):
        test_cases = [
            ((3, 4), 'N', (3, 3)),
            ((0, 0), 'S', (0, 1)),
            ((6, 6), 'E', (7, 6)),
            ((2, 2), 'W', (1, 2)),
            ((4, 5), 'NE', (5, 4)),
            ((6, 1), 'NW', (5, 0)),
            ((3, 3), 'SE', (4, 4)),
            ((1, 5), 'SW', (0, 6)),
        ]

        for pos, direction, expected in test_cases:
            with self.subTest(pos=pos, direction=direction):
                result = move_direction(direction, *pos)
                self.assertEqual(result, expected)

    def test_invalid_positions(self):
        test_cases = [
            (-1, 3),
            (5, 8),
        ]

        for pos in test_cases:
            with self.subTest(pos=pos):
                with self.assertRaises(ValueError):
                    move_direction('N', *pos)

    def test_invalid_direction(self):
        with self.assertRaises(ValueError):
            move_direction('X', 2, 4)

if __name__ == '__main__':
    unittest.main()
