import unittest
import sys

from os.path import dirname, abspath
root_dir = dirname(dirname(abspath(__file__)))

dir_src = root_dir +'\\src'
dir_tests = root_dir +'\\tests'
sys.path.append(dir_src)
sys.path.append(dir_tests)

from utils.utils import get_round_outcome,get_round_count,is_valid_entry

class RockPaperScissorsTest(unittest.TestCase):
   
    def setUp(self):
 
        print("SETUP called ...");
        # Arrange 
        self.player1 = 'ROCK'
        self.player2 = 'PAPER'
        self.player3 = 'SCISSORS'

        self.cpu1 = 'ROCK'
        self.cpu2 = 'PAPER'
        self.cpu3 = 'SCISSORS'

        self.ROUND_TEXT = "10"
        self.ERROR_TEXT = "PYTHON"
       
                    
    def tearDown(self) :
        print("TEARDOWN called ...");

        self.round = 0
       
        
    def test_get_tied_by_rock(self):
        #Act
        print("player1 == ",self.player1)
        print("cpu1 == ",self.cpu1)

        result =  get_round_outcome(self.player1,self.cpu1) 
        #Assert_
        self.assertEqual(result,'TIE') 
    
    def test_get_tied_by_paper(self):
        #Act
        result =  get_round_outcome(self.player2,self.cpu2) 
        #Assert_
        self.assertEqual(result,'TIE') 
    
    def test_get_tied_by_scissors(self):
        #Act
        result =  get_round_outcome(self.player3,self.cpu3) 
        #Assert_
        self.assertEqual(result,'TIE') 

    def test_get_cpu_win_by_rock(self):
        #Act
        result =  get_round_outcome(self.player3,self.cpu1) 
        #Assert_
        self.assertEqual(result,'CPU WINS') 
    
    def test_get_cpu_win_by_paper(self):
        #Act
        result =  get_round_outcome(self.player1,self.cpu2) 
        #Assert_
        self.assertEqual(result,'CPU WINS') 
    
    def test_get_cpu_win_by_scissors(self):
        #Act
        result =  get_round_outcome(self.player2,self.cpu3) 
        #Assert_
        self.assertEqual(result,'CPU WINS') 
    

    def test_get_player_win_by_rock(self):
        #Act
        result =  get_round_outcome(self.player1,self.cpu3) 
        #Assert_
        self.assertEqual(result,'PLAYER WINS') 

    def test_get_player_win_by_paper(self):
        #Act
        result =  get_round_outcome(self.player2,self.cpu1) 
        #Assert_
        self.assertEqual(result,'PLAYER WINS') 

    def test_get_player_win_by_scissors(self):
        #Act
        result =  get_round_outcome(self.player3,self.cpu2) 
        #Assert_
        self.assertEqual(result,'PLAYER WINS') 

    def test_get_round_count(self):
        #Act
        result =  get_round_count(self.ROUND_TEXT) 
        #Assert_
        self.assertEqual(result,10) 

    def test_error_get_round_count(self):
        try:
        #Act
            get_round_count(self.ERROR_TEXT)
        #Assert
        except ValueError as e: 
            self.assertEqual(type(e), ValueError) 
    
    def test_true_entry(self):
        
        #Act
            entry = is_valid_entry(self.player1)
        #Assert
            self.assertTrue(entry);

    def test_false_entry(self):
        
        #Act
            entry = is_valid_entry(self.ERROR_TEXT)
        #Assert
            self.assertFalse(entry);
    
if __name__ == "__main__":
    unittest.main()

