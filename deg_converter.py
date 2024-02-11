# 3.Write a Python Program to Convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):

# Formula: Fahrenheit = (Celsius * 9/5) + 32

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp:.2f}°C is equivalent to {fahrenheit_temp:.2f}°F.")