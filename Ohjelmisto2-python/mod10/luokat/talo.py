from .hissi import Hissi

class Talo():
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_määrä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def käytä_hissiä(self, hissinro, kerros):
        hissi = self.hissit[hissinro-1]
        hissi.liiku(kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.liiku(self.alin_kerros)