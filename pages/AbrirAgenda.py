import streamlit as st # type: ignore
from view import View

class AbrirAgenda:
    @staticmethod
    def main():
        st.title("Agenda")
        AbrirAgenda.agenda_c()
    @staticmethod
    def agenda_c():
        

        data = st.date_input("Qual o dia que desejas abrir a agenda?")
        Hinicial = st.time_input("Qual o horário inicial pra as consultas?")
        Hfinal = st.time_input("Qual horário final para as consultas?")
        intervalo = st.time_input("Qual o intervalo entre as consultas?")
        duracao = st.time_input("Qual a duração das consultas?")

        if st.button("Criar"):
            View.Agendaa(data, Hinicial, Hfinal, intervalo, duracao)
            st.success("Agenda Criada")
            st.rerun()