import unittest
from Solver import arithm_parser

class TestArithmeticParser(unittest.TestCase):
    def testCurrentArithmOperator(self):
        curr_token="+"
        next_token="11"
        general_sum=10.0
        curr_variable=3
        expected=(13,11.0)
        self.assertEqual(expected,arithm_parser(curr_token,next_token,general_sum,curr_variable))
    def testCurrentNumber(self):
        curr_token="11"
        next_token="-"
        general_sum=10.0
        curr_variable=3.0
        expected=(10.0,3.0)
        self.assertEqual(expected,arithm_parser(curr_token,next_token,general_sum,curr_variable))

if __name__=="__main__":
    unittest.main()