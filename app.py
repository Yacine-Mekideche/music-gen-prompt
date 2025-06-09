import streamlit as st
from prompts.generate_prompt import generate_music_prompt
from musicgen.generate_audio import generate_music
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="🎼 MusicGen From Scratch", layout="centered")

st.title("🎵 MusicGen From Scratch")
st.markdown("Describe your musical idea to generate original music with AI.")

user_input = st.text_input("🎤 Enter your musical idea:", "")

duration = st.slider("⏱️ Select duration (seconds):", min_value=5, max_value=60, value=10, step=5)

if st.button("🎶 Generate Music") and user_input:
    with st.spinner("🧠 Generating prompt..."):
        prompt = generate_music_prompt(user_input)
        st.success("✅ Prompt generated!")
        st.markdown(f"**📝 Prompt:** _{prompt}_")

    with st.spinner("🎧 Generating your music..."):
        generate_music(prompt, duration=duration, output_path="output/musicgen_sample.wav")
        st.success("✅ Music successfully generated!")


    audio_file = "output/musicgen_sample.wav"
    if os.path.exists(audio_file):
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/wav")
    else:
        st.error("Error: audio file not found.")
