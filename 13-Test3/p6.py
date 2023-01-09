class C:
    def __init__(self, value):
        self.value = value

    def m1(self):
        return self.value

    def m2(self):
        self.value += 1

    def m3(self):
        self.value -= 1

    def m4(self, n):
        self.value += n

c=C(5)
print(c.m1())
print(c.m2())
print(c.m1())
print(c.m4(-8))
print(c.m1())
print(c.m3())
print(c.m1())
print(c.m4(10))
print(c.m1())