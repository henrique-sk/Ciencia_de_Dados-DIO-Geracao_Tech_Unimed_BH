class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # pega um método e transforma em uma propriedade
    def x(self):
        return self._x or 0

    @x.setter # função de propriedade não retorna valor
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        # ao invés de excluir de fato, o que traria um mau comportamento ao código
        # atribuir 0 deixa ele lá mas com esse valor
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
