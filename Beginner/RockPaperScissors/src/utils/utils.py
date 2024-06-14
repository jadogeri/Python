
def get_round_count(input : str):
    total_rounds = 0;
    total_rounds = int(input);   
    return total_rounds;
    

def get_round_outcome(user_choice : str, cpu_choice : str):
    outcome = ""
    user_choice = user_choice.upper().strip()
    cpu_choice = cpu_choice.upper().strip();
    if (user_choice == cpu_choice):
        outcome = "TIE"
        return outcome;
    else:    
        if (user_choice == 'ROCK' and cpu_choice == 'SCISSORS'):
            outcome = "PLAYER WINS";
            return outcome;
        elif (user_choice == 'PAPER' and cpu_choice == 'ROCK'):
            outcome = "PLAYER WINS";
            return outcome;
        elif (user_choice == 'SCISSORS' and cpu_choice == 'PAPER'):
            outcome = "PLAYER WINS";
            return outcome;  
        else:       
            outcome = "CPU WINS";
            return outcome; 

def is_valid_entry(input: str):
    is_valid : bool;
    capital_input = input.upper().strip();
    
    if (capital_input == "ROCK" or capital_input == "PAPER" or capital_input == "SCISSORS" ) :
        is_valid = True;
    else :
        is_valid = False;

    return is_valid;

       