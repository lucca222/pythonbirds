class Pessoa:  # classes são tipos personalizados
    def __init__(self, nome=None, idade=35):  # Atributo de dado
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):  # metodo
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Lucca')
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
