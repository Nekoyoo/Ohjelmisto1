class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.floor = alin_kerros

    def liiku (self, kerros):
        while(self.kerros > kerros):
            print(self.liiku_alas())

        while(self.kerros < kerros):
            print(liiku_ylös())

    def liiku_alas(self):
        self.kerros -= 1
        return f"Kerros: {self.kerros}"

    def liiku_ylös(self):
        self.kerros += 1
        return f"Kerros: {self.kerros}"