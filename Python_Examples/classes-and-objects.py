class Student:
    def __init__(self, name, age, catchPhrase):
        self.name = name
        self.age = age
        self.catchPhrase = catchPhrase
    def speak(self):
        print("Hi I am " + self.name + " and I am " + str(self.age) + " years old, " + self.catchPhrase)

student = Student("Rick", 60, "Wubba lubba dub dub!")
student.speak()