import random
from .auto import Auto
from tabulate import tabulate

class Kilpailu:

    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.kuluneet_tunnit = 0

    def tunti_kuluu(self):
         for auto in self.autot:
            auton_nopeus = random.randint(-10, 15)
            auto.kiihdytä(auton_nopeus)
            auto.kulje(1)

         self.kuluneet_tunnit +=1

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

    def tulosta_tilanne(self):
        print(f"tilanne {self.kuluneet_tunnit} tunnin jälkeen")
        tilannetaulukko = []
        for auto in self.autot:
            tilannetaulukko.append([auto.rekkari,
                                     f"{auto.nyk_vauhti} km/h",
                                     f"{auto.matka} km"])
        print(tabulate(tilannetaulukko, headers = ["Nimi","Nopeus","Matka"], tablefmt="grid"))


