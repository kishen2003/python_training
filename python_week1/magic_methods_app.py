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

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Roll No: {self.roll_no}\n"
            f"Average Marks: {self.calculate_average()}\n"
        )

    def __repr__(self):
        return f"Student(name={self.name}, roll_no={self.roll_no}, marks={self.marks})\n"    
    
if __name__ == "__main__":
    s1 = Student("Kishen", 101, [75, 80, 70])
    s2 = Student("Alex", 102, [30, 35, 40])

    print(s1)        # calls __str__
    print(repr(s1)) # calls __repr__

    print(s2)
    print(repr(s2))
