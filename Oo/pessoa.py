class Pessoa:  # classes são tipos personalizados
    def __init__(self, *filhos, nome=None, idade=19):  # Atributo de dado
        self.idade = idade # Atributo de dado
        self.nome = nome # Atributo de dado
        self.filhos = list(filhos) # Atributo Complexo

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
    lucca.sobrenome = "Ribeiro"  # Criação Atributo dinamico
    print(lucca.sobrenome)
    del lucca.filhos
    print(lucca.__dict__)  # Visualização Atributos
    print(light.__dict__)
