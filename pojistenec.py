class Pojistenec: 
    def __init__(self, jmeno, prijmeni, vek, telefon, mobil):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
        self.mobil = mobil
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} {self.vek} {self.telefon} {self.mobil}"
