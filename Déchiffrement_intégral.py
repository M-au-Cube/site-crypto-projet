import time
from crypto import dechiffrer_message

Cle = input("Entrez votre clé (1 à 13 caractères, accents français autorisés).")
try:
    Final = dechiffrer_message(input("Entrez votre message à décoder."), Cle)
except ValueError as erreur:
    print(erreur)
    time.sleep(10)
else:
    print(Final)
    time.sleep(20)
