from luokat.auto import Auto


def main():
    auto = Auto("ABC-123", 142)
    print(f"rekisteritunnus: {auto.rekkari}, Huippunopeus: {auto.huippuvauhti} km/h, Nopeus: {auto.nyk_vauhti} km/h, ajettu matka: {auto.matka} km")

    auto.kiihdytä(30)
    auto.kiihdytä(-30)
    auto.kiihdytä(-25)
    print(auto.nyk_vauhti)


main()