import streamlit as st
from view import View
import pandas as pd


st.set_page_config(
    page_title="Pacientes",
    page_icon="👋",
)

st.header("Cadastro de pacientes")

tab1, tab2, tab3, tab4 = st.tabs(["Cadastrar", "Listar", "Atualizar", "Excluir"])

with tab1:
    st.title("Cadastrar")
    nome = st.text_input("Digite o nome do paciente: ")
    fone = st.text_input("Digite o telefone do paciente: ")
    cpf = st.text_input("Digite o CPF do paciente: ")
    idade = st.number_input("Digite a idade do paciente: ")

    if st.button("Cadastrar"):
        View.inserir_paciente(nome, idade, fone, cpf)
        st.write("Paciente cadastrado.")

with tab2:
    st.title("Listar")

    ids: list = []
    nomes: list = []
    idades: list = []
    cpfs: list = []
    telefones: list = []

    pacientes = View.listar_pacientes()
    for p in pacientes:
        ids.append(p.get_id_paciente())
        nomes.append(p.get_nome())
        idades.append(p.get_idade())
        cpfs.append(p.get_cpf())
        telefones.append(p.get_fone())

    df = pd.DataFrame(
        {
            "id": ids,
            "nome": nomes,
            "idade": idades,
            "cpf": cpfs,
            "telefone": telefones,
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
        },
        hide_index=True,
    )

with tab3:
    st.title("Atualizar")

    paciente = st.selectbox("Selecione o paciente para atualizar", View.listar_pacientes(), index=None)

    if paciente is not None:
        st.write("Você selecionou:", paciente.get_nome())

        nome = st.text_input("Digite o nome do paciente: ", value=paciente.get_nome())
        fone = st.text_input(
            "Digite o telefone do paciente: ", value=paciente.get_fone()
        )
        cpf = st.text_input("Digite o CPF do paciente: ", value=paciente.get_cpf())
        idade = st.number_input(
            "Digite a idade do paciente: ", value=paciente.get_idade()
        )

        id_paciente = paciente.get_id_paciente()

        if st.button("Atualizar"):
            View.atualizar_paciente(id_paciente, nome, idade, fone, cpf)
            st.write("Paciente atualizado.")

with tab4:
    st.title("Excluir")

    paciente = st.selectbox("Selecione o paciente para excluir", View.listar_pacientes(), index=None)

    if paciente is not None:
        st.write("Você selecionou:", paciente.get_nome())

        id_paciente = paciente.get_id_paciente()

        if st.button("Excluir"):
            View.excluir_paciente(id_paciente)
            st.write("Paciente excluído.")
