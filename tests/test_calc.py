import unittest

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

    def test_str(self):
        stud = Student("Faraz","CS")
        self.assertEqual(stud.__str__(),"Faraz")

if __name__=="__main__":
    unittest.main()