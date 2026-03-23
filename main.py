import translator as tr
from dictionary import Dictionary

t = tr.Translator()
dizionario = Dictionary("dictionary.txt")

flag = True
while(flag):

    t.printMenu()

    txtIn = input("scrivi qui la tua scelta ")

    if int(txtIn) == 1:
        parola_e_traduzione = input("\nscrivi qui la parola aliena e la traduzione: ")
        tr = parola_e_traduzione.split()
        dizionario.addWord(tr[0], tr[1])

    elif int(txtIn) == 2:
        parola = input("\nscrivi qui cosa vuoi cercare: ")
        if dizionario.get(parola) is not None:
            print(dizionario.get(parola))
        else:
            print("la parola digitata non è presente")


    elif int(txtIn) == 3:
        parola = input("\nscrivi qui vuoi cercare con wildcard: ")
        dizionario.translateWordWildCard(parola)

    elif int(txtIn) == 4:
        print("\necco il contenuto\n")
        dizionario.__str__()

    else:
        break