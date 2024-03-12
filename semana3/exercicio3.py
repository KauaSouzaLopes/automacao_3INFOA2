'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''

grupos = [[],[],[]]
while True:
    matricula = int(input('Digite a matrícula: '))
    grupos[matricula % 3] = matricula

    if matricula == 0:
        break


print("Grupo 1", grupos[0])
print("Grupo 2", grupos[1])
print("Grupo 3", grupos[2])