# id_servico:int, descrição:str, valor:float, duração:int
import json


class Medico:
    def __init__(self, id_medico, nome, especificacao):
        self.set_id_medico(id_medico)
        self.set_nome(nome)
        self.set_especificacao(especificacao)

    def set_id_medico(self, id_medico: int):
        self.id_medico = id_medico

    def get_id_medico(self):
        return self.id_medico

    def set_especificacao(self, especificacao: str):
        if especificacao:
            self.especificacao = especificacao
        else:
            raise ValueError("determine uma especificação")

    def get_especificacao(self):
        return self.especificacao

    def set_nome(self, nome: str):
        if nome:
            self.nome = nome
        else:
            raise ValueError("informe o nome do médico")

    def get_nome(self):
        return self.nome

    def __str__(self):
        return (
            f"\nid: {self.get_id_medico()} | nome: {self.get_nome()} | especificação: {self.get_especificacao()}"
        )


class Medico_CRUD:
    objetos_medicos: list[Medico] = []

    @classmethod
    def abrir(cls):
        cls.objetos_medicos = []
        try:
            with open("medicos.json", mode="r") as arquivo:  # r - read
                texto = json.load(arquivo)
                for obj in texto:
                    m = Medico(obj["id_medico"], obj["nome"], obj["especificacao"])
                    cls.objetos_medicos.append(m)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("medicos.json", mode="w") as arquivo:
            json.dump(cls.objetos_medicos, arquivo, default=vars)

    @classmethod
    def inserir(
        cls, obj: Medico
    ):  # eu vou receber todos os atributos com exceção do id_servico. Então eu crio um
        cls.abrir()  # eu poderia criar um random.radint para criar um id_servico pouco provável  de se repetir, mas n
        x = 0
        for y in cls.objetos_medicos:
            if y.id_medico > x:
                x = y.id_medico
        obj.id_medico = x + 1
        cls.objetos_medicos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos_medicos

    @classmethod
    def listar_id_medico(cls, id_medico):
        if id_medico:
            cls.abrir()
            for obj in cls.objetos_medicos:
                if id_medico == obj.id_medico:
                    return obj
        else:
            raise ValueError("preencher este campo")

    # id_medico:int, descrição:str, valor:float, duração:int

    @classmethod
    def atualizar(
        cls, m: Medico
    ):  # nesse objeto o cliente me fornecerá o id_medico de usuário e os demais atributos serão para a troca
        cls.abrir()
        for x in cls.objetos_medicos:
            if m.id_medico == x.id_medico:
                x.set_nome(m.get_nome())
                x.set_especificacao(m.get_especificacao())
                cls.salvar()

    @classmethod
    def excluir(cls, id_medico):
        if id_medico:
            cls.abrir()
            for obj in cls.objetos_medicos:
                if id_medico == obj.id_medico:
                    cls.objetos_medicos.remove(obj)
                    cls.salvar()
