import streamlit as st # type: ignore
# from view import View
import pandas as pd # type: ignore
from models.pacientes import Pacientes_CRUD
# from main import Principal
from pages.pacientes import Pacientes
from pages.medicos import Medicos
from pages.consultas import Consultas
from pages.AbrirAgenda import AbrirAgenda
from pages.AbrirConta import Cadastrar
from pages.ListarHorarios import ListarHorarios
from pages.Login import Login

class index:
    
    @staticmethod
    def menu_entrar():
        select = st.sidebar.selectbox("Menu", ["Cadastrar", "Login"])
        if select == "Cadastrar":
            Cadastrar.main()
        if select == "Login":
            Login.main()
        
    

    @staticmethod
    def menu_admin():
        select = st.sidebar.selectbox("Menu", ["Pacientes", "Medicos", "Consultas"])
        if select == "Pacientes":
            Pacientes.main()
        if select == "Medicos":
            Medicos.main()
        if select == "Consultas":
            Consultas.main()
    @staticmethod
    def menu_paciente():
        select = st.sidebar.selectbox("Menu", ["Listar Horários", "Marcar Consulta", "Atualizar Consulta", "Excluir Consulta", "Criar Agenda"])
        if select == "Listar Horários":
            ListarHorarios.main()
        if select == "Marcar Consulta":
            Consultas.main_cadastrar()
        if select == "Atualizar Consulta":
            Consultas.main_atualizar_c()
        if select == "Excluir Consulta":
            Consultas.main_excluir()
        if select == "Criar Agenda":
            AbrirAgenda.main()
    @staticmethod
    def sair():
        if st.button("sair"):
            del st.session_state["id_paciente"]
            del st.session_state["nome"]

    @staticmethod
    def sidebar():
        if "id_paciente" not in st.session_state:
            # usuário não está logado
            index.menu_entrar()   
        else:
            # usuário está logado, verifica se é o admin
            # admin = st.session_state["cliente_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["nome"])
            # menu do usuário
            if st.session_state["nome"] == "Admin":
                index.menu_admin()
            else:
                index.menu_paciente()
            # controle de sair do sistema
            index.sair() 



