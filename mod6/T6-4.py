def listan_summa(numerot):
    total = 0
    for numero in numerot:
        total += numero
    return total

def main():
    numerolista = [1,2,3,4,5,6]
    print(listan_summa(numerolista))

main()