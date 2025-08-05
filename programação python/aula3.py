#print(2 + 4)
#print(2.2**8)
#print(True)
#print('Hello world!')

# semântico
# somar 2 valores
# num1 = 10
# num2 = 20
# print(num1  num2)

# concatenar  == juntar

#nome = 'Julia'
#cumprimento =  'Olá, Seja bem vinda'

#print(nome,cumprimento)
#print(nome+' '+cumprimento)
#print(f'{nome} {cumprimento}')
#print('{} {}'.format(nome, cumprimento))
#print('%s %s'%(nome,cumprimento))

#atividade 2

n1  =  float(input('N1: '))
n2  =  float(input('N2: '))

soma  =  n1  +  n2 

print('Resultado da Soma:', soma)

n1  =  float(input('N1: '))
n2  =  float(input('N2: '))

subtracao  = n1 -  n2

print('Resultado da Subtração', subtracao)

n1  =  float(input('N1: '))
n2  =  float(input('N2: '))

multiplicacao = n1 * n2

print('Resultado da Multiplicação:', multiplicacao)

n1  =  float(input('N1: '))
n2  =  float(input('N2: '))

divisao =  n1 / n2

print('Resultado da Divisão: ', divisao)

#media
print('Verificar se o aluno passou')
nome  =  input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
media =  (nota1 +  nota2 +  nota3)/3
print('A média do aluno', nome, 'é ',round( media))

print(f'''
        SITUAÇÃO DO ALUNO   {nome}
        APROVADO  -  {media >= 7}
        RECUPERAÇÃO  -  {media >=5 and media <7 }
        REPROVADO   - {media <5}
''')
