import unittest
import sys

from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))

dir_src = dir +'\src'
print(dir_src)

dir_tests = dir +'\tests'
#dir_utils = dir_src + '\utils'


sys.path.append(dir_src)
sys.path.append(dir_tests)
#sys.path.append(dir_utils)

from utils.utils import is_odd



class ValidateAgeTest(unittest.TestCase):

   
    def setUp(self):
 
        print("SETUP called ...");
        # Arrange 
        self.num1 = 2
        self.num2 = 3
        self.num3 = 100000001
     
    def tearDown(self) :
        print("TEARDOWN called ...");

        self.num1 = 0;
        self.num2 = 0;
        self.num3 = 0;
       
    def test_not_even_number(self):
        #Act
        result = is_odd(self.num1)
        #Assert
        self.assertEqual(False,result)
    
    def test_even_number(self):
        #Act
        result = is_odd(self.num1)
        #Assert
        self.assertEqual(False,result)

    def test_odd_number(self):
        #Act
        result = is_odd(self.num2)
        #Assert
        self.assertEqual(True,result)


    def test_odd_binary_number(self):
        #Act
        print(self.num3)
        result = is_odd(self.num3)
        #Assert
        self.assertEqual(True,result)
    
    def test_not_even_binary_number(self):
        #Act
        print(self.num3)
        result = is_odd(self.num3)
        #Assert
        self.assertEqual(True,result)


if __name__ == "__main__":
    unittest.main()