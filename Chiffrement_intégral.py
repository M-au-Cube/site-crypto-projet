import time
from crypto import chiffrer_message

Cle = input("Entrez votre clé (1 à 13 caractères, accents français autorisés).")
try:
    Final = chiffrer_message(input("Entrez votre message à coder."), Cle)
except ValueError as erreur:
    print(erreur)
    time.sleep(10)
else:
    print(Final)
    time.sleep(20)
