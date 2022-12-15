from pojistenec import Pojistenec

seznam_pojistencu = []

maxim = Pojistenec("Maxim", "Veliký",33, 777788899)
tristan = Pojistenec("Tristan", "Dobrý",22, 777766655)

seznam_pojistencu.append(maxim)
seznam_pojistencu.append(tristan)

print("Aplikace vás vítá")
print("Vyberte z možností")

volba = input("Vaše volba")

if (volba == 1):

    jmeno = input("Zadejte jméno")
    prijmeni = input("Zadejte přijmení")
    vek = input("Zadejte vek")
    telefon = input("Zadejte telefon")
print(volba)