from math import pi

class ShapeAreaCalculator:
    def __init__(self):
        pass

    def area_square(self, side):
        return side ** 2

    def area_rectangle(self, length, width):
        return length * width

    def area_triangle(self, height, base):
        return (height * base) / 2

    def area_circle(self, radius):
        return pi * radius ** 2


calculator = ShapeAreaCalculator()

while True:
    print("==================")
    print("Area Calculator 📐")
    print("==================")
    print("\n1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit\n")

    choice = input("Which shape: ")

    if choice == "1":
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = calculator.area_triangle(height, base)
        print(f"\nThe area is {area}\n")

    elif choice == "2":
        length = float(input("Length: "))
        width = float(input("Width: "))
        area = calculator.area_rectangle(length, width)
        print(f"\nThe area is {area}\n")

    elif choice == "3":
        side = float(input("Side: "))
        area = calculator.area_square(side)
        print(f"\nThe area is {area}\n")

    elif choice == "4":
        radius = float(input("Radius: "))
        area = calculator.area_circle(radius)
        print(f"\nThe area is {area}\n")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("please try again.\n")
