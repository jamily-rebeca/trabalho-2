from view import View
from pages.index import index

def iniciar():
    if View.criarAdmin():
        View.inserir_paciente(-1, "Admin", 0, "999999999", "99999999999", "1234", "Admin@email")
    index.sidebar()

iniciar()