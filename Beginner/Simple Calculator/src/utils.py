def is_valid_symbol(operation : str):
    is_valid : bool = False;
    operation_list : list = ["+","-","*","x","X","/","%"];
    for symbol in operation_list:
        if (symbol == operation):
            is_valid = True;
            return is_valid;   
    return is_valid;

def compute_values(first_num : int, operation : str , second_num : int):
    match operation:
        case "+":
            return first_num + second_num;
        case "-":
            return first_num - second_num;
        case "*":
            return first_num * second_num;
        case "x":
            return first_num * second_num;
        case "X":
            return first_num * second_num;
        case "/":
            return first_num / second_num;
        case "%":
            return first_num % second_num;
        case _: 
            return 0;