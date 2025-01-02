import random

processo_finito = False

while processo_finito == False:
    try:
        

        caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        num_caratteri  = int(input("Quanti caratteri vuoi che abbia la password? "))

        password = ""

        for i in range(num_caratteri):
            password += random.choice(caratteri)

        print("Ecco la tua password: ", password,".")
        processo_finito = True

    except:
        print("C'è stato un errore, nella casella di testo vanno inseriti unicamente numeri.")