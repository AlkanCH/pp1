x=5
y=2

if x==0 and y==0:
    print(f"Point P({x},{y}) is in the center of the coordinate system")
elif x==0:
    print(f"Point P({x},{y}) is on y axis")
elif y==0:
    print(f"Point P({x},{y}) is on x axis")
else:
    if x>0 and y>0:
        quadrant="first"
    elif x<0 and y>0:
        quadrant="second"
    elif x<0 and y<0:
        quadrant="third"
    elif x>0 and y<0:
        quadrant="fourth"

    print(f"Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system")