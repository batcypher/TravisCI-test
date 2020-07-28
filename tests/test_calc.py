import unittest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from mypack.operation import Calculator


class Tests(unittest.TestCase):
    def test_add1(self):
        calc = Calculator()
        self.assertEqual(calc.addition(3,5),8)

    def test_add2(self):
        calc = Calculator()
        self.assertEqual(calc.addition(9,5),14)

    def test_multi(self):
        calc = Calculator()
        self.assertEqual(calc.multiplication(4,5),20)

if __name__=="__main__":
    unittest.main()