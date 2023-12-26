import unittest
import sys

from os.path import dirname, abspath
root_dir = dirname(dirname(abspath(__file__)))

dir_src = root_dir +'\\src'
dir_tests = root_dir +'\tests'
sys.path.append(dir_src)
sys.path.append(dir_tests)

from utils.utils import *

class StudentGraderTest(unittest.TestCase):
   
    def setUp(self):
 
        print("SETUP called ...");
        # Arrange 

        self.invalid_score1 = 101
        self.invalid_score2 = -5
        self.homework1 = 50       
        self.test1 = 80
        self.lab1 = 90
                    
    def tearDown(self) :
        print("TEARDOWN called ...");

        self.invalid_score1 = 0
        self.invalid_score2 = 0
        self.homework1 = 0            
        self.test1 = 0   
        self.lab1 = 0     
        
    def test_invalid_score_greater_than_out_of_bounds(self):
        #Act
        result = is_valid_score(self.invalid_score1)
        #Assert_
        self.assertFalse(result)
    
    def test_invalid_score_less_than_out_of_bounds(self):
        #Act
        result = is_valid_score(self.invalid_score2)
        #Assert_
        self.assertFalse(result)
    
    def test_valid_score(self):
        #Act
        result = is_valid_score(self.homework1)
        #Assert_
        self.assertEqual(result,True)
          
    def test_get_lab_percentage(self):
        #Act
        result = get_lab_percentage_score(self.lab1)
        #Assert
        self.assertEqual(result,9)

    def test_get_test_percentage(self):
        #Act
        result = get_test_percentage_score(self.test1)
        #Assert
        self.assertEqual(result,32)
    def test_get_homework_percentage(self):
        #Act
        result = get_homework_percentage_score(self.homework1)
        #Assert
        self.assertEqual(25,result)     


if __name__ == "__main__":
    unittest.main()

