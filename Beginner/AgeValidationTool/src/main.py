from constants import *

drinking_age = 21;
club_age = 18;
run = True;



# if __name__ == "__main__":
#     print("the main prog")
# else:
#     print("not the main prog")

def validateAge(age):
    response = "";
    if (age < club_age):
        print(MINOR_AGE_PROMPT);
        response = MINOR_AGE_PROMPT
        return response;
    elif(age >= club_age and age < drinking_age):
        print(CLUB_AGE_PROMPT);
        response = CLUB_AGE_PROMPT
        return response;
    else:
        print(ADULT_AGE_PROMPT);
        response = ADULT_AGE_PROMPT
        return response;

while (run and __name__ == "__main__") :
    age = int(input("how old are you\n"))
    validateAge(age);
    option = input('Do you want to try again!! Y or y for yes and N or n a no\n')
    if option.upper() != "Y":
        run = False;
 
