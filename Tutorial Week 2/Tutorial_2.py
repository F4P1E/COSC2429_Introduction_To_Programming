import math

print(9 * 5)
print(15 / 12)
print(12 / 15)
print(15 // 12)
print(9 % 5)
print(12 % 15)
print(6 % 6)
print(2 + (3 - 1) * 10 / 5 * (2 + 3))
print(5 ** 2)
print(5 + (2 + 1) ** 2 ** 3)
print(16 / 2 * (2 + 2))

circleRadius = float(input("Enter the radius of the circle: "))
circleRadius = math.pi * circleRadius ** 2
print("The calculated area of the circle is: ", circleRadius)

recWidth = float(input("Enter the width of the rectangle: "))
recHeight = float(input("Enter the height of the rectangle: "))
recArea = recWidth * recHeight
print("The calculated area of the rectangle is: ", recArea)
