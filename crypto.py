"""Chiffrement / déchiffrement par substitution cyclique (v2).

L'alphabet conserve l'ordre des 95 caractères de la v1, puis ajoute
les lettres accentuées françaises, la cédille, les ligatures et la
ponctuation typographique. Le modulo utilise désormais la taille
complète de cet alphabet : les messages chiffrés en v1 ne sont plus
compatibles.
"""

# Ordre v1 (indices 0-94), conservé tel quel.
_ALPHABET_V1 = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    " .,!?;:'\"()[]{}-_=+/\\|@#$%&*^~`<>"
)

# Lettres françaises (minuscules puis majuscules) et signes usuels manquants.
_ALPHABET_FR = (
    "àâäéèêëïîôöùûüÿçœæ"
    "ÀÂÄÉÈÊËÏÎÔÖÙÛÜŸÇŒÆ"
    "«»‘’“”…—–€°"
    "\n\t\u00a0"
)

ALPHABET = _ALPHABET_V1 + _ALPHABET_FR
ALPHABET_SIZE = len(ALPHABET)
MAX_KEY_LENGTH = 13

_CHAR_TO_INDEX = {char: index for index, char in enumerate(ALPHABET)}


def _unsupported_characters(text):
    return sorted({char for char in text if char not in _CHAR_TO_INDEX})


def Codage_lettres(text):
    """Convertit une chaîne en liste d'indices dans l'alphabet v2."""
    unknown = _unsupported_characters(text)
    if unknown:
        readable = ", ".join(repr(char) for char in unknown)
        raise ValueError(
            "Caractère(s) non supporté(s) : " + readable
            + ". Utilisez uniquement l'alphabet français v2 (lettres, accents, "
            "cédille, ligatures œ/æ, chiffres, ponctuation, retours à la ligne)."
        )
    return [_CHAR_TO_INDEX[char] for char in text]


def Decodage_lettres(indices):
    """Convertit une liste d'indices en chaîne."""
    result = []
    for value in indices:
        if 0 <= value < ALPHABET_SIZE:
            result.append(ALPHABET[value])
        else:
            result.append(" ")
    return "".join(result)


def _validate_key(cle):
    if not cle or len(cle) > MAX_KEY_LENGTH:
        raise ValueError("La clé doit contenir entre 1 et 13 caractères")
    return Codage_lettres(cle)


def chiffrer_message(message, cle):
    """Chiffre un message avec une clé (soustraction cyclique)."""
    cle_coded = _validate_key(cle)
    phrase = Codage_lettres(message)
    key_len = len(cle_coded)
    for i in range(len(phrase)):
        phrase[i] = (phrase[i] - cle_coded[i % key_len]) % ALPHABET_SIZE
    return Decodage_lettres(phrase)


def dechiffrer_message(message_chiffre, cle):
    """Déchiffre un message avec une clé (addition cyclique)."""
    cle_coded = _validate_key(cle)
    phrase = Codage_lettres(message_chiffre)
    key_len = len(cle_coded)
    for i in range(len(phrase)):
        phrase[i] = (phrase[i] + cle_coded[i % key_len]) % ALPHABET_SIZE
    return Decodage_lettres(phrase)
