def gallonat_litroiksi(gallona):
    return gallona * 3.785

def main():
    gallona = float(input("Anna bensiinimäärä gallonoina: "))
    while gallona > 0:
        print(gallonat_litroiksi(gallona))
        gallona = float(input("Anna bensiinimäärä gallonoina: "))

main()