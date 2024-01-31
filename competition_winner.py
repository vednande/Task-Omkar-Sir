class Competition:
    def __init__(self, school_name, name):
        self.school_name = school_name
        self.name = name

class Student(Competition):
    def __init__(self, school_name, name, score):
        super().__init__(school_name, name)
        self.score = score

    def display(self):
        print(f"Score of {self.name} from {self.school_name} is {self.score}")


s1 = Student("Narayana Vidyalayam", "Ved Nande", 89)
print(s1.__dict__)
s1.display()

s2 = Student("Bhavan's Vidya Mandir", "Aman Rai", 95)
print(s2.__dict__)
s2.display()

if s1.score > s2.score:
    print(f"{s1.name} from {s1.school_name} is the winner")
else:
    print(f"{s2.name} from {s2.school_name} is the winner")
