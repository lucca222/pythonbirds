"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado Velocidade
2) Método acelerar, que deverá incrementar a velocidade uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor de direção com valores possiveis: Norte, Sul, Leste, Oeste.
2) Metodo girar_a_direita
2) Metodo girar_a_esquerda

  N
O   L
  S

"""


class Motor:
    velocidade = 0

    @classmethod
    def acelerar(cls):
        cls.velocidade += 1
        return cls.velocidade

    @classmethod
    def frear(cls):
        if cls.velocidade == 1 or cls.velocidade == 0:
            cls.velocidade = 0
        else:
            cls.velocidade -= 2
        return cls.velocidade


class Direcão:
    valor = 'Norte'

    @classmethod
    def girar_a_direita(cls):
        direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']
        for i, d in enumerate(direcoes):
            if cls.valor == d:
                if i == 3:
                    cls.valor = direcoes[0]
                    return cls.valor
                else:
                    cls.valor = direcoes[i+1]
                    return cls.valor

    @classmethod
    def girar_a_esquerda(cls):
        direcoes = ['Norte', 'Oeste', 'Sul', 'Leste']
        for i, d in enumerate(direcoes):
            if cls.valor == d:
                if i == 3:
                    cls.valor = direcoes[0]
                    return cls.valor
                else:
                    cls.valor = direcoes[i + 1]
                    return cls.valor


class Carro(Motor, Direcão):
    pass



