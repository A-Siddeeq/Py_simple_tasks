# 5. Write a Simple Python Program to Find the Minimum of Two Numbers

def find_minimum(num1, num2):

    return min(num1, num2)

first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
minimum_value = find_minimum(first_num, second_num)
print(f"The minimum value is {minimum_value}.")