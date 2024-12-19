meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH" : "leggera disapprovazione",
            "CREEPY" : "spaventoso, inquietante",
            "PARA" : "preoccuparsi per qualcosa, paranoiarsi"
            }
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole): ")

if parola in meme_dict.keys():
    print(parola,":",meme_dict[parola])
else:
    print("Mi dispiace, non ho trovato la parola che cercavi, prova con un'altra!")
