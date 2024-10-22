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


with tab4:
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
