class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    # @property
    # def nome(self):
    #     return self._nome
    # se for só para retornar um atributo, seu uso não faz sentido
    # somente caso se queira fazer alguma alteração desse atributo
    #por exemplo:
    # @nome.setter
    # def nome(self, value):
    #     #... lógica para modificar o nome
    #     pass

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Henrique", 1985)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
