import streamlit as st # type: ignore
import pandas as pd # type: ignore
from datetime import datetime
from view import View
from models.consultas import Consulta

st.set_page_config(
    page_title="Consultas",
    page_icon="👋",
)

with st.sidebar:
    st.page_link("pages/medicos.py", label="Médicos")
    st.page_link("pages/consultas.py", label="Consultas")
    st.page_link("pages/pacientes.py", label="Paciente")


st.title("Consultas")



tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cadastrar", "Listar", "Atualizar", "Excluir", "Agenda"])

with tab1:
    st.title("Cadastrar Consulta")
    id_paciente = st.text_input("Digite id do paciente: ")
    id_medico = st.text_input("Digite o id do Médico: ")
    especificacao = st.text_input("Digite a especificação do Médico: ")
    # data = st.date_input("Digite a data da consulta")
    select = st.selectbox("Selecione um horário disponível", View.listConsultas(), index=None)

    # horario = datetime.combine(data, hora)

    if st.button("Cadastrar"):
        # if select.get_idPaciente() != 0:
        #     st.warning("selecione um horário ainda não preechido")
        if not id_paciente or not id_medico or not especificacao:
            st.warning("Preencha aos campos")
        else:
            View.atualizar_consulta(select.get_idConsulta(), id_paciente, id_medico, especificacao, select.get_horario())
            st.write("Consulta cadastrada.")

with tab2:
    st.title("Listar")

    ids_consulta: list= []
    ids_pacientes: list= []
    ids_medicos: list= []
    especificacoes: list = []
    horarios: list = []

    consultas = View.listConsultas()
    for c in consultas:
        ids_consulta.append(c.get_idConsulta())
        ids_pacientes.append(c.get_idPaciente())
        ids_medicos.append(c.get_idMedico())
        especificacoes.append(c.get_especificacao())
        horarios.append(c.get_horario())
        

    df = pd.DataFrame(
        {
            "id consulta": ids_consulta,
            "id paciente": ids_pacientes,
            "id médico": ids_medicos,
            "especificação": especificacoes,
            "horários": horarios,
        
        }
    )

    st.dataframe(
        df,
        column_config={
            "id consulta": "id consulta",
            "id paciente": "id paciente",
            "id médico": "id médico",
            "especificacao": "Especificação",
            "horários": "horários",
        },
        hide_index=True,
    )

with tab3:
    st.title("Atualizar")

    consulta = st.selectbox("Selecione uma consulta para atualizar", View.listConsultas(), index=None)

    if consulta is not None:
        st.write("Você selecionou a consulta com o id:", consulta.get_idConsulta())

        id_paciente = st.text_input("Digite o id do paciente: ", value=consulta.get_idPaciente())
        id_medico = st.text_input("Digite o id do medico: ", value=consulta.get_idMedico())
        especificacao = st.text_input("Digite o especificação do médico: ", value=consulta.get_especificacao())
        dia = st.date_input("qual dia?")
        hora = st.time_input("Qual o horário?")
        horario = datetime.combine(dia, hora)

        if st.button("Atualizar"):
            if not id_paciente or not id_medico or not especificacao or not dia or not hora:
                st.warning("Adicione Todos Os Valores")
            else:
                View.atualizar_consulta(consulta.get_idConsulta(), id_paciente, id_medico, especificacao, horario)
                st.success("consulta atualizado.")


with tab4:
    st.title("Excluir")

    consulta = st.selectbox("Selecione a consulta para excluir", View.listConsultas(), index=None)

    if consulta is not None:
        st.write("Você selecionou:", consulta.get_idConsulta())

        id_consulta = consulta.get_idConsulta()

        if st.button("Excluir"):
            if not consulta:
                st.warning("Selecione o campo.")
            View.excluir_medico(id_consulta)
            st.write("consulta excluída.")


with tab5:

    st.title("Agenda")

    data = st.date_input("Qual o dia que desejas abrir a agenda?")
    Hinicial = st.time_input("Qual o horário inicial pra as consultas?")
    Hfinal = st.time_input("Qual horário final para as consultas?")
    intervalo = st.time_input("Qual o intervalo entre as consultas?")
    duracao = st.time_input("Qual a duração das consultas?")

    if st.button("Criar"):
        View.Agendaa(data, Hinicial, Hfinal, intervalo, duracao)
