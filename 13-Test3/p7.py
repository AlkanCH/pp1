class C:
    @staticmethod
    def m1(n):
        return "".join(c for c in str(n) if int(c) % 2 == 0)

    @staticmethod
    def m2(n):
        for i in range(len(str(n)) - 1):
            if int(str(n)[i]) > int(str(n)[i + 1]):
                return False
        return True

    @staticmethod
    def m3(n):
        return "".join(str(i) for i in range(10) if str(i) not in str(n))

print(C.m1(4231564))  # 4264
print(C.m1(79381))    # 8
print(C.m2(125579))   # True
print(C.m2(4557879))  # False
print(C.m3(23557))    # "014689"
print(C.m3(12340))    # "56789"
