import streamlit as st # type: ignore
from view import View
import pandas as pd # type: ignore
from models.pacientes import Pacientes_CRUD



# identificacao = View.identificar(st.session_state["email"])
# if identificacao == 1:
#     with st.sidebar:
#         st.page_link("pages/medicos.py", label="Médicos")
#         st.page_link("pages/consultas.py", label="Consultas")
#         st.page_link("pages/pacientes.py", label="Paciente")
#         st.page_link("main.py", label="Sair")
#     st.header("Cadastro de pacientes")

class Pacientes:

    
    @staticmethod
    def main():
        st.set_page_config(
    page_title="Pacientes",
    page_icon="👋",
)
        tab1, tab2, tab3, tab4 = st.tabs(["Cadastrar", "Listar", "Atualizar", "Excluir"])
        with tab1:
            Pacientes.Cadastro_p()
        with tab2:
            Pacientes.lista_p()
        with tab3:
            Pacientes.atualizar_p()
        with tab4:
            Pacientes.excluir_p()


    # isso vai ficar numa página diferente

    @staticmethod
    def Cadastro_p():
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
                    
    @staticmethod
    def lista_p():
        st.title("Listar")

        ids: list = []
        nomes: list = []
        idades: list = []
        cpfs: list = []
        telefones: list = []
        emails: list = []
        #não mostrar a senha no listar

        for p in View.listar_pacientes():
            ids.append(p.get_id_paciente())
            nomes.append(p.get_nome())
            idades.append(p.get_idade())
            cpfs.append(p.get_cpf())
            telefones.append(p.get_fone())
            emails.append(p.get_email())

        df = pd.DataFrame(
            {
                "id": ids,
                "nome": nomes,
                "idade": idades,
                "cpf": cpfs,
                "telefone": telefones,
                "email": emails,
            }
        )

        st.dataframe(
            df,
            column_config={
                "id": "ID",
                "nome": "Nome",
                "idade": "Idade",
                "cpf": "Cpf",
                "telefone": "Telefone",
                "email": "E-Mail",
            },
            hide_index=True,
        )


    @staticmethod
    def atualizar_p():
        st.title("Atualizar")

        paciente = st.selectbox("Selecione o paciente para atualizar", View.listar_pacientes(), index=None)

        if paciente is not None:
            st.write("Você selecionou:", paciente.get_nome())

            nome = st.text_input("Digite o nome do paciente: ", value=paciente.get_nome())
            fone = st.text_input("Digite o telefone do paciente: ", value=paciente.get_fone())
            cpf = st.text_input("Digite o CPF do paciente: ", value=paciente.get_cpf())
            idade = st.number_input("Digite a idade do paciente: ", value=paciente.get_idade())
            email = st.text_input("digite o email do paciente: ", value=paciente.get_email())
            id_paciente = paciente.get_id_paciente()

            if st.button("Atualizar"):
                if not nome or not fone or not cpf or not idade or not email:
                    st.warning("Adicione Todos Os Valores.")
                else:
                    View.atualizar_paciente(id_paciente, nome, idade, fone, cpf, email, paciente.get_senha())
                    st.success("Paciente atualizado.")



    @staticmethod
    def excluir_p():
        st.title("Excluir")

        paciente = st.selectbox("Selecione o paciente para excluir", View.listar_pacientes(), index=None)

        if paciente is not None:
            st.write("Você selecionou:", paciente.get_nome())

            id_paciente = paciente.get_id_paciente()

            if st.button("Excluir"):
                if not paciente:
                    st.warning("selecione um paciente.")
                else:
                    View.excluir_paciente(id_paciente)
                    st.success("Paciente excluído.")
