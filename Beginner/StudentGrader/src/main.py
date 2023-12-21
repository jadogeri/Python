from constants import *
from utils.utils import *


run = True;

test = 0
lab = 0
homework = 0
user_score = 0

test_percentage     = 0.4
lab_perentage       = 0.1
homework_percentage = 0.5

while (run and __name__ == "__main__") :
    try:
        counter = 3
        while(counter > 0):
            user_score = int(input());
            if is_valid_score(user_score):
                match counter:
                    case 3:
                        test = get_test_percentage_score(user_score)
                        print("test == ",test,"counter ==",counter)
                        counter = counter - 1
                    case 2:
                        lab = get_lab_percentage_score(user_score)                       
                        print("lab == ",lab,"counter ==",counter)
                        counter = counter - 1
                    case 1:
                        homework = get_homework_percentage_score(user_score)
                        print("homework == ",homework,"counter ==",counter)
                        counter = counter - 1                  
                    case default :
                        break
        total = test + lab + homework  
        print("total ==",total,"/100")     
           
    except ValueError as err :
        print(err)
    option = str(input('Do you want to try again!! Y or y for yes and N or n a no\n'))
    if option.upper() == "Y":
        run = True;
        print(" this is true")
        counter = 3
    elif option.upper() == "N":
        run = False;
        print(" this is false")
       
 



# def get_round_count():
#     total_rounds = 0
#     try:
#         count = int(input("how many rounds\n"))  
#         total_rounds = count      
#     except ValueError as err :
#         print(err)
#     return total_rounds
    