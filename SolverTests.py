import unittest
from Solver import solve_expression


class TestSolve(unittest.TestCase):
    def test1(self):
        arr = ["+", "5", "+", "3"]
        expected = 8.0
        self.assertEqual(expected, solve_expression(arr))

    def testOneNumber(self):
        arr = ["+", "5"]
        expected = 5.0
        self.assertEqual(expected, solve_expression(arr))

    def testEmpty(self):
        arr = ["+", "0"]
        expected = 0.0
        self.assertEqual(expected, solve_expression(arr))

    def testOneNegativeNumber(self):
        arr = ["-", "5"]
        expected = -5.0
        self.assertEqual(expected, solve_expression(arr))

    def test2(self):
        arr = ["+", "12", "/", "4"]
        expected = 3.0
        self.assertEqual(expected, solve_expression(arr))

    def test3(self):
        arr = ["+", "11", "*", "12", "+", "5"]
        expected = 137.0
        self.assertEqual(expected, solve_expression(arr))

    def test4(self):
        arr = ["+", "5", "-", "3"]
        expected = 2.0
        self.assertEqual(expected, solve_expression(arr))

    def test5(self):
        arr = ["+", "0", "-", "5", "*", "3"]
        expected = -15.0
        self.assertEqual(expected, solve_expression(arr))

    def test6(self):
        arr = ["+", "11", "-", "4"]
        expected = 7.0
        self.assertEqual(expected, solve_expression(arr))

    def test7(self):
        arr = ["+", "11", "-", "4"]
        expected = 7.0
        self.assertEqual(expected, solve_expression(arr))

    def testComplex(self):
        arr = [
            "+",
            "11",
            "-",
            "4",
            "+",
            "5",
            "*",
            "2",
            "-",
            "12",
            "/",
            "4",
            "+",
            "11",
            "*",
            "12",
            "*",
            "15",
        ]
        expected = 1994.0
        self.assertEqual(expected, solve_expression(arr))

    def testManyMultiplications(self):
        expected = 1980.0
        arr = ["+", "11", "*", "12", "*", "15"]
        self.assertEqual(expected, solve_expression(arr))

    def testManyDivides(self):
        expected = 140 / 5 / 6
        arr = ["+", "140", "/", "5", "/", "6"]
        self.assertEqual(expected, solve_expression(arr))

    def testBrackets_plus(self):
        expected = 11
        arr = ["+", "5", "+", "(", "10", "-", "4", ")"]
        self.assertEqual(expected, solve_expression(arr))

    def testBrackets_mult(self):
        expected = 30
        arr = ["+", "5", "*", "(", "10", "-", "4", ")"]
        self.assertEqual(expected, solve_expression(arr))

    def testBrackets_mult2x(self):
        expected = 220
        arr = ["+", "5", "*", "(", "11", "*", "4", ")"]
        self.assertEqual(expected, solve_expression(arr))

    def testBrackets_negative_in_brackets(self):
        expected = -220
        arr = ["+", "5", "*", "(", "11", "*", "(", "-", "4", ")", ")"]
        self.assertEqual(expected, solve_expression(arr))

    def testInBracket(self):
        expected = 15
        arr = ["(", "12", "+", "3", ")"]
        self.assertEqual(expected, solve_expression(arr))


if __name__ == "__main__":
    unittest.main()
