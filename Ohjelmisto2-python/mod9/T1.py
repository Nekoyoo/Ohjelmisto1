from luokat.auto import Auto

def main():
    auto = Auto("ABC-123", 142)
    print(f"rekisteritunnus: {auto.rekkari}, huippunopeus: {auto.huippuvauhti} km/h, nopeus: {auto.nyk_vauhti} km/h, ajettu matka: {auto.matka} km. ")