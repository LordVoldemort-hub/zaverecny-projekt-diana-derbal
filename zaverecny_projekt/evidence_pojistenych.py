from pojistenec import Pojistenec


# Třída slouží k uchování a správě pojištěnců
class EvidencePojistenych:
    def __init__(self):
        self.pojistenci = []  # Seznam pro uchovávání všech pojištěnců

    def pridat_pojistence(self, jmeno, prijmeni, telefon, vek):
        """
        Přidá nového pojištěnce do evidence.

        Návratová hodnota:
        Zpráva o úsoěšném přidání pojištěnce.
        """
        pojistenec = Pojistenec(jmeno, prijmeni, telefon, vek)
        self.pojistenci.append(pojistenec)
        return "Pojištěný byl přidán."

    def vypis_pojistence(self):
        """
        Vratí seznam všech pojištěnců nebo zprávu že žádní nejsou evidování.
        """
        if not self.pojistenci:
            return "Žádní pojištění nejsou evidováni."
        else:
            return [str(pojistenec) for pojistenec in self.pojistenci]

    def vyhledat_pojistence(self, jmeno, prijmeni):
        """
        Vyhledá pojištěnce podle jména a příjmení.
        """
        nalezeno = False
        for pojistenec in self.pojistenci:
            # Porovnání jména a příjmení s údaji v evidenci
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                nalezeno = True
                return str(pojistenec)  # Vrátí nalezeného pojištěnce
        if not nalezeno:
            return "Pojištěný nebyl nalezen."  # Zpráva, pokud nebyl žádný shodný pojištěnec nalezen
