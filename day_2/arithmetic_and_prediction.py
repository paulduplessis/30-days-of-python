import math

# 3.5
print(7/2)

# 3
print(7//2)

# 2
print(-7 % 3)

# False
print(0.1 + 0.2 == 0.3)

# -9 --> Different to flooring for //, floors to 0
print(int(-9.81))

# False
print(bool(''))

# Evaluates true as 1 so 1 + 1 = 2
print(True + True)

radius = float(input("Enter a radius: "))
area = math.pi * radius ** 2
print(area)