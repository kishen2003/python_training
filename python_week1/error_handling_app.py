class InvalidMarksError(Exception):
    pass

def calculate_average(marks):
    if not isinstance(marks,list):
        raise TypeError("Marks must be provided as a list")
    if len(marks) == 0:
        raise InvalidMarksError("Marks list cannot be empty")
    total = 0
    for x in marks:
        if (isinstance(x, int) or isinstance(x, float)) and x>=0:
            total += x
        else:
            raise InvalidMarksError("Invalid mark found")
    return total/len(marks)

def get_student_average(marks):
    try:
        avg = calculate_average(marks)
    except TypeError as e:
        return str(e)
    except InvalidMarksError as e:
        return str(e)
    else:
        return avg

if __name__ == "__main__":
    print(get_student_average([80, 90, 70]))
    print(get_student_average([]))
    print(get_student_average([80, -10, 70]))
    print(get_student_average("not a list"))
