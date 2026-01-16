class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_sum(self):
        total = 0
        for x in self.marks:
            total += x
        return total
    
    def calculate_average(self):
        if len(self.marks) == 0:
            return None
        total = self.calculate_sum()
        return total/len(self.marks)
    
    def is_pass(self):
        avg = self.calculate_average()
        if avg >= 40:
            return True
        return False
    
    def display_info(self):
        return f"Name: {self.name}\nRoll No: {self.roll_no}\nAverage: {self.calculate_average()}\nStatus: {"Pass" if self.is_pass() else "Fail"}\n"

if __name__ == "__main__":
    s1 = Student("Kishen", 101, [75, 80, 70])
    s2 = Student("Alex", 102, [30, 35, 40])

    print(s1.display_info())
    print(s2.display_info())
