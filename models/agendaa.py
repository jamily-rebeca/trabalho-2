from datetime import datetime, date, timedelta
from view import View
from consultas import Consultas_CRUD

class Agenda:
    def __init__(self, data, Hinicial, Hfinal, intervalo, duracao):
        self.set_data(data)
        self.set_inicial(Hinicial)
        self.set_final(Hfinal)
        self.set_intervalo(intervalo)
        self.set_duracao(duracao)

    def set_data(self, data:date):
        if data and date > datetime.now():
            self.data = data
        else:
            raise ValueError("informe uma data válida")
        
    def get_data(self):
        return self.data

    def set_inicial(self, Hinicial):
        if Hinicial:
            self.Hinicial = Hinicial
        else:
            raise ValueError("informe um horário válido")
        
    def get_Hinicial(self):
        return self.Hinicial

    def set_final(self, Hfinal):
        if Hfinal:
            self.Hfinal = Hfinal
        else:
            raise ValueError("informe um horário válido")
        
    def get_Hfinal(self):
        return self.Hfinal
        
    def set_intervalo(self, intervalo:timedelta):
        if intervalo:
            self.intervalo = intervalo
        else:
            raise ValueError("informe um intervalo válido")
        
    def get_intervalo(self):
        return self.intervalo
        
    def set_duracao(self, duracao:timedelta):
        if duracao:
            self.duracao = duracao
        else:
            raise ValueError("informe um duração válido")
        
    def get_duracao(self):
        return self.duracao
    
    def __str__(self):
        return f"data: {self.get_data()} -- horário inicial: {self.get_Hinicial()} -- horário final: {self.get_Hfinal()} -- intervalo: {self.get_intervalo()} -- duração: {self.get_duracao()}"
    
# esta função manipulará as informações dadas e usará  
class Criar:
    @classmethod
    def CriarAgenda(cls, data, Hinicial, Hfinal, intervalo, duracao):
        data_inicial = datetime.combine(data, Hinicial)
        data_final = datetime.combine(data, Hfinal)
        Consultas_CRUD.inserir(0, 0, "--", data_inicial)
        horario = data_inicial + intervalo + duracao


        while (horario:datetime + duracao + intervalo < data_final):
            Consultas_CRUD.inserir_consulta(0, 0, "--", horario)
            horario = horario + duracao + intervalo


    