nimet = set()

nimi = input("Anna nimi (tyhjä lopettaa ohjelman): ")
while nimi != "":
    if nimi not in nimet:
        print("Uusi nimi annettu")
        nimet.add(nimi)
    else:
        print("Nimi annettu aikaisemmin")

    nimi = input("Anna nimi (tyhjä lopettaa ohjelman): ")

print(f"Kaikki annetut nimet: {nimet}")