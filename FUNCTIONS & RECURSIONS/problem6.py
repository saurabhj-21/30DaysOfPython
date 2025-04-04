#Write a python function which converts inches to cms.

inches = float(input("Enter length in inches: "))

def inches_to_cms(inches):
    cms = inches * 2.54 # 1 inch = 2.54 cm
    return cms
inches_to_cms(inches)
print(f"{inches} inches is equal to {inches_to_cms(inches)} cm.")