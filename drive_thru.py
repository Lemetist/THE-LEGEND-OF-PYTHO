def get_item(num):
    menu = {
        1: "Burger",
        2: "Fries",
        3: "Soda",
        4: "Ice Cream",
        5: "Cookie"
    }
    return menu[num]

def welcome():
    print("1. Burger\n2. Fries\n3. Soda\n4. Ice Cream\n5. Cookie")
    num = int(input("What would you like to order? (Enter a number): "))
    print(f"You ordered: {get_item(num)}")

# Вызываем функцию welcome для запуска программы
welcome()
print("Thank you for visiting!")