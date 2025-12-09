from luokat.auto import Auto

auto = Auto("ABC-123", 142)

auto.kiihdytä(70)
auto.kulje(2)





print(f"""Auton rekisteritunnus: {auto.rekkari}
Auton huippunopeus: {auto.huippuvauhti} km/h
Auton tämänhetkinen nopeus: {auto.nyk_vauhti} km/h
Auton kuljettu matka: {auto.matka} km""")

auto.kiihdytä(-200)

print(f"""Auton rekisteritunnus: {auto.rekkari}
Auton huippunopeus: {auto.huippuvauhti} km/h
Auton nykyinen nopeus: {auto.nyk_vauhti} km/h
Auton kuljettu matka: {auto.matka} km""")