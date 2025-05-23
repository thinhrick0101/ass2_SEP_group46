"""
This is a comment
"""
# pylint: disable=E0401
import unittest
from calculator import divide
class TestDivision(unittest.TestCase):
    """
    This is a comment
    """
    def test_divide_normal(self):
        """
        This is a comment
        """
        self.assertAlmostEqual(divide(10, 2), 5.0, places=4, msg="10 / 2 should be 5")
        self.assertAlmostEqual(divide(9, 3), 3.0, places=4, msg="9 / 3 should be 3")

    def test_divide_with_decimals(self):
        """
        This is a comment
        """
        self.assertAlmostEqual(divide(5, 2), 2.5, places=4, msg="5 / 2 should be 2.5")
        self.assertAlmostEqual(divide(7, 3), 2.3333, places=4, msg="should be equal 2.3333")

    def test_divide_by_zero(self):
        """
        This is a comment
        """
        with self.assertRaises(ValueError) as context:
            divide(1, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
