import streamlit as st #type: ignore
from models.pacientes import Pacientes_CRUD
from view import View


st.title("Hello")




class Principal:
    @staticmethod
    def main():
        
        st.set_page_config(
    page_title="Visitante",
    page_icon="👋",
)
        tab1, tab2 = st.tabs(["Registro", "Login"])
        with tab1:
            Principal.cadastrar()
        with tab2:
            Principal.login()


    @staticmethod
    def cadastrar():
        st.header("Cadastrar")

        # View.CriarAdmin cria um usuário admin
        
        nome = st.text_input("Digite o nome do paciente: ")
        idade = st.number_input("Digite a idade do paciente: ")
        fone = st.text_input("Digite o telefone do paciente: ")
        cpf = st.text_input("Digite o CPF do paciente: ")
        senha = st.text_input("Digite a senha do paciente: ", type="password")
        # confirmSenha = st.text_input("Comfirme sua senha: ", type="password")
        email = st.text_input("Digite o email do paciente: ")


        if st.button("Cadastrar"):
            valido = True
            if not nome or not fone or not cpf or not idade or not senha or not email:
                st.warning("Adicione Todos Os Valores.")
            # if senha != confirmSenha:
                # st.warning("A senha de confirmação está diferente da anterior")
            else:
                for p in View.listar_pacientes():
                    if p.get_email() == email:
                        st.warning("Esse email já é usado por outro usuário.")
                        valido = False
                        
                if valido:
                    View.inserir_paciente(nome, idade, fone, cpf, senha, email)
                    st.success("Paciente cadastrado.")
                    
                    st.switch_page("pages/pacientes.py")
                    # mudar o link, está levando para a página que o admin tem acesso

    @staticmethod
    def login():
        st.header("Login")

        email = st.text_input("qual o email?")
        senha = st.text_input("qual a senha?")

        if st.button("entrar"):
            if email and senha:
                for paciente in View.listar_pacientes():
                    if paciente.get_email() == email and paciente.get_senha() == senha:
                        st.session_state["cliente_id"] = paciente.get_id_paciente()
                        st.session_state["email"] = paciente.get_email()
                        st.rerun()
                    else:
                        st.warning("senha ou email incorreto")        

            else:
                st.warning("preencha todos os blocos")    
        