# @author : Joseph Adogeri
# @since  : 10-JUL-2024
# @version: 1.0


def factorial(num : int): 
    
    if( num == 1 or num == 0 ):
        return 1;
    else:
        return num * factorial( num - 1 ); 
             
    
      
