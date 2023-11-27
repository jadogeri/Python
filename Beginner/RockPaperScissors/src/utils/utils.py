
def get_round_count():
    total_rounds = 0
    try:
        count = int(input("how many rounds\n"))  
        total_rounds = count      
    except ValueError as err :
        print(err)
    return total_rounds
    

ager = 700