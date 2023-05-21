import unittest
from Q3PartC import pie_divider

class TestPieDivider(unittest.TestCase):
    def test_boundary_values(self):
        # Test case 1: Minimum valid input values
        self.assertEqual(pie_divider(1, 0), (0, 0, "Perfect"))

        # Test case 2: Typical input values
        self.assertEqual(pie_divider(5, 15), (3, 0, ""))

        # Test case 3: Maximum valid input values
        self.assertEqual(pie_divider(100, 1000), (10, 0, ""))

    def test_path_coverage(self):
        # Test case 4: num_pies < 0 and num_people < 1
        self.assertEqual(pie_divider(-10, 0), (0, 0, "Invalid"))

        # Test case 5: num_pies >= 0 and num_people >= 1
        self.assertEqual(pie_divider(3, 10), (3, 1, ""))

    def test_statement_coverage(self):
        # Test case 6: Calculation of pies_per_person
        self.assertEqual(pie_divider(4, 15), (3, 3, ""))

        # Test case 7: Calculation of leftover_pies
        self.assertEqual(pie_divider(6, 20), (3, 2, ""))

if __name__ == '__main__':
    unittest.main()
