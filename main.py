import streamlit as st #type: ignore

st.title("Hello")

# from datetime import datetime
# from consultas import Consultas_CRUD
# from medico import Medico_CRUD
# from view import View


# class UI:
#     @staticmethod
#     def menu_main():
#         print("1 - Pacientes\n2 - Consultas\n3 - Médicos\n4 - Sair")
#         op = int(input("\ndigite uma opção: "))
#         if op > 0 and op <= 4:
#             return op

#     @staticmethod
#     def main():
#         Pacientes_CRUD.abrir()
#         Medico_CRUD.abrir()
#         Consultas_CRUD.abrir()
#         while True:
#             op = UI.menu_main()
#             if op == 1:
#                 UI_pacientes.main_pacientes()
#             if op == 2:
#                 UI_consultas.main_consultas()
#             if op == 3:
#                 UI_medicos.main_medicos()
#             if op == 4:
#                 print("fim")
#                 break


# class UI_medicos:
#     @staticmethod
#     def menu_medicos():
#         print(
#             "\n1 - Inserir médico\n2 - Listar médicos\n3 - Listar médicos por id\n4 - Atualizar dados\n5 - Excluir médico\n6 - Sair"
#         )
#         op = int(input("\ndigite um comando: "))
#         if op > 0 and op <= 6:
#             return op
#         else:
#             raise ValueError("digite um valor válido")

#     @staticmethod
#     def main_medicos():
#         while True:
#             op = UI_medicos.menu_medicos()
#             if op == 1:
#                 UI_medicos.inserir()
#             if op == 2:
#                 UI_medicos.listar()
#             if op == 3:
#                 UI_medicos.listar_id()
#             if op == 4:
#                 UI_medicos.atualizar()
#             if op == 5:
#                 UI_medicos.excluir()
#             if op == 6:
#                 break

#     @staticmethod
#     def inserir():
#         nome = input("digite o nome do médico: ")
#         especificacao = input("digite a especificação do médico: ")
#         View.inserir_medico(nome, especificacao)

#     @staticmethod
#     def listar():
#         medicos = View.listar_medicos()
#         for x in medicos:
#             print(x)

#     @staticmethod
#     def listar_id():
#         id = int(input("Digite o ID do médico: "))
#         medico = View.listar_medicos_id(id)
#         print(medico)

#     @staticmethod
#     def atualizar():
#         id = int(input("digite o id do médico que terá seus dados modificados: "))
#         nome = input("digite o novo nome de médico: ")
#         especificacao = input("digite a nova especificação do medico: ")
#         View.atualizar_medico(id, nome, especificacao)

#     @staticmethod
#     def excluir():
#         id = int(input("Digite o ID do médico que deseja excluir: "))
#         View.excluir_medico(id)


# class UI_consultas:
#     @staticmethod
#     def menu_consultas():
#         print(
#             "\n1 - marcar consulta\n2 - listar minhas consultas\n3 - listar minhas consultas em determinada especificação\n4 - atualizar\n5 - excluir\n6 - sair"
#         )
#         op = int(input("\ndigite uma opção: "))
#         if op > 0 and op <= 6:
#             return op

#     @staticmethod
#     def main_consultas():
#         while True:
#             op = UI_consultas.menu_consultas()
#             if op == 1:
#                 UI_consultas.inserir()
#             if op == 2:
#                 UI_consultas.listar()
#             if op == 3:
#                 UI_consultas.listar_id()
#             if op == 4:
#                 UI_consultas.atualizar()
#             if op == 5:
#                 UI_consultas.excluir()
#             if op == 6:
#                 break

#     @staticmethod
#     def inserir():
#         id_paciente = int(input("digite o id do paciente: "))
#         id_medico = int(input("digite o id do médico: "))
#         especificacao = input("digite a especificação de sua consulta")
#         horario_str = input(
#             "digite a data de sua consulta no formato dd/mm/aaaa hh:mm: "
#         )
#         horario = datetime.strptime(horario_str, "%d/%m/%Y %H:%M")
#         View.inserir_consulta(id_paciente, id_medico, especificacao, horario)

#     @staticmethod
#     def listar():
#         id = int(input("Digite o ID do paciente: "))
#         consultas = View.listar_consultas(id)
#         for c in consultas:
#             print(c)

#     @staticmethod
#     def listar_id():
#         id_paciente = int(input("Digite o ID do paciente: "))
#         especificacao = input("Digite a especificação: ")
#         consultas = View.listar_consultas_especificacao(id_paciente, especificacao)
#         for c in consultas:
#             print(c)

#     @staticmethod
#     def atualizar():
#         id_consulta = int(input("digite o id da consulta: "))
#         id_paciente = int(input("digite o id do paciente: "))
#         id_medico = int(input("digite o id do médico: "))
#         especificacao = input("digite a especificação de sua consulta: ")
#         horario_str = input("digite o novo horário no formato dd/mm/aaaa hh:mm: ")
#         horario = datetime.strptime(horario_str, "%d/%m/%Y %H:%M")
#         View.atualizar_consulta(
#             id_consulta, id_paciente, id_medico, especificacao, horario
#         )

#     @staticmethod
#     def excluir():
#         id = int(input("Digite o id da consulta que deseja excluir: "))
#         View.excluir_consulta(id)


# UI.main()
