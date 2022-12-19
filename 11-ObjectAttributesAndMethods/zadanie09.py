import random

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def a(number, value):
        list=[]
        for i in range(number):
            list.append(value)
        print(list)
        return list

    @staticmethod
    def b(number, value_from, value_to):
        list=[]
        for i in range(number):
            list.append(random.randint(value_from,value_to))
        print(list)
        return list


Arrays.a(6,4)
Arrays.b(6,9,27)