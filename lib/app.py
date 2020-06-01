class Members: 
    def __init__(self, full_name):
        self.full_name = full_name

    def intro(self):
        return(f"Hi, my name is {self.full_name}")  
    
    
class Instructor(Members):
    def __init__(self, full_name):
        super().__init__(full_name)
        self.bio = bio
        self.skills = skills

    def create_bio(self, bio):
        self.bio = bio

    def add_skills(self, skills):
        self.skills = skills
    
    

class Student(Members):
    def __init__(self, full_name):
        super().__init__(full_name)
        self.reason = reason
    def set_reason():
        self.reason = reason

class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
    
    def add_participant(self):


jane = Student('Jane Doe')
jane.intro()

vicky = Instructor("Vicky Python")
vicky.intro()

print(jane)
print(vicky)





