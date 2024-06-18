import re

class Student():
    def __init__(self, _name, _age=13, _grade="12th"):
        self._name = _name
        self._age = _age
        self._grade = _grade
    
    def __str__(self):
        return f"Student 1: {self._name}, Age: {self._age}, Grade: {self._grade}"
    
    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, new_name):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        string = isinstance(new_name, str)
        # checking format
        if not string:
            return "Onle letters are allowed"
        elif bool(re.search(r" ", new_name)):
            return "Name should not contain spaces!"
        elif regex.search(new_name):
            return "No special characters allowed"
        elif not new_name.istitle():
            return "Please capitalize only the first letter"
        elif len(new_name) < 3:
            return "New Student name must be 3 or more characters long"
        else:
            self._name = new_name
            return 0

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if type(new_age) == int:
            if new_age > 10 and new_age < 19:
                self._age = new_age
            else:
                return "Age must be between 11 and 18"
        else:
            return "Please type a number"

    @property
    def get_grade(self):
        return self._grade

    @get_grade.setter
    def set_grade(self, new_grade):
        grade = None
        th_ending = (new_grade[len(new_grade) - 2:])

        if th_ending == "th":
            grade = int(new_grade[:len(new_grade) - 2])
        else:
            checking_str = new_grade.isalpha()
            if (checking_str):
                print("Only numbers are allowed")
                return 1
            else:
                grade = int(new_grade)

        if grade > 8 and grade < 13:
            if th_ending == 'th':
                self._grade = new_grade
            else:
                print("Grade must be in the format xxth")
        else:
            print("Grade must be between 9 and 12")

    def advance(self, ):

# student = Student("Alice", 13, "12th")
# print(student)
# print(student.get_name)
# student.set_name = "Maria"
# print(student.get_age)
# student.set_age = "hi"
# print(student.get_age)
# print(student.get_grade)
# student.set_grade = "10th"
# print(student.get_grade)
