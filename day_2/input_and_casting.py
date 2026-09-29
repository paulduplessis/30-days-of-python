# If "abc" is inputted for age or years it raises a ValueError because it is of the incorrect type for the type cast

name = input("Enter your name: ")
age = int(input("Enter your age: "))
years = float(input("Enter the decimal no. of years to project forward: "))

projected_age = age + years

print("In ", years, " years, ", name, " will be ", projected_age, sep = "")