import math
def isPrimeNumber(user_choice : int):
    
    outcome : bool = True;   

    if (user_choice <= 1):
        outcome = False;
        return outcome; 
    if (user_choice == 2 or user_choice == 3):
            return True;
    if (user_choice % 2 == 0 or user_choice % 3 == 0):
            return False;
    else: 
       
       for i in range(2, int(math.sqrt(user_choice)) + 1):
          if (user_choice % i == 0 ):
             return False;
    return outcome;