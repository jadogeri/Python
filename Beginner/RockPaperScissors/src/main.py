
import sys
import time
import random


from utils.utils import *
from os.path import dirname, abspath
# dir_src = dirname((abspath(__file__)))

# print('line 7',dir_src)

# #dir_utils = dir_src + '\utils'

# sys.path.append(dir_src)
# #sys.path.append(dir_utils)

#print('ager is === '+ str(ager))

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
 


