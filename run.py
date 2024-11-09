from view import View
from pages.index import index

def iniciar():
    View.criarAdmin()
    index.sidebar()

iniciar()