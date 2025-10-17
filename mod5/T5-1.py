import random
noppamäärä = int(input("Anna noppien lukumäärä: "))

total = 0
for noppa in range(noppamäärä):
    total += random.randint(1, 6)

print(f"noppien summa on {total}")