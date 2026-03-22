import re
import translator

class Dictionary:

    def __init__(self, nome_file: str):
        tr = translator.Translator()
        self.dizionario = tr.loadDictionary(nome_file)

    def addWord(self, p_aliena:str, p_tradotta:str):
        if (self.dizionario.get(p_aliena) is not None) and (self.dizionario.get(p_aliena) == p_tradotta):
            print("La traduzione è già presente")

        self.dizionario[p_aliena] = p_tradotta

        print(list(self.dizionario.items())[list(self.dizionario.items()).__len__()-1])
        print("Parola aggiunta!")
        with open("dictionary.txt", "a") as file:
            file.write("\n"+p_aliena+" "+p_tradotta)

    def __str__(self):
        for chiave, valore in self.dizionario.items():
            print(chiave, valore)

    def translate(self, p_aliena:str):
        if self.dizionario.get(p_aliena) is not None:
            return self.dizionario[p_aliena]
        return None

    import re

    def translateWordWildCard(self, parola_aliena: str):
        # Trasformiamo "p?re" in un pattern "p.re"
        # Il punto nelle regex indica "un carattere qualsiasi"
        pattern = parola_aliena.replace("?", ".")

        # Aggiungiamo ^ e $ per indicare inizio e fine stringa esatti
        regex = f"^{pattern}$"

        trovata = False
        for parola in self.dizionario.keys():
            if re.match(regex, parola):
                print(f"\nRisultato trovato: {parola} -> {self.dizionario[parola]}")
                trovata = True

        if not trovata:
            print("Nessuna corrispondenza trovata.")


    def get(self, parola: str):
        return self.dizionario.get(parola)