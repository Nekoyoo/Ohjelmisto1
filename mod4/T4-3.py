numerot = []
while True:
    num = input("kirjoita luku: ")

    if num == " ":
        print(f"Pienin luku {min(numerot)} ja suurin luku {max(numerot)}")
        break

    numerot.append(int(num))