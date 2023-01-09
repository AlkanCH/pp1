def f(n):
    if n == 0:
        return ""
    elif n < 0:
        return ""
    else:
        sticks = "/////-" * (n // 5) + "".join(["/"] * (n % 5))
        return sticks.rstrip("-")

print(f(10))