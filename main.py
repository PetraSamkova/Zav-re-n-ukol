from pojistenec import Pojistenec
from evidencepojistenych import EvidencePojistenych

class UzivatelskeRozhrani:
    def __init__(self):
        self.evidence = EvidencePojistenych()

    def vytvor_pojisteneho(self):
        while True:
            jmeno = input("Zadejte jméno: ")
            if not jmeno.strip():
                print("Jméno nesmí být prázdné.")
                continue

            prijmeni = input("Zadejte příjmení: ")
            if not prijmeni.strip():
                print("Příjmení nesmí být prázdné.")
                continue

            vek = input("Zadejte věk: ")
            if not vek.strip():
                print("Věk nesmí být prázdný.")
                continue

            telefon = input("Zadejte telefonní číslo: ")
            if not telefon.strip():
                print("Telefonní číslo nesmí být prázdné.")
                continue

            pojisteny = Pojistenec(jmeno, prijmeni, vek, telefon)
            self.evidence.pridej_pojisteneho(pojisteny)
            print("Data byla uložena. Pokračujte ve výběru akce...")
            break

    def zobraz_menu(self):
        print("Evidence pojištěných:")
        print("1. Přidat nového pojistěného")
        print("2. Vypsat všechny pojištěné")
        print("3. Vyhledat pojištěného")
        print("4. Konec")

    def pruvodce_vytvorenim_pojisteneho(self):
        print("Pro vytvoření nového pojištěného vyplňte následující údaje:")
        self.vytvor_pojisteneho()

    def spust(self):
        while True:
            self.zobraz_menu()
            volba = input("Zvolte akci 1,2,3 a nebo 4: ")

            if volba == "1":
                self.pruvodce_vytvorenim_pojisteneho()
            elif volba == "2":
                self.evidence.zobraz_vsechny_pojistene()
            elif volba == "3":
                jmeno = input("Zadejte jméno pojištěného: ")
                prijmeni = input("Zadejte příjmení pojištěného: ")
                nalezeny = self.evidence.najdi_pojisteneho(jmeno, prijmeni)
                if nalezeny:
                    print("Pojištěný nalezen:", nalezeny)
                else:
                    print("Pojištěný nenalezen.")
            elif volba == "4":
                print("Ukončuji program.")
                break
            else:
                print("Neplatná volba. Zvolte znovu.")

uzivatelskerozhrani = UzivatelskeRozhrani()
uzivatelskerozhrani.spust()
