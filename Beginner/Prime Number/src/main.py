from constants import *


# if __name__ == "__main__":
#     print("the main prog")
# else:
#     print("not the main prog")
input_count : int = 0
while (input_count == 0):
    try:
        input_count = int(input("how many inputs?\n"));        

    except  ValueError as err :
        print(err)

def isPrimeNumber(user_choice : int):
    
    outcome : bool = False;
    exponent : int = 0;
    base : int = 2;

    if (user_choice == 1 or user_choice == 0):
        outcome = False;
        return outcome; 
    elif (user_choice == 2 or user_choice == 3):
        outcome = True;
        return outcome;
    elif (user_choice % 2 == 0 or user_choice % 3 == 0):
        outcome = False;
        return outcome;    
    else:    
        n : int = 1;
        run : bool = True;
        upper_bound : int = (6 * n) + 1;
        lower_bound : int = (6 * n) - 1;
   
        while (run and (n <= user_choice or n >= user_choice)): 
            print("in loop")
            print("upper_bound == ", upper_bound);
           

            if (user_choice == upper_bound or user_choice == lower_bound ):                
                outcome = True;
                return outcome;
            if ( upper_bound > user_choice):
                run = False;
            else:
                n = n + 1;
        return outcome;

def  recur(n : int, user_choice : int):
    if (((6 * n) - 1 == user_choice) or ((6 * n) + 1 == user_choice)):
        return True
 


while (input_count > 0 and __name__ == "__main__") :
    try:
        input_string = str(input("Enter numner?\n"));
        input_int = int(input_string);

        if(isPrimeNumber(input_int)):
            print("True");
        else:
            print("False");
        input_count -= 1
    except ValueError as err :
        print(err);
   
 
"""

import time
import random


from utils.utils import *

choices = []

rounds : int = 0;

try:
    file = open('constants.txt')
    cpu_choices = file.readlines();
    file.close();
    rock, paper ,scissors = cpu_choices ;
    round_text = input("how many rounds\n");

    rounds = get_round_count(round_text);

except  ValueError as err :
    print(err)

    



try:
        player_choice = input("TYPE [ROCK], [PAPER] OR [SCISSORS]\n");
        if (is_valid_entry(player_choice)) :
            
            cpu_choice = random.choice(cpu_choices);
            print("cpu chose "+ cpu_choice);
            outcome = get_round_outcome(player_choice,cpu_choice);
            time.sleep(3);
            print(outcome);
            rounds -= 1;
        else:
            print("ENTRY '",player_choice,"' IS NOT A VALID INPUT");


"""