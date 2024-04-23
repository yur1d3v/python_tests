"""
Red -> Create tests and watch them fail

Green -> Create the code and watch them get it right

Refactor -> refactor the code looking for points to improve and apply good
programming practices.

"""
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
from baconwitheggs import bacon_with_eggs

class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs_should_raise_assertion_error_if_it_does_not_receive_int(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('0')

    def test_bacon_and_eggs_should_return_bacon_and_eggs_if_input_is_a_multiple_of_3_and_5(self):
        inputs = (15, 30, 45, 60)
        exit = 'Bacon with eggs'

        for input in inputs:
            with self.subTest(input=input, exit=exit):
                self.assertEqual(
                    bacon_with_eggs(input),
                    exit,
                    msg=f'"{input}" not return "{exit}"'
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)