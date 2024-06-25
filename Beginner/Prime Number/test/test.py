import unittest
import sys


from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))

dir_src = dir +'\\src'
print(dir_src)

dir_tests = dir +'\tests';


sys.path.append(dir_src)
sys.path.append(dir_tests)

from utils.utils import isPrimeNumber

class PrimeNumberTest(unittest.TestCase):

   
    def setUp(self):
 
        print("SETUP called ...");
        # Arrange 

        self.num1 : int = 24
        self.num2 : int = 97;
     
    def tearDown(self) :
        print("TEARDOWN called ...");

        self.num1 = 0;
        self.num2 = 0;
       
    def test_is_prime_number(self):
        #Act
        result = isPrimeNumber(self.num2)
        #Assert
        self.assertTrue(result)

    def test_is_not_prime_number(self):
        #Act
        result = isPrimeNumber(self.num1)
        #Assert
        self.assertFalse(result)



if __name__ == "__main__":
    unittest.main()