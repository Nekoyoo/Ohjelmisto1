alkuluku = False
numero = int(input("anna kokonaisluku: "))

while numero == 1:
    print("anna luku korkeampi kuin 1")
    numero = int(input("anna kokonaisluku: "))

for num in range(2, numero):
    if numero % num == 0:
        alkuluku = False
        break
    else:
        alkuluku = True


print(alkuluku)