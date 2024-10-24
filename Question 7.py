#classifying triangles

def classify_triangle(side1,side2,side3):
    if(side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):
        if side1 == side2 == side3:
            return "equilateral"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "isosceles"
        else:
            return "scalene"
    else:
        return "not a valid triangle"

    #user input the triangles sides
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

#results
result = classify_triangle(side1,side2,side3)

#print results
print(result)