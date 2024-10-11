import random

symbols =['🍒',' 🍇', '🍉', '7️⃣']

def slot_machine():
    results = (random.choices(symbols,k=3))
    print(results)
    if results[0] == results[1] == results[2]:
        print("You win!")
    else:
        print("You lose!")

while True:
    play = input("Do you want to play? (y/n): ")
    if play == 'n':
        break
    elif play == 'y':
        slot_machine()
