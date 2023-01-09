class C():

    def __init__(self, array):
        self.array=array

    def __str__(self):
        return "+".join(str(x) for x in self.array) + "=" + str(sum(self.array))

print(C([6,0,15,7,-4]))