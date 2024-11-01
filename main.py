import streamlit as st #type: ignore
from models.pacientes import Pacientes_CRUD
from view import View


st.title("Hello")


tab1, tab2 = st.tabs(["Registro", "Login"])

with tab1:
    st.header("Cadastrar")
    
    nome = st.text_input("Digite o nome do paciente: ")
    idade = st.number_input("Digite a idade do paciente: ")
    fone = st.text_input("Digite o telefone do paciente: ")
    cpf = st.text_input("Digite o CPF do paciente: ")
    senha = st.text_input("Digite a senha do paciente: ", type="password")
    email = st.text_input("Digite o email do paciente: ")


    if st.button("Cadastrar"):
        if not nome or not fone or not cpf or not idade or not senha or not email:
            st.warning("Adicione Todos Os Valores.")
        else:
            for p in Pacientes_CRUD.listar():
                if p.get_email() == email:
                    st.warning("Esse email já é usado por outro usuário.")
                else:
                    View.inserir_paciente(nome, idade, fone, cpf, senha, email)
                    st.success("Paciente cadastrado.")
                    st.switch_page("")


with tab2:
    st.header("Login")

    # nome de usuario eseha

    