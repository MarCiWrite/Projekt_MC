class Pojistenec: 
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} {self.vek} {self.telefon}"



maxim = Pojistenec("Maxim", "Veliký", 33, 777788899)
print(maxim)

tristan = Pojistenec("Tristan", "Dobrý", 22, 777766655)
print(tristan)