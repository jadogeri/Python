import unittest

from constants import *
from main import validateAge

class ValidateAgeTest(unittest.TestCase):

   # Arrange 
    num1 = 17
    num2 = 19
    num3 = 24

    def setup(self):
 
        print("SETUP called ...");
     
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