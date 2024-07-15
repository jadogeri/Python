import math

from utils.utils import *

# if __name__ == "__main__":
#     print("the main prog")
# else:
#     print("not the main prog")
input_count : int = 0
while (input_count == 0):
    try:
        input_count = int(input("how many inputs?\n"));        

    except  ValueError as err :
        print(err)

while (input_count > 0 and __name__ == "__main__") :
    try:
        input_string = str(input("Enter numner?\n"));
        input_int = int(input_string);
        if ( is_valid_input(input_int) ):
            print("f(" + str(input_int) + ") = " + str(fibonacci(input_int)));
            input_count -= 1;
    except ValueError as err :
        print(err);
   
