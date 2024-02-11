# 4. Write a Python Program to Check if a Number is Even or Odd
def check_even_odd(number):
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

user_number = int(input("Enter a number: "))
result = check_even_odd(user_number)
print(f"{user_number} is an {result} number.")