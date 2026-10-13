# Plateforme de chiffrement Streamlit (v2)

Application web pour chiffrer et déchiffrer des messages avec une clé personnelle.
La v2 prend en charge le français : accents, cédille, ligatures (œ, æ),
guillemets, apostrophes typographiques et retours à la ligne.

## Lancement local

```bash
pip install -r requirements.txt
streamlit run app.py
```

L'application s'ouvre sur `http://localhost:8501`.

## Utilisation

1. Onglet **Chiffrer** : saisir une clé (1 à 13 caractères) et le message, puis copier le résultat.
2. Onglet **Déchiffrer** : saisir **la même clé** et le texte chiffré.

Les messages chiffrés avec la v1 ne sont plus déchiffrables avec la v2
(l'alphabet et le modulo ont changé).

## Déploiement sur Streamlit Community Cloud

1. Pousser ce dépôt sur GitHub.
2. Se connecter sur [share.streamlit.io](https://share.streamlit.io) avec GitHub.
3. **Create app** → **Yup, I have an app**.
4. Choisir le dépôt, la branche `main` et le fichier `app.py`.
5. Déployer.

## Fichiers

```
├── app.py                         # Application Streamlit
├── crypto.py                      # Alphabet et algorithmes v2
├── Chiffrement_intégral.py        # Script console de chiffrement
├── Déchiffrement_intégral.py      # Script console de déchiffrement
├── Notice_chiffrement_v2.docx     # Notice utilisateur Word
├── requirements.txt
└── README.md
```
