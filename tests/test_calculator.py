try:
    import sys
    import os
    
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from calculator import sum,subtract

class TestCalculadora(unittest.TestCase):
    def test_sum_5_5_must_return_10(self):
        self.assertEqual(sum(5,5), 10)

    def test_sum_5_negative_and_5_must_return_0(self):
        self.assertEqual(sum(-5,5), 0)

    def test_sum_multiple_entries(self):
        x_y_exits=(
        (10, 10, 20),
        (5, 5, 10),
        (1.5, 1.5, 3.0),
        (-5, 5, 0),
        (100, 100, 200),
        )

        for x_y_exit in x_y_exits:
            with self.subTest(x_y_saida=x_y_exits):
                x, y, exit = x_y_exit
                self.assertEqual(sum(x,y), exit) 

    def test_x_not_is_int_or_float_must_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum('11', 0)

    def test_y_not_is_int_or_float_must_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum(11, '0')

    def test_subtraction_5_4_must_return_1(self):
        self.assertEqual(subtract(5,4), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)