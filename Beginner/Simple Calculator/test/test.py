import unittest
import sys


from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))

dir_src = dir +'\\src'
print(dir_src)

dir_tests = dir +'\tests';


sys.path.append(dir_src)
sys.path.append(dir_tests)

from utils.utils import compute_values, is_valid_symbol

class SimpleCalculatorTest(unittest.TestCase):

   
    def setUp(self):
 
        print("SETUP called ...");
        # Arrange 

        self.plus : str = "+";
        self.minus : str = "-";
     
    def tearDown(self) :
        print("TEARDOWN called ...");

        self.num1 = 0;
        self.num2 = 0;
       
    def test_is_add(self):
        #Act
        result = compute_values(self.num2)
        #Assert
        self.assertTrue(result)

    def test_is_minus(self):
        #Act
        result = compute_values(self.num1)
        #Assert
        self.assertFalse(result)
    
    def test_is_valid_symbol(self):
        #Act
        result = is_valid_symbol(self.num1)
        #Assert
        self.assertFalse(result)




if __name__ == "__main__":
    unittest.main()