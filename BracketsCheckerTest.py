import unittest
from StackForBrackets import get_enclosing_bracket_ind


class TestBrackets(unittest.TestCase):
    def test1(self):
        s="( )"
        opening_ind = 15
        expected = 17
        self.assertEqual(expected, get_enclosing_bracket_ind(s,opening_ind))
    def test2(self):
        s="("
        opening_ind = 15
        expected = False
        self.assertEqual(expected, get_enclosing_bracket_ind(s,opening_ind))
    def test3(self):
        s = "(())"
        opening_ind = 15
        expected = 18
        self.assertEqual(expected, get_enclosing_bracket_ind(s, opening_ind))
    def test4(self):
        s = "(33(11)22)"
        opening_ind = 15
        expected = 24
        self.assertEqual(expected, get_enclosing_bracket_ind(s, opening_ind))
    def test5(self):
        s = "(()"
        opening_ind = 15
        expected = False
        self.assertEqual(expected, get_enclosing_bracket_ind(s, opening_ind))


if __name__=="__main__":
    unittest.main()