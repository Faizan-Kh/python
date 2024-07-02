class Person:
    def __init__(this, first_name, last_name):
        this.first_name = first_name
        this.last_name = last_name

    def display_name(this):
        print(this.first_name, this.last_name)

x = Person("Faizan", "Khan")
x.display_name()

class Student(Person):
    def student_name(this):
        print("Students Name: ", this.first_name, this.last_name)

student = Student("Fawad", "Iqbal")
student.student_name()
