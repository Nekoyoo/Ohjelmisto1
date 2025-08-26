import math
alkukorkeus = float(input('Ilmoita alkukorkeus metreinä: '))

PUTOAMISKIIHTYVYYS = 9.81
kokonaisaika = math.sqrt(2*alkukorkeus/PUTOAMISKIIHTYVYYS)

aika = 0
while aika < kokonaisaika:
    matka = 0.5 * PUTOAMISKIIHTYVYYS * aika ** 2
    print(f'pudottu matka: {matka:.2f}m')
    aika = aika + 1

print(f'kokonaisaika: {aika:.2f}s')