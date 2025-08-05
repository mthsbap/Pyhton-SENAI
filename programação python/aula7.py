#Exercício 1: Crie uma lista chamada numeros que contenha
#  os números inteiros de 1 a 10 e imprima-a na tela.
# numeros = list(range(1, 11))
# print(numeros)

# #Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.
# print(numeros[2])

# #exercicio 3: Adicione o número 9 à lista numeros e imprima a lista atualizada.
# numeros.append(9)
# print(numeros)

# #Exercício 4: Remova o número 5 da lista numeros e imprima a lista resultante.
# numeros.remove(5)
# print(numeros)

# #Exercício 5: Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.
# carros = ["Volkswagen Gol", "Fiat Uno", "Chevrolet Onix"]
# print(carros, numeros)

# #
import random
lista =  ["Pedra", "Papel", "Tesoura"]
computador = random.choice(lista)
chances = 3
jogador = input("Escolha: Pedra, Papel ou Tesoura: ")


if (computador == jogador) :
    print(computador)
    print(jogador)
    print("EMPATOU")

elif ((jogador == "Tesoura" and computador == "Pedra") or (jogador == "Pedra" and computador == "Papel") or (jogador == "Papel" and computador == "Tesoura")) :
    print(computador)
    print(jogador)
    print("PERDEU")
elif ((jogador == "Tesoura" and computador == "Papel") or (jogador == "Pedra" and computador == "Tesoura") or (jogador == "Papel" and computador == "Pedra")) :
    print(computador)
    print(jogador)
    print("GANHOU")

#
import random


# PAPEL TESOURA E PEDRA 


m_chute  = [0,1,2]
lista  =  ['Pedra','Papel', 'Tesoura']


computador =  random.choice(lista)
meu_chute =  int(input('Digite sua opção - Pedra 0, Papel 1, Tesoura 2: '))
comparacao =  computador == meu_chute
print('')
print('Minha escolha: ', lista[meu_chute])
print('Computador: ', computador)
etiquetas  = [0,1,2]


indice = lista.index(computador)


print('Escolha do ', computador)
print(f'''
{lista[meu_chute]} X {computador}
{indice == meu_chute} - Empate



{indice == 0 and meu_chute == 0} - Empate
{indice == 0 and meu_chute == 1} - Você ganhou 
{indice == 0 and meu_chute == 2} - Computador ganhou 


{indice == 1 and meu_chute == 1} - Empate 
{indice == 1 and meu_chute == 0} - Computador ganhou 
{indice == 1 and meu_chute == 2} - Você ganhou 


{indice == 2 and meu_chute == 1} - Computador ganhou 
{indice == 2 and meu_chute == 2} - Empate
{indice == 2 and meu_chute == 0} - Você ganhou 


''')
#



print('Mercado Y')
produtos = ['','Arroz', 'feijão','Carne','salgadinho']
precos = ['',10.50, 8.00,10.0,5.25]
print(f'''Produtos a venda', 
      {produtos[1]} R$ - {precos[1]}
      {produtos[2]} R$ - {precos[2]}
      {produtos[3]} R$ - {precos[3]}
      {produtos[4]} R$ - {precos[4]}
''')
carrinho = []
meu_total  = []


produto_1 = int(input('Escolha o produto pelo ID - 1 - 2 - 3 - 4'))
produto_2 = int(input('Escolha o produto pelo ID - 1 - 2 - 3 - 4'))


carrinho.append(produtos[produto_1])
carrinho.append(produtos[produto_2])


meu_total.append(precos[produto_1])
meu_total.append(precos[produto_2])


soma  =  sum(meu_total)
print('-------//------')
print(f'R$ {soma}')
print(f'''Seus produtos: 
      
      1 - {produtos[produto_1]}
      2 - {produtos[produto_2]}
      
      
      ''')

# tupla = (1,2,3,4,5,6)
# a,b,c,d,e,f = 1,2,3,4,5,6
# tupla = a,b,c,d,e,f
# print(tupla)


# estrutura de dados:
# guardar dados


nome = 'Julia'
lista = [1,2,3]
tuplas = (1,2,3)
conjuntos = {1,2,3}
dicionarios = {'keys': 'Values'}


pessoa =  {
'nome':'Paulo',
'Idade': 25,
'Endereço':'Rua r, nº 25',
'Curso':'Python 60h',
'livros': ['Harari','Taleb','X'],
'dados sensiveis':(12131,213221,4546545,'@paulo.com'),
'anos_viagem': {2022,2023,2024,2024},
'arvores genealogica':{
'Mãe':'Maria',
'Pai':'Caio',
'Filhos':2,


},
'Animais': input('Digite seu bichinho:  ')



}



print(pessoa['arvores genealogica']['Mãe'])


pessoa['veiculos'] = ['Jeep','Ferrari']


print(pessoa)









list()
tuple()
set()
dict()




# d = dict(n = 10, x = 20)
# print(d)
# lista =  [1,2,2,3,3,4,5,6,6]
# print(lista)
# conjuntos = {1,2,2,3,3,4,5,6,6}
# print(conjuntos)


# # c  =  set(range(1,12))
# # print(c)




dicionario =  {}




produto1 = input('p: ')
produto2 = input('p: ')


dicionario['Produtos'] = [produto1, produto2]
print(dicionario)
d  =  {
1:'teste',
2:'teste2',
3:'teste3',
4:'teste4'
}
