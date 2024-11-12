import streamlit as st # type: ignore
import pandas as pd # type: ignore
from view import View



class ListarHorarios:
    @staticmethod
    def main():
        st.header("Listar")
        print(st.session_state)
        ListarHorarios.listar_c()
    @staticmethod
    def listar_c():
        # id_paciente = st.session_state.id_paciente #isso funciona? Ou tem que se st.session_state["id_paciente"]
        # nome_paciente = st.session_state.nome 
        # # ids_consulta: list= [] não precisa disso
        # # ids_pacientes: list= [] descobrir qual é o nome do médico

        # ids_medicos: list= []
        # especificacoes: list = []
        # horarios: list = []
        # nome_medico: list = []

        

        # consultas = View.listar_consultas(id_paciente)
        # for c in consultas:
        #     # ids_consulta.append(c.get_idConsulta())
        #     # ids_pacientes.append(c.get_idPaciente())
        #     ids_medicos.append(c.get_idMedico())
        #     especificacoes.append(c.get_especificacao())
        #     horarios.append(c.get_horario())
        # for id_medico in ids_medicos:
        #     for medico in View.listar_medicos():
        #         if id_medico == medico.get_id_medico():
        #             nome_medico.append(medico.get_nome())


        # df = pd.DataFrame(
        #     {
        #         "nome paciente": nome_paciente,
        #         "nome médico": nome_medico,
        #         "especificação": especificacoes,
        #         "horários": horarios,
            
        #     }
        # )

        # st.dataframe(
        #     df,
        #     column_config={
        #         "Nome Paciente": "Paciente",
        #         "Nome Médico": "Médico",
        #         "especificacao": "Especificação",
        #         "horários": "Horário",
        #     },
        #     hide_index=True,
        # )
        st.title("Listar")

        ids_consulta = []
        ids_pacientes = []
        ids_medicos = []
        especificacoes = []
        horarios = []

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



    @staticmethod
    def listar_minhas_c(id_paciente):
        st.subheader("Listar Minhas Consultas")
        ids_consulta = []
        ids_pacientes = []
        ids_medicos = []
        especificacoes = []
        horarios = []
        MinhasConsultas = View.listar_consultas(id_paciente)
        for c in MinhasConsultas:
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