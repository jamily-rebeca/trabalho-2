import json
from datetime import datetime


class Paciente:
    def __init__(self, id_paciente, nome, aniversario, fone, cpf, senha, email):
        self.set_id_paciente(id_paciente)
        self.set_nome(nome)
        self.set_aniversario(aniversario)
        self.set_fone(fone)
        self.set_cpf(cpf)
        self.set_senha(senha)
        self.set_email(email)

    def set_id_paciente(self, id_paciente: int):
        self.id_paciente = id_paciente

    def get_id_paciente(self):
        return self.id_paciente

    def set_nome(self, nome: str):
        if nome:
            self.nome = nome
        else:
            raise ValueError("informe o nome do paciente")

    def get_nome(self):
        return self.nome

    def set_fone(self, fone: str):
        if fone:
            self.fone = fone
        else:
            raise ValueError("Adicione o telefone")

    def get_fone(self):
        return self.fone

    def set_cpf(self, cpf: str):
        if cpf:
            self.cpf = cpf
        else:
            raise ValueError("informe o cpf do paciente")

    def get_cpf(self):
        return self.cpf

    def set_aniversario(self, aniversario: datetime):
        if aniversario <= datetime.today():
            self.aniversario = aniversario

    def get_aniversario(self):
        return self.aniversario

    def set_senha(self, senha):
        if senha:
            self.senha = senha
        else:
            raise ValueError("Informe a senha que desejas utilizar")

    def get_senha(self):
        return self.senha

    def set_email(self, email):
        if email:
            self.email = email
        else:
            raise ValueError("Informe um email")

    def get_email(self):
        return self.email

    def __str__(self):
        return f"\nid: {self.get_id_paciente()} | nome: {self.get_nome()} | idade: {self.get_idade()} | cpf: {self.get_cpf()} | telefone: {self.get_fone()} | senha(achoqeundeveriapôr): {self.get_senha()} | email: {self.get_email()}"


class Pacientes_CRUD:
    objetos_pacientes: list[Paciente] = []

    @classmethod
    def abrir(cls):
        cls.objetos_pacientes = []
        try:
            with open("data/pacientes.json", mode="r") as arquivo:  # r - read
                texto = json.load(arquivo)
                for obj in texto:
                    p = Paciente(
                        obj["id_paciente"],
                        obj["nome"],
                        datetime.strptime(obj["aniversario"], "%d/%m/%Y"),
                        obj["fone"],
                        obj["cpf"],
                        obj["senha"],
                        obj["email"],
                    )
                    cls.objetos_pacientes.append(p)
        except FileNotFoundError:
            pass

    @staticmethod
    def modo(obj):
        if isinstance(obj, datetime):
            return datetime.strftime(obj, "%d/%m/%Y")
        return vars(obj)
    
    @classmethod
    def salvar(cls):
        with open("data/pacientes.json", mode="w") as arquivo:
            json.dump(cls.objetos_pacientes, arquivo, default=Pacientes_CRUD.modo)

    @classmethod
    def inserir(
        cls, obj: Paciente
    ):  # eu vou receber todos os atributos com exceção do id_cliente. Então eu crio um
        cls.abrir()  # eu poderia criar um random.radint para criar um id_cliente pouco provável  de se repetir, mas n
        x = 0
        # for email in cls.objetos_pacientes:
        #     if email in cls.objetos_pacientes:
        #         raise ValueError("informe um email válido")
        #     else:

        for p in cls.objetos_pacientes:
            if p.get_email() == obj.get_email():
                return None

        if obj.get_email() == "admin":
            obj.set_id_paciente(-1)
        else:
            for y in cls.objetos_pacientes:
                if y.id_paciente > x:
                    x = y.id_paciente
            obj.set_id_paciente(x + 1)
        cls.objetos_pacientes.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):

        cls.abrir()
        return cls.objetos_pacientes

    @classmethod
    def listar_id_paciente(cls, id_paciente):
        if id_paciente:
            cls.abrir()
            for obj in cls.objetos_pacientes:
                if id_paciente == obj.id_paciente:
                    return obj
        else:
            raise ValueError("preencher este campo")

    @classmethod
    def atualizar(
        cls, p: Paciente
    ):  # nesse objeto o cliente me fornecerá o id_cliente de usuário e os demais atributos serão para a troca
        cls.abrir()
        for x in cls.objetos_pacientes:
            if p.id_paciente == x.id_paciente:
                x.set_nome(p.get_nome())
                x.set_aniversario(p.get_aniversario())
                x.set_fone(p.get_fone())
                x.set_cpf(p.get_cpf())
                x.set_senha(p.get_senha())
                x.set_email(p.get_email())
                cls.salvar()

    @classmethod
    def identificacao(cls, i):
        cls.abrir()
        for pacientes in cls.objetos_pacientes:
            if i == -1:
                return 1
        else:
            return 0

    @classmethod
    def CriarAdmin(cls):
        criar = True
        for x in cls.objetos_pacientes:
            if x.get_email() == "Admin":
                criar = False
        return criar

    @classmethod
    def excluir(cls, id_paciente):
        if id_paciente:
            cls.abrir()
            for obj in cls.objetos_pacientes:
                if id_paciente == obj.id_paciente:
                    cls.objetos_pacientes.remove(obj)
                    cls.salvar()
