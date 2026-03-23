class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        print("\nMenù principale, cosa vuoi fare?\n")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit\n")

    def loadDictionary(self, nome_file: str):
        file = open(nome_file, 'r', encoding="utf-8").read().splitlines()
        d = {}
        for riga in file:
            parti_riga = riga.split(" ")
            if d.get(parti_riga[0]) is None:
                d[parti_riga[0]] = [parti_riga[1]]
            else:
                d[parti_riga[0]].append(parti_riga[1])
        return d

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass