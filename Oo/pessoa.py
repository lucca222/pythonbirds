class Pessoa:  # classes são tipos personalizados
    olhos = 2  # atribudo de classe

    def __init__(self, *filhos, nome=None, idade=19):  # Atributo de dado
        self.idade = idade  # Atributo de dado
        self.nome = nome  # Atributo de dado
        self.filhos = list(filhos)  # Atributo Complexo

    def cumprimentar(self):  # metodo de instância
        return f'{id(self)}'

    @staticmethod  # não precisa de self nem cls # metodo estatico
    def metodo_estatico():
        return 42

    @classmethod  # coisas globais da classe # metodo de classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    lucca = Pessoa(idade=17, nome='Lucca')
    light = Pessoa(lucca, nome="Light")
    print(lucca.nome)
    print(lucca.idade)
    for filho in light.filhos:
        print(filho.nome)
    lucca.sobrenome = "Ribeiro"  # Criação Atributo dinamico
    print(lucca.sobrenome)
    del lucca.filhos
    print(lucca.__dict__)  # Visualização Atributos
    print(light.__dict__)
    print(Pessoa.olhos)  # atribudo de classe
    lucca.olhos = 3
    print(lucca.olhos)  # atribudo de classe
    print(light.olhos)  # atribudo de classe
    print(lucca.__dict__)  # Visualização Atributos
    print(light.__dict__)
    print(Pessoa.metodo_estatico(), light.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), light.nome_e_atributos_de_classe())
