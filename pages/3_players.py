import streamlit as st  # Importa a biblioteca Streamlit para criar a interface web
import webbrowser

st.markdown("# PLAYERS ")
btn = st.button("Voltar para HOME")
if btn:
    webbrowser.open(url="http://localhost:8501/home")

df_data = st.session_state["data"]
df_data
