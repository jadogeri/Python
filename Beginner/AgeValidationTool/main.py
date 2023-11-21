drinking_age = 21;
club_age = 18;
run = True;

def validateAge(age):
    if (age <= club_age):
        print("Not old enough to get into the club\n");
    elif(age > club_age and age < drinking_age):
        print("You can come in but cant buy a drink\n");
    else:
        print("You can come in and buy a drink\n");
while (run) :
    age = int(input("how old are you\n"))
    validateAge(age);
    option = input('Do you want to try again!! Y or y for yes and N or n a no\n')
    if option.upper() != "Y":
        run = False;
 
