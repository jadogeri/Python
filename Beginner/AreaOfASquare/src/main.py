from constants import *

radius : int | float;
run = True;



# if __name__ == "__main__":
#     print("the main prog")
# else:
#     print("not the main prog")

def convert_string_to_number(value) -> int | float:
    radius = int | float ;
    if value.isdigit() :
        radius = int(value)
    else:
        radius = float(value)
    return radius

def calculate_area(radius):
    
    area = radius * radius ;
    return area;

while (run and __name__ == "__main__") :
    try:
        radius_string : str = (input(ENTER_VALUE_PROMPT));

        radius = convert_string_to_number(radius_string);
        print(calculate_area(radius));
    except ValueError as err :
        print(err)
    option : str = input('Do you want to try again!! Y or y for yes and N or n a no\n')
    if option.upper().strip() != "Y":
        run = False;
 
