import unittest

from mypack.records import Student

class Tests(unittest.TestCase):
    def test_str1(self):
        stud = Student("Faraz","CS")
        self.assertEqual(stud.__str__(),"Faraz")

    def test_str2(self):
        stud = Student("Chetan","CS")
        self.assertEqual(stud.__str__(),"Chetan")

if __name__=="__main__":
    unittest.main()