# 2. Write a Simple Python Program to Swap Two Numbers
def swap_numbers(a, b):
   
    # Swap the values
    a, b = b, a
    
    # Printing the swapped values
    print(f"Swap: First number = {a}, Second number = {b}")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
swap_numbers(num1, num2)