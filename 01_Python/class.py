class student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa




stud1 = student("Amit ", 7)
stud2 = student("kundun", 7.5)
stud3 = student ("ranjeet" , 7)

print(f"cgpa of {stud1.name} is {stud1.cgpa}")
print(f"cgpa of {stud2.name} is {stud2.cgpa}")