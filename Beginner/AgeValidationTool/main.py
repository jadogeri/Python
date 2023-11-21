drinking_age = 21;
club_age = 18;
run = True;

if __name__ == "__main__":
    print("the main prog")
else:
    print("not the main prog")

def validateAge(age):
    if (age <= club_age):
        print("Not old enough to get into the club\n");
        return age;
    elif(age > club_age and age < drinking_age):
        print("You can come in but cant buy a drink\n");
        return age;
    else:
        print("You can come in and buy a drink\n");
        return age;

while (run) :
    age = int(input("how old are you\n"))
    validateAge(age);
    option = input('Do you want to try again!! Y or y for yes and N or n a no\n')
    if option.upper() != "Y":
        run = False;
 
