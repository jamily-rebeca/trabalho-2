import streamlit as st # type: ignore
from view import View
import pandas as pd # type: ignore
from models.pacientes import Pacientes_CRUD
from main import Principal
from pacientes import Pacientes
from medicos import Medicos
from consultas import Consultas

class index:
    def menu_entrar():
        select = st.sidebar.selectbox("Menu", ["Cadastrar", "Login"])
        if select == "Cadastrar":
            Principal.cadastrar()
        if select == "Login":
            Principal.login
        

    def menu_admin():
        select = st.sidebar.selectbox("Menu", ["Pacientes", "Medicos", "Consultas"])
        if select == "Pacientes":
            Pacientes.main()
        if select == "Medicos":
            Medicos.main()
        if select == "Consultas":
            Consultas.main()

    def menu_paciente():
        select = st.sidebar.selectbox("Menu", ["Consultas"])
        if select == "Consultas":
            Consultas.main()

    def sair():
        del st.session_state["email"]
        del st.session_state["senha"]


    def sidebar():
        if "email" not in st.session_state:
            # usuário não está logado
            index.menu_entrar()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["email"])
            # menu do usuário
            if st.session_state["cliente_nome"] == "admin":
                index.menu_admin()
            else:
                index.menu_paciente()
            # controle de sair do sistema
            index.sair() 



