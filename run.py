from view import View
from pages.index import index

def iniciar():
    if View.criarAdmin():
        View.inserir_paciente("Admin", 0, "999999999", "99999999999", "1234", "admin")
    index.sidebar()

iniciar()