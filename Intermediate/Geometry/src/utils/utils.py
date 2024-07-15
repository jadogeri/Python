# @author : Joseph Adogeri
# @since  : 10-JUL-2024
# @version: 1.0


def fibonacci(num : int): 
    
    if( num == 1 ):
        return 0;
    elif( num == 2):
        return 1;
    else:
        return fibonacci( num - 1 ) + fibonacci( num - 2); 
             
    
def is_valid_input(num : int):
    if ( num <= 0 ):
        return False;
    return True;

