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
            if is_valid_score(user_score) == True:
                match counter:
                    case 3:
                        test = get_test_percentage_score(user_score)                        
                        counter = counter - 1
                    case 2:
                        lab = get_lab_percentage_score(user_score)                 
                        counter = counter - 1
                    case 1:
                        homework = get_homework_percentage_score(user_score)
                        counter = counter - 1                  
                    case default :
                        break
        total = test + lab + homework   
        print(total)       
           
    except ValueError as err :
        print(err)
    option = str(input('Do you want to try again!! Y or y for yes and N or n a no\n'))
    if(option.upper() == 'N') :
        run = False

   
       
 


