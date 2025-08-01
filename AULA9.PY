
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
