import  unittest
from GetTokens import GetTokens

class TestTokens(unittest.TestCase):
    def test1(self):
        expr="5+3"
        arr = ["+","5","+","3"]
        self.assertEqual(arr,GetTokens(expr))
    def testOneNumber(self):
            expr = "5"
            arr = ["+", "5"]
            self.assertEqual(arr, GetTokens(expr))
    def testEmpty(self):
            expr = ""
            arr = []
            self.assertEqual(arr, GetTokens(expr))
    def testOneNegativeNumber(self):
        expr = "-5"
        arr = ["-", "5"]
        self.assertEqual(arr, GetTokens(expr))
    def test2(self):
        expr="12/4"
        arr = ["+","12","/","4"]
        self.assertEqual(arr,GetTokens(expr))
    def test3(self):
        expr="11*12+5   "
        arr = ["+","11","*","12","+","5"]
        self.assertEqual(arr,GetTokens(expr))
    def test4(self):
        expr="  5  +  3  "
        arr = ["+","5","+","3"]
        self.assertEqual(arr,GetTokens(expr))
    def test5(self):
        expr="-5*3   "
        arr = ["-","5","*","3"]
        self.assertEqual(arr,GetTokens(expr))
    def test6(self):
        expr = "  11-4"
        arr = ["+", "11", "-", "4"]
        self.assertEqual(arr,GetTokens(expr))
    def test7(self):
        expr = "  11 - 4 +5 * 2-12/4+11*12*15"
        arr = ["+", "11", "-", "4","+","5","*","2","-","12","/","4","+","11","*","12","*","15"]
        self.assertEqual(arr,GetTokens(expr))
    def testManyMultiplications(self):
        expr = "  11*12*15"
        arr = ["+", "11", "*", "12", "*", "15"]
        self.assertEqual(arr, GetTokens(expr))
if __name__ == "__main__":
    unittest.main()