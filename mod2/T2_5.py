lei_str = input('Syötä leivisköjen määrä: ')
nau_str = input('Syötä naulojen määrä: ')
luo_str = input('Syötä luotien määrä: ')
lei = float(lei_str)
nau = float(nau_str)
luo = float(luo_str)
lei2g = lei*20*32*13.3
nau2g = nau*32*13.3
luo2g = luo*13.3
nyky = (lei2g + nau2g + luo2g)/1000
nyky_kg = int((lei2g + nau2g + luo2g)/1000)
nyky_g = int(((float(nyky) - float(nyky_kg))*1000))
print(f'Kokonaismassa nykysuureina on {nyky_kg} kilogrammaa ja {nyky_g} grammaa.')