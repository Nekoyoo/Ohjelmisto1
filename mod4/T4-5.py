username = "python"
password = "rules"

tries = 0
while tries <= 5:
    input_username = input("käyttäjätunnus: ")
    input_password = input("salasana: ")
    if username == input_username and password == input_password:
        print("Tervetuloa")
        break

    print("Pääsy evätty")
    tries += 1