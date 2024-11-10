import streamlit as st # type: ignore
from view import View
import pandas as pd # type: ignore



# with st.sidebar:
#     st.page_link("pages/medicos.py", label="Médicos")
#     st.page_link("pages/consultas.py", label="Consultas")
#     st.page_link("pages/pacientes.py", label="Paciente")


# st.title("Página 2 medicos")

class Medicos:
    @staticmethod
    def main():
        st.set_page_config(
    page_title="Médicos",
    page_icon="👋",
)
        tab1, tab2, tab3, tab4 = st.tabs(["Cadastrar", "Listar", "Atualizar", "Excluir"])
        with tab1:
            Medicos.cadastrar_m()
        with tab2:
            Medicos.listar_m()
        with tab3:
            Medicos.atualizar_m()
        with tab4:
            Medicos.excluir_m()
    @staticmethod
    def cadastrar_m():
        st.title("Cadastrar")
        nome = st.text_input("Digite o nome do Médico: ")
        especificacao = st.text_input("Digite a especificação do médico")

        if st.button("Cadastrar"):
            View.inserir_medico(nome, especificacao)
            st.write("Médico cadastrado.")

    @staticmethod
    def listar_m():
        st.title("Listar")

        ids: list= []
        nomes: list = []
        especificacoes: list = []

        medicos = View.listar_medicos()
        for m in medicos:
            ids.append(m.get_id_medico())
            nomes.append(m.get_nome())
            especificacoes.append(m.get_especificacao())
            

        df = pd.DataFrame(
            {
                "id": ids,
                "nome": nomes,
                "especificacao": especificacoes,
            }
        )

        st.dataframe(
            df,
            column_config={
                "id": "ID",
                "nome": "Nome",
                "especificacao": "Especificação",
            },
            hide_index=True,
        )

    @staticmethod
    def atualizar_m():
        st.title("Atualizar")

        medico = st.selectbox("Selecione o medico para atualizar", View.listar_medicos(), index=None)

        if medico is not None:
            st.write("Você selecionou:", medico.get_nome())

            nome = st.text_input("Digite o nome do medico: ", value=medico.get_nome())
            
            especificacao = st.text_input("Digite o especificação do médico: ", value=medico.get_especificacao())
            

            id_medico = medico.get_id_medico()

            if st.button("Atualizar"):
                if not nome or not especificacao:
                    st.warning("Adicione Todos Os Valores")
                else:
                    View.atualizar_medico(id_medico, nome, especificacao)
                    st.success("médico atualizado.")

    @staticmethod
    def excluir_m():
        st.title("Excluir")

        medico = st.selectbox("Selecione o medico para excluir", View.listar_medicos(), index=None)

        if medico is not None:
            st.write("Você selecionou:", medico.get_nome())

            id_medico = medico.get_id_medico()

            if st.button("Excluir"):
                if not medico:
                    st.warning("Selecione o campo.")
                View.excluir_medico(id_medico)
                st.write("Médico excluído.")
