#!/usr/bin/env python

# Create Unittests for both modules
# Make sure each class/method includes a docstring
# Make sure entire script conforms to PEP8 guidelines
# To test, run the script in the terminal.


# Standard Python Library
import unittest

# Local Imports
from puppy import Puppy, Leech
from arithmetic import SimpleOperations, Complex


case1 = SimpleOperations(3, 2)
case2 = Complex(3, 2)
case3 = Puppy('James', 5)
case4 = Leech('Jonathan', 10, True)


class ArithmeticTest(unittest.TestCase):
    # TODO


class PuppyTest(unittest.TestCase):
    # TODO


if __name__ == "__main__":
    unittest.main()

