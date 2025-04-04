#Write a python program using function to convert Celsius to Fahrenheit.

# The formula for conversion is: F = C * 9/5 + 32

temperature = float(input("Enter temperature in Celsius: "))

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
celsius_to_fahrenheit(temperature)
print(f"{temperature} Celsius is equal to {celsius_to_fahrenheit(temperature)} Fahrenheit.")