
def get_round_count():
    total_rounds = 0
    try:
        count = int(input("how many rounds\n"))  
        total_rounds = count      
    except ValueError as err :
        print(err)
    return total_rounds
    

def get_round_outcome(user_choice, cpu_choice):
    outcome = ""
    user_choice = user_choice.upper().strip()
    if (user_choice in cpu_choice):
        print("user_choice == " + user_choice + " and cpu_choice == " + cpu_choice)
        outcome = "TIE"
        return outcome;
    else:    
        if (user_choice in 'ROCK' and cpu_choice == 'SCISSORS'):
            print("user_choice == " + user_choice + " and cpu_choice == " + cpu_choice)
            outcome = "PLAYER WINS"
            return outcome;
        if (user_choice in 'PAPER' and cpu_choice == 'ROCK'):
            print("user_choice == " + user_choice + " and cpu_choice == " + cpu_choice)
            outcome = "PLAYER WINS"
            return outcome;
        if (user_choice in 'SCISSORS' and cpu_choice == 'PAPER'):
            print("user_choice == " + user_choice + " and cpu_choice == " + cpu_choice)
            outcome = "PLAYER WINS"
            return outcome;  
        else:       
            outcome = "CPU WINS"
            return outcome; 
       