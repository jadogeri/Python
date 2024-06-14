import unittest
import sys

from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))

dir_src = dir +'\\src'
print(dir_src)

dir_tests = dir +'\tests'


sys.path.append(dir_src)
sys.path.append(dir_tests)

from main import calculate_area, convert_string_to_number
from constants import *


class AreaOfASquareTest(unittest.TestCase):

   
    def setUp(self):
 
        print("SETUP called ...");
        # Arrange 
        self.num1 = 10;
        self.num2 = 2.5;
        self.str1 = "10";
        self.str2 = "2.5";
        self.str3 = "PYTHON";


     
    def tearDown(self) :
        print("TEARDOWN called ...");

        self.num1 = 0;
        self.num2 = 0;
        self.str1 = "";
        self.str2 = "";
        self.str3 = "";

       
    def test_calculate_area_with_int(self):
        #Act
        result = calculate_area(self.num1)
        #Assert
        self.assertEqual(100,result)

    def test_calculate_area_with_float(self):
        #Act
        result = calculate_area(self.num2)
        #Assert
        self.assertEqual(6.25,result)

    def test_convert_string_to_int(self):
        #Act
        result = convert_string_to_number(self.str1)
        #Assert
        self.assertEqual(10,result)

    def test_convert_string_to_float(self):
        #Act
        result = convert_string_to_number(self.str2)
        #Assert
        self.assertEqual(2.5,result)

    def test_error_convert_string(self):
        try:
        #Act
            convert_string_to_number(self.str3)
        #Assert
        except ValueError as e: 
            self.assertEqual(type(e), ValueError) 





if __name__ == "__main__":
    unittest.main()