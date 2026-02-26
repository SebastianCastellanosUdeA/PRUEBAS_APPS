import streamlit as st
import random

st.set_page_config(page_title="olá bbs", page_icon="🎂", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b8b;'>
    🎉 sdds de vocês 🎉
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown("### 💖 eu trabalhando fortemente 💖")

if st.button("Haz clic aqui 🎁"):
    frases = [
        "fofos 🌟",
        "vamos por mais aventuras 💕",
        "Deus os abençõe ✨",
        "Vamos viajar pelo mundo 🌎💫"
    ]

    st.success(random.choice(frases))
    st.balloons()