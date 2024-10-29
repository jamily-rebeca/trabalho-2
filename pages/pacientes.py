import streamlit as st # type: ignore
from view import View
import pandas as pd # type: ignore


st.set_page_config(
    page_title="Pacientes",
    page_icon="👋",
)
st.header("Cadastro de pacientes")

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
        if not nome or not fone or not cpf or not idade or not senha or not email:
            st.warning("Adicione Todos Os Valores.")
        else:
            View.inserir_paciente(nome, idade, fone, cpf, senha, email)
            st.success("Paciente cadastrado.")

with tab2:
    st.title("Listar")

    ids: list = []
    nomes: list = []
    idades: list = []
    cpfs: list = []
    telefones: list = []
    emails: list = []
    #não mostrar a senha no listar


    pacientes = View.listar_pacientes()
    for p in pacientes:
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
            if not nome or not fone or not cpf or not idade:
                st.warning("Adicione Todos Os Valores.")
            else:
                View.atualizar_paciente(id_paciente, nome, idade, fone, cpf)
                st.success("Paciente atualizado.")




with tab4:
    st.title("Excluir")

    medico = st.selectbox("Selecione o paciente para excluir", View.listar_pacientes(), index=None)

    if medico is not None:
        st.write("Você selecionou:", medico.get_nome())

        id_paciente = medico.get_id_paciente()

        if st.button("Excluir"):
            if not medico:
                st.warning("selecione um médico.")
            else:
                View.excluir_paciente(id_paciente)
                st.success("Paciente excluído.")
