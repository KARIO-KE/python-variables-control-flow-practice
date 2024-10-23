side1 = float(input("Enter length of the first side: "))
side2 = float(input("Enter length of the second side: "))
side3 = float(input("Enter length of the third side: "))
if side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"
print(f"The triangle is {triangle_type}.")
