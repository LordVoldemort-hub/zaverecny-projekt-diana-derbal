from evidence_pojistenych import EvidencePojistenych


# Hlavní menu programu
def hlavni_menu():
    # Vytvoření instance EvidencePojistenych pro práci s pojištěnci
    evidence = EvidencePojistenych()

    # Nekonečný cyklus pro opakované zobrazení menu, dokud uživ. nezvolí "konec"
    while True:
        # zobrazení hlav. menu
        print("\nEvidence pojištěných")
        print("---------------------------------")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3- Vyhledat pojištěného")
        print("4 - Konec")

        # Uživatelská volba
        volba = input("\nVybete si akci: \n")

        # Přidání nového pojištěného
        if volba == "1":
            # Validace jména(nesmí obsahovat čísla nebo speciální znaky)
            while True:
                jmeno = input("Zadejte jméno pojištěného: ")
                if jmeno.isalpha():  # Ověření, zda jméno obsahuje pouze písmena
                    break
                print("Jméno nesmí obsahovat čísla nebo speciální znaky. Zkuste to znovu.")

            # Validace příjmení(stejné jako u jména)
            while True:
                prijmeni = input("Zadejte příjmení: ")
                if prijmeni.isalpha():  # Ověření zda příj. obsahuje pouze písmena
                    break
                print("Příjmení nesmí obsahovat čísla nebo speciální znaky. Zkuste to znovu.")

            telefon = input("Zadejte telefonní číslo: ")

            # Validace věku(musí být kladné celé číslo)
            while True:
                try:
                    vek = int(input("Zadejte věk: "))
                    if vek > 0:  # Kontrola kladného čísla
                        break
                    else:
                        print("Věk musí být kladné číslo. Zkuste to znovu.")
                except ValueError:  # Chyba při zadání nečíselného vstupu
                    print("Věk musí být kladné číslo. Zkuste to znovu.")

            # Přidání pojištěného do evidence a zobrazení výsledku
            print(evidence.pridat_pojistence(jmeno, prijmeni, telefon, vek))

        # Výpis všech pojištěnců
        elif volba == "2":
            # Získání seznamu pojištěnců, nebo zprávy že žádní nejsou evidováni
            pojistenci = evidence.vypis_pojistence()  # pokud je návratová hodnota seznam

            for pojistenec in pojistenci:  # Výpis každého pojištěnce
                print(pojistenec)

        # Vyhledání pojištěného podle jména a příjmení
        elif volba == "3":
            # Validace jmnéna(stejné jako při přidávání)
            while True:
                jmeno = input("Zadejte jméno pojištěného: ")
                if jmeno.isalpha():
                    break
                print("Jméno nesmí obsahovat čísla nebo speciální znaky. Zkuste to znovu.")

            # Validace příjmení(stejné jako při přidávání)
            while True:
                prijmeni = input("Zadejte příjmení: ")
                if prijmeni.isalpha():
                    break
                print("Příjmení nesmí obsahovat čísla nebo speciální znaky. Zkuste to znovu.")

            # Vyhledání pojištěného v evidenci a zobrazení výsledku
            print(evidence.vyhledat_pojistence(jmeno, prijmeni))

        # Ukončení programu
        elif volba == "4":
            print("Konec programu.")
            break  # Ukončení smyčky a programu

        # Neplatná volba - opakované zobrazení menu
        else:
            print("Neplatná volba, zkuste to znovu.")


# Spuštění hlavního menu
if __name__ == "__main__":
    hlavni_menu()
