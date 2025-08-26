a = int(input('Anna vuosiluku: '))
if (a % 4) != 0:
    print('Vuosi ei ole karkausvuosi.')
elif (a % 4) == 0 and (a % 100) == 0 and (a % 400) != 0:
    print('Vuosi ei ole karkausvuosi.')
else:
    print('Vuosi on karkausvuosi.')