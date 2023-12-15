from utils.utils import *

# if __name__ == "__main__":
#     print("the main prog")
# else:
#     print("not the main prog")

result = False

run = True

while (run and __name__ == "__main__") :
    try:
        value = int(input("Enter integer number\n"))
        result = is_odd(value);
        if  (result) :  
            print("true")
        else : 
            print("false")
    except ValueError as err :
        print(err)
    option = str(input('Do you want to try again!! Y or y for yes and N or n a no\n'))
    if(option.upper() == 'N') :
        run = False
  
      
