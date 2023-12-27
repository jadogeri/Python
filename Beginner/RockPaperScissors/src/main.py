
import sys
import time
import random


from utils.utils import *
from os.path import dirname, abspath


choices = []
file = open('constants.txt')
cpu_choices = file.readlines();
file.close()
rock, paper ,scissors = cpu_choices

rounds = get_round_count();
    
while (rounds > 0 and __name__ == "__main__") :
    try:
        player_choice = str(input("TYPE [ROCK], [PAPER] OR [SCISSORS]\n"))
        cpu_choice = random.choice(cpu_choices)
        print("cpu chose "+ cpu_choice)
        outcome = get_round_outcome(player_choice,cpu_choice)
        time.sleep(3)
        print(outcome)
        rounds -= 1
    except ValueError as err :
        print(err)
 


