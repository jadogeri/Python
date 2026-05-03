from constants import *

radius : int | float


# if __name__ == "__main__":
#     print("the main prog")
# else:
#     print("not the main prog")

def convert_string_to_number(value) -> int | float:
    radius = int | float 
    if value.isdigit() :
        radius = int(value)
    else:
        radius = float(value)
    return radius

def calculate_area(radius):
    
    area = radius * radius
    return area

def main():
    while True: 
        try:
            radius_string = input(ENTER_VALUE_PROMPT)
            radius = convert_string_to_number(radius_string)
            print(calculate_area(radius))
        except ValueError as err:
            print(err)
            
        option = input('Do you want to try again? Y/N: ')
        if option.upper() != "Y":
            break  


if __name__ == "__main__" :
    main()

 
