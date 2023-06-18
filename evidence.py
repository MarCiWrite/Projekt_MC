from pojistenec import Pojistenec


class Evidence:
    def __init__(self):
        self.seznam = [] 
        
    def zalozit_pojistence(self):
        
        
        jmeno = input("Zadejte jméno \n")
        prijmeni = input("Zadejte příjmení \n")
        vek = input("Zadejte věk \n")
        telefon = input("Zadejte telefon \n")
        mobil = input("Zadejte mobil \n")

        
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon, mobil)
        
        self.seznam.append(novy_pojistenec)
        input("Pokračujte libovolnou klávesou .....")
    
    
    
    def vypis_pojistencu(self):
        
        for pojistenec in self.seznam:
           
            print(pojistenec)
    
    def vyhledani_pojistence(self):
        
        hledane_jmeno = input("Zadejte hledáné jméno \n")
        hledane_prijmeni = input("Zadejte hledané příjmení \n")
        for pojistenec in self.seznam:
            
            if (pojistenec.jmeno == hledane_jmeno and pojistenec.prijmeni == hledane_prijmeni):
                
                
                print(pojistenec)
                
            else:
                print("Pojištěnec neexistuje")
        
    
    def spustit(self):
        
        print("***********************************")
        print("|* Vítejte v aplikaci Pojištěnci *|")
        print("***********************************")
        
        
        print("[* Volby *]")
        print("1. Vytvoření pojištěnce")
        print("2. Vypsání pojištěnce ")
        print("3. Vyhledání pojištěnce ")
        print("4. Konec aplikace ")
        
        
        volba = input("Zadejte Vaší volbu \n")
        while volba != 4:
          
            if (volba == "1"):
                self.zalozit_pojistence()
            elif (volba == "2"):
                self.vypis_pojistencu()    
            elif (volba == "3"):
                self.vyhledani_pojistence()
            elif (volba == "4"):
                print("Děkujeme za využití")
                break
                
            volba = input("Zadejte vaší volbu \n")
                
                
            
        