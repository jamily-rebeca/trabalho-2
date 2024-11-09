import streamlit as st # type: ignore
from view import View
import pandas as pd # type: ignore
from models.pacientes import Pacientes_CRUD

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

identificacao = View.identificar(st.session_state["email"])
if identificacao == 1:
    with st.sidebar:
        st.page_link("pages/medicos.py", label="Médicos")
        st.page_link("pages/consultas.py", label="Consultas")
        st.page_link("pages/pacientes.py", label="Paciente")
        st.page_link("main.py", label="Sair")

    tab1, tab2, tab3, tab4 = st.tabs(["Cadastrar", "Listar", "Atualizar", "Excluir"])

    # isso vai ficar numa página diferente

    with tab1:
        st.title("Cadastrar")
        nome = st.text_input("Digite o nome do paciente: ")
        idade = st.number_input("Digite a idade do paciente: ")
        fone = st.text_input("Digite o telefone do paciente: ")
        cpf = st.text_input("Digite o CPF do paciente: ")
        senha = st.text_input("Digite a senha do paciente: ")
        email = st.text_input("Digite o email do paciente: ")


        if st.button("Cadastrar"):
            valido = True
            if not nome or not fone or not cpf or not idade or not senha or not email:
                st.warning("Adicione Todos Os Valores.")
            else:
                for p in View.listar_pacientes():
                    if p.get_email() == email:
                        st.warning("Adicione outro email")
                        valido = False
                if valido:
                    View.inserir_paciente(nome, idade, fone, cpf, senha, email)
                    st.success("Paciente cadastrado.")
                    