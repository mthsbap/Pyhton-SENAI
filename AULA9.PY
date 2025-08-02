# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
número = int(input("DIGITE UM NÚMERO: "))
print(número)
#2*
#Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
#base na idade.
idade = int(input("DIGITE SUA IDADE: "))
if idade <= 15 :
    print("NÃO PODE VOTAR")
else :
    print("PODE VOTAR")
#3
#Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
num = 7
if num % 2 == 0 :
    print("O NÚMERO É PAR")
else : 
    print("O NÚMERO É ÍMPAR")
# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
num_1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
num_2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
num_3 = int(input("DIGITE O TERCEIRO NÚMERO: "))

if num_1 == num_2 == num_3 :
    print("O TRIÂNGULO É EQUILÁTERO")
elif num_1 != num_2 != num_3 :
    print("O TRIÃNGULO É ESCALENO")
else :
    print("O TRIÂNGULO É ISÓSCELES")
 
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

#5*
#Determine se um número é múltiplo de 5 e 7.
print("DESCUBRA SE UM NÚMERO É MÚLTIPLO DE 5 E 7")
dig_num = int(input("DIGITE UM NÚMERO: "))
if dig_num % 5 == 0 and dig_num % 7 == 0 :
    print("O NÚMERO É MÚLTIPLO DE 5 E 7")
else :
    print("O NÚMERO NÃO É MÚLTIPLO DE 5 E 7")
# 6* 
# Verifique se um número é positivo e maior que 10
print("VERIFIQUE SE UM NÚMERO É POSITIVO E MAIOR QUE 10")
num_dig = int(input("DIGITE O NÚMERO: "))

if num_dig >= 0 and num_dig > 10 :
    print("O NÚMERO É POSITIVO E MAIOR QUE 10")
else :
    print("O NÚMERO NÃO É POSITIVO E MAIOR QUE 10")
#7*
# Verifique se um número é divisível por 3 ou 5.

print("DESCUBRA SE UM NÚMERO É DIVÍSIVEL POR 3 OU 5")
div = int(input("DIGITE O NÚMERO: "))
if div % 3 == 0 or div % 5 == 0:
    print("O NÚMERO É DIVISIVEL POR 3 OU 5")
else :
    print("O NÚMERO NÃO É DIVISIVEL POR 3 OU 5")
#-----------------------------------------------------------------------------------------
quartos = {"Simples": 100, "Duplo" : 150, "Luxo" : 250}

print(" BEM-VINDO AO SISTEMA DE CADASTRO DE CLIENTES PARA RESERVA NO HOTEL")
usuario_1 = input("DIGITE O NOME DO 1º CLIENTE: ")
idade_1 = int(input("DIGITE A IDADE DO 1º CLIENTE: "))
usuario_2 = input("DIGITE O NOME DO 2º CLIENTE: ")
idade_2 = int(input("DIGITE A IDADE DO 2º CLIENTE: "))
usuario_3 = input("DIGITE O NOME DO 3º CLIENTE: ")
idade_3 = int(input("DIGITE A IDADE DO 3º CLIENTE: "))

print("RESERVA DE QUARTOS")
escolha_1 = input(f'''
{usuario_1} ESCOLHA O TIPO DE QUARTO:
Simples - R$ 100,00 por dia.
Duplo - R$ 150,00 por dia.
Luxo - R$ 250,00 por dia.
''')
escolha_2 = input(f'''
{usuario_2} ESCOLHA O TIPO DE QUARTO:
Simples - R$ 100,00 por dia.
Duplo - R$ 150,00 por dia.
Luxo - R$ 250,00 por dia.
''')
escolha_3 = input(f'''
{usuario_3} ESCOLHA O TIPO DE QUARTO:
Simples - R$ 100,00 por dia.
Duplo - R$ 150,00 por dia.
Luxo - R$ 250,00 por dia.
''')

print("CÁLCULO DA ESTADIA DOS CLIENTES")
dias_1 = int(input(f"{usuario_1} DIGITE A SUA QUANTIDADE DE DIAS: "))
dias_2 = int(input(f"{usuario_2} DIGITE A SUA QUANTIDADE DE DIAS: "))
dias_3 = int(input(f"{usuario_3} DIGITE A SUA QUANTIDADE DE DIAS: "))
calculo_1 = quartos[escolha_1] * dias_1
calculo_2 = quartos[escolha_2] * dias_2
calculo_3 = quartos[escolha_3] * dias_3

print(f'''PAGAMENTO:
CLIENTE: {usuario_1}, IDADE: {idade_1}, QUARTO: {escolha_1}, VALOR POR DIA: R${float(quartos[escolha_1]):.2f}, DIAS: {dias_1}, PREÇO DA ESTADIA: R${float(calculo_1):.2f}
CLIENTE: {usuario_2}, IDADE: {idade_2}, QUARTO: {escolha_2}, VALOR POR DIA: R${float(quartos[escolha_2]):.2f}, DIAS: {dias_2}, PREÇO DA ESTADIA: R${float(calculo_2):.2f}
CLIENTE: {usuario_3}, IDADE: {idade_3}, QUARTO: {escolha_3}, VALOR POR DIA: R${float(quartos[escolha_3]):.2f}, DIAS: {dias_3}, PREÇO DA ESTADIA: R${float(calculo_3):.2f}
''')
