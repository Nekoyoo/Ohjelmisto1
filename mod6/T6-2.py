import random

def nopanheitto(sivu=21):
    return random.randint(1,sivu)

def main():
    noppa = 0
    while noppa != suurin:
        noppa = nopanheitto(suurin)
        print(noppa)

suurin = int(input("Kuinka suuren nopan haluat heittää: "))

main()