import unittest
from io import StringIO
from unittest.mock import patch
from Q3PartC import pie_divider

class TestPieDivider(unittest.TestCase):
    def test_boundary_values(self):
        with patch('builtins.input', side_effect=['1', '0']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                pie_divider()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "Invalid\n0\nPerfect")

    def test_path_coverage(self):
        with patch('builtins.input', side_effect=['-10', '0']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                pie_divider()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "Invalid")

        with patch('builtins.input', side_effect=['-2', '10']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                pie_divider()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "Invalid")

    def test_statement_coverage(self):
        with patch('builtins.input', side_effect=['4', '12']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                pie_divider()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "3\n0")

        with patch('builtins.input', side_effect=['7', '25']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                pie_divider()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "3\n4")

if __name__ == '__main__':
    unittest.main()
