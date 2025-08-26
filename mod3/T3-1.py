pituus = float(input('Anna kuhan pituus senttimetreinä: '))
if pituus < 37:
    puute = 37 - pituus
    print(f'Kuha on {puute} cm verran alamittainen. Laske kuha takaisin järveen.')
else:
    print('Voit pitää kuhan.')