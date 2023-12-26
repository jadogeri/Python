def is_valid_score(value):
    if(value >= 0 and value <= 100):
        return True
    else:
        return False

def get_test_percentage_score(value):
    return 0.4 * value

def get_lab_percentage_score(value):
    return 0.1 * value


def get_homework_percentage_score(value):
    return 0.5 * value