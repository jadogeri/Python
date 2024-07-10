import unittest
import sys


from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))

dir_src = dir +'\\src'
print(dir_src)

dir_tests = dir +'\tests';


sys.path.append(dir_src)
sys.path.append(dir_tests)

from utils.utils import factorial

class FactorialTest(unittest.TestCase):

   
    def setUp(self):
 
        print("SETUP called ...");
        # Arrange 

        self.num1 : int = 0
        self.num2 : int = 1;
        self.num3 : int = 3;

     
    def tearDown(self) :
        print("TEARDOWN called ...");

        self.num1 = 0;
        self.num2 = 0;
        self.num3 = 0;

       
    def test_base_case_0(self):
        #Act
        result = factorial(self.num1)
        #Assert
        self.assertEqual(result,1)

    def test_base_case_1(self):
        #Act
        result = factorial(self.num2)
        #Assert
        self.assertEqual(result, 1)

    def test_correct_factorial(self):
        #Act
        result = factorial(self.num3)
        #Assert
        self.assertEqual(result, 6)



if __name__ == "__main__":
    unittest.main()