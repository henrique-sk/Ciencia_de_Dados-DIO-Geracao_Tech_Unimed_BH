class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # métodos de classe estão ligados à classe e não ao objeto
    # visto que recebem um parâmetro que aponta para a classe e não a instância do objeto
    @classmethod
    # se preciso ter acesso ao contexto da classe utilizo classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # cls é uma instância da classe
        idade = 2022 - ano
        return cls(nome, idade)

    # métodos estáticos não recebem um primeiro argumento explícito
    # é vinculado à classe e não ao objeto
    # não pode acessar ou modificar o estado da classe
    @staticmethod
    # não preciso de contexto, nem da classe nem de instância, uso staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1985, 11, 11, "Henrique")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
print(Pessoa.e_maior_idade(p.idade))
