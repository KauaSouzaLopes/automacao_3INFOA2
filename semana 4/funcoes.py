'''
As funções permite modularizar o código , dividir ele em partes menores que podem ser reaproveitadas. Isso simplifica a codificação.

Estrutura função python

def nome_funcao(param1, param2, paramN):
    //algum codigo que a função faz
    returnn saida_da_funcao
'''
#cria uma função que calcula a área do triângulo
def calculateTriangleArea(base, altura):
        area = (base * altura) / 2
        return area

#Exemplo 1: chamar a função
area1 = calculateTriangleArea(100, 10)
print("A área do triângulo 1 é ", area1)

#Exemplo2: chamar a função
base = float(input('Digite a base: '))
altura = float(input('Digite a altura: '))
area2 = calculateTriangleArea(base, altura)
base = float("A área do triângulo 2 é ", area2)

#cria uma função que calcula a área do triângulo
def calculateTriangleArea(base, altura):
        area = (base * altura) / 2
        return area

#cria uma função que calcula a área do quadrado
def calculateSquareArea(base, altura):
        area = (base * altura) / 2
        return area