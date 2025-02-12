# Třída slouží k uchování údajů o jednotlivých pojištěncích
class Pojistenec:
    # Vytvoření podkladů pojištěného
    def __init__(self, jmeno, prijmeni, telefon, vek):
        """
       Konstruktor inicializuje atributy jméno, příjmení, telefon a věk.
        """
        self.jmeno = jmeno  # Jméno pojištěnce
        self.prijmeni = prijmeni  # Příjmení pojištěnce
        self.telefon = telefon  # Telefonní číslo pojištěnce
        self.vek = vek  # Věk pojištěnce

    def __str__(self):
        """
        Metoda pro textovou reprezentaci objektu.
        Vrací číselný řetězec obsahující informace o pojištěnci.
        """
        return f"{self.jmeno} {self.prijmeni}, {self.vek} let, tel: {self.telefon}"
