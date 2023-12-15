import unittest
import sys

from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))

dir_src = dir +'\src'
print(dir_src)

dir_tests = dir +'\tests'


sys.path.append(dir_src)
sys.path.append(dir_tests)

from main import validateAge
from constants import *


class ValidateAgeTest(unittest.TestCase):

   
    def setUp(self):
 
        print("SETUP called ...");
        # Arrange 
        self.num1 = 17
        self.num2 = 19
        self.num3 = 24
     
    def tearDown(self) :
        print("TEARDOWN called ...");

        self.num1 = 0;
        self.num2 = 0;
        self.num3 = 0;
       
    def test_minor_age(self):
        #Act
        result = validateAge(self.num1)
        #Assert
        self.assertEqual(MINOR_AGE_PROMPT,result)

    def test_club_age(self):
        #Act
        result = validateAge(self.num2)
        #Assert
        self.assertEqual(CLUB_AGE_PROMPT,result)


    def test_drinking_age(self):
        #Act
        print(self.num3)
        result = validateAge(self.num3)
        #Assert
        self.assertEqual(ADULT_AGE_PROMPT,result)


if __name__ == "__main__":
    unittest.main()