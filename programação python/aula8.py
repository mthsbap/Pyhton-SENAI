#Crie um e-commerce com a estrutura de dicionários.
#Produtos:  Livros, tablets e fones de ouvido
#As ações: 
#Comprar()
#Pagar()
#mostra o valor da compra



# produtos = {"Livros" : 59.99 , "Tablets" : 699.00 , "Fones de ouvido" : 249.99}

# print("Bem vindo ao e-commerce!")
# escolha_1 = str(input("Escolha um produto; Livros, Tablets, Fones de ouvido: "))
# escolha_2 = str(input("Escolha um produto; Livros, Tablets, Fones de ouvido: "))
# escolha_3 = str(input("Escolha um produto; Livros, Tablets, Fones de ouvido: "))

# print("Os produtos escolhidos foram :")
# print(escolha_1, escolha_2,  escolha_3)
# print("Seus respectivos preços: ", (produtos.get(escolha_1)) + (produtos.get(escolha_2)) + (produtos.get(escolha_3)))

livros = {"Anne Frank" : 99.99, "Pare de se odiar" : 159.99, "Harry Potter" : 299.99},
tablets = {"Multilaser" : 699.99, "Samsung" : 1599.99, "iPad" : 5199.99},
fones = {"iPod" : 999.99, "Xiaomi" : 129.99, "JBL" : 499.99}
produtos = [livros, tablets, fones]






print("Bem vindo ao e-commerce!")
escolha_tipo_1 = int(input("Escolha um produto; 0 - Livros, 1 - Tablets, 2 - Fones de ouvido: "))
escolha_1 = str(input(f'''
Escolha pelo nome:
Livros - Anne Frank, Pare de se odiar, Harry Potter
Tablets - Multilaser, Samsung, iPad
Fones - iPod, Xiaomi, JBL
'''))

print(escolha_1(produtos))

# e_commerce = {

# 1:{
# 'a':20.00,
# 'b':30.00,
# 'c':10.00
# },
# 2:{
# 'a':20.00,
# 'b':30.00,
# 'c':10.00
# },
# 3:{
# 'a':20.00,
# 'b':30.00,
# 'c':10.00
# }
# }

# carrinho = []
# meu_total = []

# print('Digite o id da seção:livros 1 - tablets 2  - fones 3')

# secao = int(input('escolha a sessão: ')) 
# p1 = input('Digite')

# carrinho.append(p1)
# print(carrinho)

# secao2 = int(input('escolha a sessão: ')) 
# p2 = input('Digite')
# carrinho.append(p2)
# print(carrinho)

# v1 = e_commerce[secao][p1]
# v2 = e_commerce[secao2][p2]

# meu_total.extend([v1,v2])

# soma = sum(meu_total)

# print('Carrinho', carrinho)
# print('R$', soma)


# e_commerce = {
# 'livros':20,
# 'tablets':10,
# 'fone':50
# }


# carrinho = []
# meu_total = []

# secao = input('escolha a sessão: ') 
# carrinho.append(secao)
# print(carrinho)

# meu_total.append(e_commerce[secao])

# secao2 = input('escolha a sessão: ')
# carrinho.append(secao2)
# print(carrinho)

# meu_total.append(e_commerce[secao2])



# soma = sum(meu_total)

# print('Carrinho', carrinho)
# print('R$', soma)








# e = {
# 'livros':['a','b','c'],
# 1:[10,20,30],

# 'tablets':['a','b','c'],
# 2:[1,2,3],

# 'fones':['a','b','c'],
# 3:[1,2,3]

# }

# carrinho = []
# meu_total = []

# print('Digite o id da seção:livros - tablets - fones')

# secao = input('escolha a sessão: ')
# print('Digite a seção dos valores 1,2,3')
# sv = int(input('Seção valores: '))
# print('Digite o indice do produto: ')
# p1 = int(input('Digite id produtos 0 1 2'))

# # print(carrinho[secao][p1])

# meu_total.append(e[sv][p1])


# print('Digite o id da seção:livros - tablets - fones')
# secao2 = input('escolha a sessão: ')
# print('Digite a seção dos valores 1,2,3')
# sv2= int(input('Seção valores: '))
# print('Digite o indice do produto: ')
# p2 = int(input('DDigite id produtos 0 1 2'))


# # print(carrinho[secao2][p2])

# meu_total.append(e[sv2][p2])

# soma = sum(meu_total)

# print('Carrinho', e[secao ][p1],e[secao2][p2] )
# print('R$', soma)








