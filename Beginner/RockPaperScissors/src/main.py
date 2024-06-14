
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

    
while (rounds > 0 and __name__ == "__main__") :
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
           
    except ValueError as err :
        print(err)
 


