sex = input('Kerro biologinen sukupuolesi (M/F): ')
B_hb = float(input('Kerro hemoglobiiniarvosi (g/l): '))
if (sex != 'M' and sex != 'F'):
    print('Tarkista "sukupuoli".')
if B_hb < 0:
    print('Tarkista "hemoglobiiniarvo.')
if sex == 'M' and B_hb < 134:
    print('Hemoglobiiniarvosi on alhainen.')
if sex == 'M' and 134 <= B_hb <= 195:
    print('Hemoglobiiniarvosi on normaali.')
if sex == 'M' and B_hb > 195:
    print('Hemoglobiiniarvosi on korkea.')
if sex == 'F' and B_hb < 117:
    print('Hemoglobiiniarvosi on alhainen.')
if sex == 'F' and 117 <= B_hb <= 175:
    print('Hemoglobiiniarvosi on normaali.')
if sex == 'F' and B_hb > 175:
    print('Hemoglobiiniarvosi on korkea.')