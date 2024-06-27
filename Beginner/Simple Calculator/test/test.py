import unittest
import sys


from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))

dir_src = dir +'\\src'
print(dir_src)

dir_tests = dir +'\tests';


sys.path.append(dir_src)
sys.path.append(dir_tests)

from utils import compute_values, is_valid_symbol;

class SimpleCalculatorTest(unittest.TestCase):

   
    def setUp(self):
 
        print("SETUP called ...");
        # Arrange 

        self.plus : str = "+";
        self.minus : str = "-";
        self.minus : str = "-";
        self.star : str = "*";
        self.small_x : str = "x";
        self.large_X : str = "X";
        self.divide : str = "/";
        self.mod : str = "%";
    
        self.num1 : int = 50;
        self.num2 : int = 100;
        
        self.symbol : str = "$";
     
    def tearDown(self) :
        print("TEARDOWN called ...");

        self.num1 = 0;
        self.num2 = 0;
       
    def test_is_add(self):
        #Act
        result = is_valid_symbol(self.plus);
        #Assert
        self.assertTrue(result);

    def test_is_minus(self):
        #Act
        result = is_valid_symbol(self.minus);
        #Assert
        self.assertTrue(result)

    def test_is_star(self):
        #Act
        result = is_valid_symbol(self.star)
        #Assert
        self.assertTrue(result)

    def test_is_small_x(self):
        #Act
        result = is_valid_symbol(self.small_x);
        #Assert
        self.assertTrue(result)

    def test_is_divide(self):
        #Act
        result = is_valid_symbol(self.divide)
        #Assert
        self.assertTrue(result)

    def test_is_mod(self):
        #Act
        result = is_valid_symbol(self.minus)
        #Assert
        self.assertTrue(result)
    
    def test_is_valid_symbol(self):
        #Act
        result = is_valid_symbol(self.num1)
        #Assert
        self.assertFalse(result)




if __name__ == "__main__":
    unittest.main();

