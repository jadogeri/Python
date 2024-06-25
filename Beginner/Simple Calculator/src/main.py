from utils import *;
input_count : int = 0;
while (input_count == 0):
    try:
        input_count = int(input("how many inputs?\n"));
    except ValueError as error:
        print(error);
is_symbol_found : bool = False;

while(input_count > 0 and __name__ == "__main__"):
    try:        
        first_num = int(input("Enter first number\n"));
        while(not is_symbol_found):
            operation = str((input("Enter operation\n")));
            if(is_valid_symbol(operation)):          
                is_symbol_found = True;  
            else:
                print(f"operation symbol {operation} is not valid, please use another operation")    
        second_num = int(input("Enter second number"));
        print(compute_values(first_num,operation,second_num));
        is_symbol_found = False;
        input_count -= 1;
    except ValueError as error:
        print(error);