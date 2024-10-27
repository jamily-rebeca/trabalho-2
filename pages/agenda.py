import streamlit as st
from view import View
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Agenda",
    page_icon="👋",
)


tab1, tab2, = st.tabs(["Criar", "Exibir"])

with tab1:
    st.title("Agenda")

    data = st.date_input("Qual o dia que desejas abrir a agenda?")
    Hinicial = st.time_input("Qual o horário inicial pra as consultas?")
    Hfinal = st.time_input("Qual horário final para as consultas?")
    intervalo = st.time_input("Qual o intervalo entre as consultas?")
    duracao = st.time_input("Qual a duração das consultas?")

    if st.button("Criar"):
        View.Agendaa(data, Hinicial, Hfinal, intervalo, duracao)

with tab2:
    st.title("Exibir agenda")

    
