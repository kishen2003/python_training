def save_student(name, roll_no, marks):
    with open('python_week1/students.txt', 'a') as f:
        f.write(f"{name},{roll_no},{marks}\n")


def read_students():
    try:
        with open('python_week1/students.txt', 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def find_student(roll_no):
    try:
        with open('python_week1/students.txt', 'r') as f:
            for line in f:
                name, rno, marks = line.strip().split(',')
                if int(rno) == roll_no:
                    return line.strip()
            return "Student not found"
    except FileNotFoundError:
        return "Student not found"


if __name__ == "__main__":
    save_student("Kishen", 101, 75)
    save_student("Alex", 102, 35)

    print(read_students())
    print(find_student(101))
    print(find_student(999))
