a_str = input('Syötä ensimmäinen luku: ')
b_str = input('Syötä toinen luku: ')
c_str = input('Syötä kolmas luku: ')
a = float(a_str)
b = float(b_str)
c = float(c_str)
sum = a+b+c
tulo = a*b*c
avg = (a+b+c)/3
print('Lukujen summa on ' + str(sum) + ', tulo ' + str(tulo) + ' ja keskiarvo ' + str(avg) + '.')