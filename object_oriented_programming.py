class Student:
    def __init__(self, first_name, last_name, age, gender, marks):
        self.name = f"{first_name.title()} {last_name.title()}"
        self.age = age
        self.gender = gender
        self.marks = marks

    def information(self):
        print(f"Name: {self.name} \nAge: {self.age}\nGender: {self.gender}\nMarks: {self.marks}")


std1 = Student("Harry", "Potter", 11, "Male", 75)
std2 = Student("Hermione", "Granger", 11, "Female", 100)

std1.information()
std2.information()
