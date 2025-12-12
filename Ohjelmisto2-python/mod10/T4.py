from luokat.kilpailu import Kilpailu
from luokat.auto import Auto
import random




autot = []
for i in range(1, 11):
    huippunopeus =  random.randint(100, 200)
    autot.append(Auto("ABC-"+ str(i), huippuvauhti))


kilpailu = Kilpailu("Suuri romuralli",8000, autot)


while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    if kilpailu.kuluneet_tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
print("kilpailu päättynyt")