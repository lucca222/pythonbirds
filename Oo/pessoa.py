class Pessoa:  # classes são tipos personalizados
    def __init__(self, *filhos, nome=None, idade=19):  # Atributo de dado
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):  # metodo
        return f'{id(self)}'


if __name__ == '__main__':
    lucca = Pessoa(idade=17, nome='Lucca')
    light = Pessoa(lucca, nome="Light")
    print(Pessoa.cumprimentar(lucca))
    print(lucca.cumprimentar())
    print(lucca.nome)
    print(lucca.idade)
    for filho in light.filhos:
        print(filho.nome)
