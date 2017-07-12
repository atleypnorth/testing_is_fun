import unittest

from functions import add_numbers, multiply, average2, average


class TestFunctions(unittest.TestCase):

    def test_add(self):
        '''Test the addition of two numbers'''

        self.assertEqual(add_numbers(1, 1), 2)
        self.assertEqual(add_numbers(1, 2), 3)
        with self.assertRaises(TypeError):
            add_numbers(1, None)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)

    def test_average2(self):
        self.assertEqual(average2(2, 4), 3)

    def test_average(self):
        self.assertEqual(average(2, 4), 3)


if __name__ == '__main__':
    unittest.main()
