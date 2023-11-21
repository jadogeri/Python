import unittest

def sum(a,b):
    return a + b;

class unitTest(unittest.TestCase):

    def setup(self):
    # Arrange 
        print("SETUP called ...");
        self.num1 = 10
        self.num2 = 15
        self.num3 = 17
        self.num4 = 18
        self.num5 = 20
        self.num6 = 21
        self.num7 = 25

    # Act


    # Assert
    def test_test(self):
        pass;
    def test_test2(self):
        pass;

class unitTest2(unittest.TestCase):
    def test_test(self):
        pass;
    def test_test2(self):
        pass;


    
    


if __name__ == "__main__":
    unittest.main()