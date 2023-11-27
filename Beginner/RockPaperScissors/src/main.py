
import sys
import time


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
choices = file.readlines();
file.close()
print(choices)
rock, paper ,scissors = choices

drinking_age = 21;
club_age = 18;
run = True;

rounds = 0


while (rounds == 0 ) :
    rounds = get_round_count();
    time.sleep(10)
    


# if __name__ == "__main__":
#     print("the main prog")
# else:
#     print("not the main prog")

def validateAge(age):
    response = "";
    if (age < club_age):
       
        return response;
    elif(age >= club_age and age < drinking_age):

        return response;
    else:
    
        return response;

while (rounds > 0 and __name__ == "__main__") :
    try:
        age = int(input("how old are you\n"))
        validateAge(age);
    except ValueError as err :
        print(err)
    option = str(input('Do you want to try again!! Y or y for yes and N or n a no\n'))
    if option.upper() != "Y":
        run = False;
 
