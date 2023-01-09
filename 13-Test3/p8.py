class C:
    def __init__(self, students):
        self.students = students

    def m(self, n):
        students = sorted(self.students.keys())
        return ",".join(student for student in students if sum(self.students[student]) / len(self.students[student]) >= n)

s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
print(s.m(4))  # "Barbara,Peter"
print(s.m(3))  # "Barbara,Harry,Peter"
print(s.m(5))  # ""
