class Student():

    university="UEK Kraków"
    id = 99999

    def __init__(self, name, surname, field):
        self.name = name
        self.surname = surname
        self.field = field
        Student.id +=1

    def __str__(self):
        return f"{self.name} {self.surname} ({self.id}), {self.field}, {Student.university}"

student1 = Student("Anna", "Maj", "Applied Informatics")
print(student1)
student2 = Student("Maria", "Sokołowska", "Economy")
print(student2)
student3 = Student("Robert", "Ślusarczyk", "Math")
print(student3)