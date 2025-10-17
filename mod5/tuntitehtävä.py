loppuarvo = int(input('Anna epänegatiivinen kokonaisluku: '))
if loppuarvo <= 0:
    print('Anna epänegatiivinen lukuarvo.')
else:
    for luku in range(0, loppuarvo+1):
        if luku % 2 == 0:
            print(luku)