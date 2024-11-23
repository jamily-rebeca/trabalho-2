from view import View
from pages.index import index
from datetime import datetime

def iniciar():
    if View.criarAdmin():
        View.inserir_paciente("Admin", datetime(1, 1, 1), "999999999", "99999999999", "1234", "admin")
    index.sidebar()

iniciar()