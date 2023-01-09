def f(d):
    cars = {}
    for entry in d:
        if entry[1] == "in":
            cars[entry[0]] = True
        elif entry[1] == "out":
            cars[entry[0]] = False
    return sorted([key for key, value in cars.items() if value])

cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))  # ["BA111","GX444","KR234"]
