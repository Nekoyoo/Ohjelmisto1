import random

random_numero = random.randint(1, 10)

while True:
    guess = int(input("Arvaa numero 1-10: "))

    if guess == random_numero:
        print("Oikein")
        break
    elif guess > random_numero:
        print("Liian suuri arvaus")
    else:
        print("liian pieni arvaus")