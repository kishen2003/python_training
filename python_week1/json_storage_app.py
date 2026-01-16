import json

def load_students():
    try:
        with open('python_week1/students.json','r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_students(students):
    with open('python_week1/students.json','w') as f:
        json.dump(students,f,indent=4)

def add_student(name, roll_no, marks):
    student_list = load_students()
    student_dict = {"name":name,"roll_no":roll_no,"marks":marks}
    student_list.append(student_dict)
    save_students(student_list)

def find_student(roll_no):
    student_list = load_students()
    for student in student_list:
        if student["roll_no"] == roll_no:
            return student
    return "Student not found"

if __name__ == "__main__":
    add_student("Kishen", 101, 75)
    add_student("Alex", 102, 35)

    print(load_students())
    print(find_student(101))
    print(find_student(999))


