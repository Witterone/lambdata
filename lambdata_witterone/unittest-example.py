# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:04:43 2020

@author: Ronin
"""


# Tests check that code does as it is intended.
# Regression in coding is going backwards in improvement

import unittest 
#supports unit tests
#unit is the smallest cohesive piece of code we can test
#integration many pieces, end to end testing all parts
#user acceptance, running


from example_module import increment

class EXampleModuleTests(unittest.TestCase):
    """ Making sure it works as expected """
    def test_increment(self):
        """testing that the increment function adds one"""
        x =7
        y = increment(x)
        w = -10
        v = increment(w)
        self.assertEqual(y,8)
        self.assertEqual(v,-9)
        
if __name__ == '__main__':
    #this conditional is for code that will be run
    #when we execute from command line
    unittest.main()
        