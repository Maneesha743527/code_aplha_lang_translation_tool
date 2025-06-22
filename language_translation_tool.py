import streamlit as st
from googletrans import Translator

st.title("🌐 Language Translation Tool")

translator = Translator()

text = st.text_area("Enter the text to translate:")
source_lang = st.text_input("Source Language (e.g., 'en' for English):")
target_lang = st.text_input("Target Language (e.g., 'fr' for French):")

if st.button("Translate"):
    if text and source_lang and target_lang:
        try:
            translated = translator.translate(text, src=source_lang, dest=target_lang)
            st.success(f"Translated Text: {translated.text}")
        except Exception as e:
            st.error(f"Translation Failed: {str(e)}")

# Optional usability feature
if st.button("Clear"):
    st.experimental_rerun()
