import translator as tr
from dictionary import Dictionary

t = tr.Translator()
dizionario = Dictionary("dictionary.txt")

flag = True
while(flag):

    t.printMenu()

    txtIn = input("scrivi qui la tua scelta ")
    # Add input control here!

    if int(txtIn) == 1:
        parola_e_traduzione = input("\nscrivi qui la parola aliena e la traduzione: ")
        t = parola_e_traduzione.split()
        dizionario.addWord(t[0], t[1])

    elif int(txtIn) == 2:
        parola = input("\nscrivi qui cosa vuoi cercare: ")
        if dizionario.get(parola) is not None:
            print(dizionario[parola])
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