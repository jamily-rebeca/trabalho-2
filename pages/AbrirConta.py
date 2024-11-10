from view import View
import streamlit as st # type: ignore

class Cadastrar:
    @staticmethod
    def main():
        st.header("Cadastrar")
        Cadastrar.cadastrar()
    @staticmethod
    def cadastrar():
    
        nome = st.text_input("Digite o nome do paciente: ")
        idade = st.number_input("Digite a idade do paciente: ")
        fone = st.text_input("Digite o telefone do paciente: ")
        cpf = st.text_input("Digite o CPF do paciente: ")
        senha = st.text_input("Digite a senha do paciente: ", type="password")
        email = st.text_input("Digite o email do paciente: ")


        if st.button("Cadastrar"):
            valido = True
            if not nome or not fone or not cpf or not idade or not senha or not email:
                st.warning("Adicione Todos Os Valores.")
            else:
                for p in View.listar_pacientes():
                    if p.get_email() == email:
                        st.warning("Esse email já é usado por outro usuário.")
                        valido = False
                        
                if valido:
                    View.inserir_paciente(nome, idade, fone, cpf, senha, email)
                    st.success("Paciente cadastrado.")