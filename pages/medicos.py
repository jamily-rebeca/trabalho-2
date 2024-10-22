import streamlit as st
from view import View
import pandas as pd

st.set_page_config(
    page_title="Médicos",
    page_icon="👋",
)

st.title("Página 2 medicos")



tab1, tab2, tab3, tab4 = st.tabs(["Cadastrar", "Listar", "Atualizar", "Excluir"])

with tab1:
    st.title("Cadastrar")
    nome = st.text_input("Digite o nome do Médico: ")
    especificacao = st.text_input("Digite a especificação do médico")

    if st.button("Cadastrar"):
        View.inserir_medico(nome, especificacao)
        st.write("Médico cadastrado.")

with tab2:
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
