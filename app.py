import json
import time
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from crypto import ALPHABET_SIZE, chiffrer_message, dechiffrer_message

st.set_page_config(
    page_title="Plateforme de Chiffrement",
    page_icon="🔐",
    layout="wide",
)


def render_copy_button(button_label, text_to_copy):
    """Render a small HTML button that copies provided text to clipboard."""
    unique_id = str(time.time()).replace(".", "")
    safe_text = json.dumps(text_to_copy)
    html = (
        "<button id=\"copy-btn-" + unique_id + "\" style=\"padding:0.4rem 0.8rem; cursor:pointer;\">" + button_label + "</button>"
        + "<textarea id=\"copy-src-" + unique_id + "\" style=\"position:absolute; left:-9999px; top:-9999px;\"></textarea>"
        + "<script>\n"
        + "const btn = document.getElementById(\"copy-btn-" + unique_id + "\");\n"
        + "const ta = document.getElementById(\"copy-src-" + unique_id + "\");\n"
        + "const text = " + safe_text + ";\n"
        + "btn.addEventListener(\"click\", async () => {\n"
        + "  const prev = btn.innerText;\n"
        + "  async function fallbackCopy() {\n"
        + "    try {\n"
        + "      ta.value = text;\n"
        + "      ta.style.display = 'block';\n"
        + "      ta.select();\n"
        + "      document.execCommand('copy');\n"
        + "      ta.style.display = 'none';\n"
        + "      btn.innerText = \"Copié ✓\";\n"
        + "      setTimeout(() => btn.innerText = prev, 1500);\n"
        + "    } catch (err) {\n"
        + "      console.error(err);\n"
        + "      alert('Impossible de copier automatiquement. Sélectionnez et copiez manuellement.');\n"
        + "    }\n"
        + "  }\n"
        + "  if (navigator.clipboard && navigator.clipboard.writeText) {\n"
        + "    try {\n"
        + "      await navigator.clipboard.writeText(text);\n"
        + "      btn.innerText = \"Copié ✓\";\n"
        + "      setTimeout(() => btn.innerText = prev, 1500);\n"
        + "    } catch (e) {\n"
        + "      await fallbackCopy();\n"
        + "    }\n"
        + "  } else {\n"
        + "    await fallbackCopy();\n"
        + "  }\n"
        + "});\n"
        + "</script>"
    )
    components.html(html, height=50)


NOTICE_PATH = Path(__file__).parent / "Notice_chiffrement_v2.docx"

st.title("🔐 Plateforme de Chiffrement")

tab1, tab2, tab3 = st.tabs(["🔒 Chiffrer", "🔓 Déchiffrer", "🧭 Méthodologie"])

with tab1:
    st.header("Chiffrer un message")
    st.write("Entrez votre clé et votre message à chiffrer.")

    col1, col2 = st.columns(2)

    with col1:
        cle_chiffrement = st.text_input(
            "Clé de chiffrement",
            placeholder="Ex: CléÉté56",
            help="Clé de 1 à 13 caractères (lettres accentuées, cédille, chiffres et symboles autorisés)",
        )

    with col2:
        message_original = st.text_area(
            "Message à chiffrer",
            placeholder="Ex: Ça, c'est déjà vraiment mieux !",
            height=100,
        )

    if st.button("🔒 Chiffrer le message", type="primary"):
        if cle_chiffrement and message_original:
            try:
                message_chiffre = chiffrer_message(message_original, cle_chiffrement)
                st.success("Message chiffré avec succès !")
                st.code(message_chiffre, language="text")
                render_copy_button("📋 Copier le message chiffré", message_chiffre)
            except Exception as e:
                st.error(f"Erreur lors du chiffrement : {str(e)}")
        else:
            st.warning("Veuillez remplir tous les champs.")

with tab2:
    st.header("Déchiffrer un message")
    st.write("Entrez votre clé et votre message chiffré à déchiffrer.")

    col1, col2 = st.columns(2)

    with col1:
        cle_dechiffrement = st.text_input(
            "Clé de déchiffrement",
            placeholder="Ex: CléÉté56",
            help="Clé de 1 à 13 caractères (lettres accentuées, cédille, chiffres et symboles autorisés)",
        )

    with col2:
        message_chiffre_input = st.text_area(
            "Message chiffré",
            placeholder="Entrez votre message chiffré ici...",
            height=100,
        )

    if st.button("🔓 Déchiffrer le message", type="primary"):
        if cle_dechiffrement and message_chiffre_input:
            try:
                message_dechiffre = dechiffrer_message(message_chiffre_input, cle_dechiffrement)
                st.success("Message déchiffré avec succès !")
                st.code(message_dechiffre, language="text")
                render_copy_button("📋 Copier le message déchiffré", message_dechiffre)
            except Exception as e:
                st.error(f"Erreur lors du déchiffrement : {str(e)}")
        else:
            st.warning("Veuillez remplir tous les champs.")

with tab3:
    st.header("Méthodologie (v2)")
    st.write(
        "Cette version prend en charge le français : accents, cédille, ligatures "
        "(œ, æ), guillemets, apostrophes typographiques et retours à la ligne."
    )

    st.subheader("Principes et étapes")
    st.markdown(
        f"""
        - **Clé** : entre 1 et 13 caractères.
        - **Alphabet v2** : {ALPHABET_SIZE} caractères (lettres latines, chiffres,
          ponctuation, accents français, ç/Ç, œ/Œ, æ/Æ, « », tirets, euro, sauts de ligne).
        - **Chiffrer** :
          1. Aller dans l'onglet "🔒 Chiffrer".
          2. Saisir la clé puis le message en clair.
          3. Cliquer sur "Chiffrer le message" et copier le résultat.
        - **Déchiffrer** :
          1. Aller dans l'onglet "🔓 Déchiffrer".
          2. Saisir **la même clé** que lors du chiffrement.
          3. Coller le message chiffré, puis cliquer sur "Déchiffrer le message".
        - **Important** : un message chiffré avec la v1 ne se déchiffre plus avec la v2.
        """
    )

    if NOTICE_PATH.exists():
        st.download_button(
            label="📄 Télécharger la notice Word v2",
            data=NOTICE_PATH.read_bytes(),
            file_name=NOTICE_PATH.name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    else:
        st.info("La notice Word v2 sera disponible dans le dossier du projet.")

st.sidebar.markdown("## 📖 Instructions d'utilisation")
st.sidebar.markdown("""
1. **Clé** : 1 à 13 caractères
2. **Caractères** : français accentué, cédille, ligatures, chiffres, ponctuation
3. **Chiffrement** : message en clair + clé
4. **Déchiffrement** : message chiffré + **la même clé**
""")

st.sidebar.markdown("## ⚠️ Important")
st.sidebar.markdown("""
- Gardez votre clé secrète
- La v2 n'est pas compatible avec les messages chiffrés en v1
- Un caractère hors alphabet est refusé (il n'est plus remplacé par un espace)
""")
