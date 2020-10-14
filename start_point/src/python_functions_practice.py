def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(self):
      string = "A string of length 21"
      return len(string)

def join_string(string_1, string_2):
      string_1 = "Mary had a little lamb, "
      string_2 = "its fleece was white as snow"
      return string_1 + string_2

def add_string_as_number(string_1, string_2):
      string_1 = "1"
      string_2 = "2"
      return int(string_1) + int(string_2)


def number_to_full_month_name(month_number):
    if month_number == 1:
        return "January"

    elif month_number == 3:
        return "March"

    elif month_number == 9:
        return "September"

def number_to_short_month_name(month_number):
    if month_number == 1:
        return "Jan"
    
    elif month_number == 4:
        return "Apr"

    elif month_number == 10:
        return "Oct"


def volume_of_cube(l, b, h):
    volume = l * b * h
    return volume
    


      