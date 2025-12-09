import random
from luokat.auto import Auto

def main():
    autot = []
    for i in range(10):
        huippuvauhti = random.randint(100, 200)
        autot.append(Auto(f"ABC-{i+1}", huippuvauhti))

    kokonaismatka = 0
    while kokonaismatka <= 10000:
        for auto in autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
            if auto.matka >= 10000:
                kokonaismatka = auto.matka
                print("voittaja: ", auto)

main()