class Auto:
    def __init__(self, rekkari, huippuvauhti):
        self.rekkari = rekkari
        self.huippuvauhti = huippuvauhti
        self.nyk_vauhti = 0
        self.matka = 0

    def kiihdytä(self, vauhti):
        uusi_vauhti = self.nyk_vauhti + vauhti
        if uusi_vauhti <= 0:
            self.nyk_vauhti = 0
        elif uusi_vauhti >= self.huippuvauhti:
            self.nyk_vauhti = self.huippuvauhti
        else:
            self.nyk_vauhti += vauhti

    def kulje(self, aika):
        self.matka += self.nyk_vauhti * aika

    def _str_(self):
        return f"REKKARI: {self.rekkari}, NYK_NOPEUS: {self.nyk_vauhti} HUIPPUVAUHTI: {self.huippuvauhti}, MATKA: {self.matka}"