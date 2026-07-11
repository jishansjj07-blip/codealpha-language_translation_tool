import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyperclip
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text into multiple languages using Google Translate.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

text = st.text_area("Enter Text")

source_language = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_language = st.selectbox(
    "Select Target Language",
    list(languages.keys()),
    index=1
)

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    elif source_language == target_language:
        st.warning("Source and Target languages cannot be the same.")

    else:
        try:
            translated_text = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            ).translate(text)

            st.success("Translation Successful!")

            st.subheader("Translated Text")

            st.text_area(
                "",
                translated_text,
                height=150
            )

            if st.button("📋 Copy Translation"):
                pyperclip.copy(translated_text)
                st.success("Copied to clipboard!")

            st.subheader("🔊 Listen to Translation")

            tts = gTTS(
                text=translated_text,
                lang=languages[target_language]
            )

            audio_file = "translation.mp3"
            tts.save(audio_file)

            audio = open(audio_file, "rb")
            st.audio(audio.read(), format="audio/mp3")

        except Exception as e:
            st.error(f"Error: {e}")   