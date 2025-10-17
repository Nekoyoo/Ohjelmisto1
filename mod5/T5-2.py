numero = input("Kirjoita luku, tyhjä merkki lopettaa ohjelman: ")

numerolista = []

while numero != "":
    numerolista.append(int(numero))
    numero = input("Kirjoita luku: ")

numerolista.sort(reverse=True)

print(f"suurimmat luvut ovat: {numerolista[0:5]}")