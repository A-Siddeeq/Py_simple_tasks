# 1. Write a Python Program to Calculate the Area of a Triangle

def calculate_triangle_area(base, height):

# Formula: area = 0.5 * base * height

    area = 0.5 * base * height
    return area

base_length = float(input("Enter the base length of the triangle: "))
height_length = float(input("Enter the height of the triangle: "))
triangle_area = calculate_triangle_area(base_length, height_length)
print(f"The area of the triangle is {triangle_area:.2f} square units.")

# 2. Write a Simple Python Program to Swap Two Numbers
def swap_numbers(a, b):
   
    # Swap the values
    a, b = b, a
    
    # Printing the swapped values
    print(f"Swap: First number = {a}, Second number = {b}")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
swap_numbers(num1, num2)

# 3.Write a Python Program to Convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):

# Formula: Fahrenheit = (Celsius * 9/5) + 32

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp:.2f}°C is equivalent to {fahrenheit_temp:.2f}°F.")

# 4. Write a Python Program to Check if a Number is Even or Odd
def check_even_odd(number):
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

user_number = int(input("Enter a number: "))
result = check_even_odd(user_number)
print(f"{user_number} is an {result} number.")

# 5. Write a Simple Python Program to Find the Minimum of Two Numbers

def find_minimum(num1, num2):

    return min(num1, num2)

first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
minimum_value = find_minimum(first_num, second_num)
print(f"The minimum value is {minimum_value}.")