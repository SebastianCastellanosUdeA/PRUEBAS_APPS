import streamlit as st
import random

st.set_page_config(page_title="Niver da Duda 💖", page_icon="🎂", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b8b;'>
    🎉 Feliz Cumpleaños Amiguinha querida 🎉
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown("### 💖 Hoy celebramos lo increíble que eres 💖")

if st.button("Haz clic para tu sorpresa 🎁"):
    frases = [
        "vc é uma fofa 🌟",
        "vamos por mais aventuras 💕",
        "Deus te abençõe ✨",
        "Vamos viajar pelo mundo 🌎💫"
    ]

    st.success(random.choice(frases))
    st.balloons()