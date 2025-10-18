vuodenaika = ("talvi", "kevät", "kesä", "syksy")
kuukausi  = int(input("Kirjoita kuukauden numero(1-12): "))

if kuukausi <= 0 or kuukausi > 12:
    print("syötö numero 1-12")
elif 2 >= kuukausi or kuukausi == 12:
    print(vuodenaika[0])
elif 3 <= kuukausi < 6:
    print(vuodenaika[1])
elif 6 <= kuukausi < 9:
    print(vuodenaika[2])
else:
    print(vuodenaika[3])