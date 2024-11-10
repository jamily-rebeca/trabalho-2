import streamlit as st # type: ignore
from view import View
# Precisa importar os pacientes?

class Login:

    def main():
        st.header("Login")
        Login.login()

    def login():
        email = st.text_input("qual o email?")
        senha = st.text_input("qual a senha?")

        for paciente in View.listar_pacientes():
            if paciente.get_email()==email and paciente.get_senha()==senha:
                st.session_state["id_paciente"] = paciente.get_id_paciente
                st.session_state["nome"] = paciente.get_nome()
                st.rerun()