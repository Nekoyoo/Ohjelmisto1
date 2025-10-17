import random

def nopanheitto():
    return random.randint(1,6)

def main():
    noppa = 0
    while noppa != 6:
        noppa = nopanheitto()
        print(noppa)

main()