# 1. Write a Python Program to Calculate the Area of a Triangle

def calculate_triangle_area(base, height):

# Formula: area = 0.5 * base * height

    area = 0.5 * base * height
    return area

base_length = float(input("Enter the base length of the triangle: "))
height_length = float(input("Enter the height of the triangle: "))
triangle_area = calculate_triangle_area(base_length, height_length)
print(f"The area of the triangle is {triangle_area:.2f} square units.")