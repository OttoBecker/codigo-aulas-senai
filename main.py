# VARIAVEIS
nome_da_variavel = 35

# print(nome_da_variavel > 5) 

# n1,n2 = 7,10

# print(n1, n2) 

# n1 = 7,10, 15

# print(n1[0], n1[2])

# n1, n2 = (7,10), (15, 19)

# print(n1, n2)

# nome = "dennis" if nome_da_variavel <= 35 else "otto"
# print(nome)

# if (condicao) : && if not (condicao) :
#     ... 
    # Indentação é importante!
# idade = 3
# if idade >= 0:
#     if idade >= 18:
#         print("você é maior de 18")

#     elif idade > 12:
#         print("você é adolescente")
#     else: 
#         print("você é uma criança")
# else:
#     print("Não é permitida a entrada de valores negativos")
# idade = 3
# while idade < 9:
#     print("No ano de: 200" + str(idade), "o marcelo tem:", str(idade) )
#     idade += 1
# else:
#     print("No ano de: 200" + str(idade) + "." + "Qual a idade do marcelo?")

# dar clear no terminal limpa os dados

# for i in range(1,11):
#         if i == 5:
#             continue
#         print(i)
#         if i == 10:
#             break
#     else:
#         print("você é maior de idade")

# idade = -5
# def nome_funcao(par1, par2, par3=0): # Parametro obrigatório à esquerda e não obrigatório a direita
#     # ^^ Preenche com 0 apenas quando não for passado
#     # idade += 10 -- Pode apenas consultar a variável, mas não é possível alterar 
#     # a variável global (Apenas se usar global nome_variavel)
#     # global idade
#     par1 += par2
#     if par1 >= 0:
#         if par1 >= 18:
#             print("você é maior de 18")

#         elif par1 > 12:
#             print("você é adolescente")
#         else: 
#             print("você é uma criança")
#     else:
#         print("Não é permitida a entrada de valores negativos")

#     return par1 >= 12, par1

# n1,n2 = nome_funcao(idade, 19)

# print(n1,n2)


# def func1():
#     print("func1")

# def func2():
#     print("func2")

# def func3():
#      print("func3")

# def elsee():
#      print("Outro")

# # x = 22
# # nomes = { # <- Dicionário
# #     x > 10:func1,
# #     x > 20:func2,
# #     x > 30:func3,
# # }
     
# nomes = { # <- Dicionário
#     1:func1,
#     1:func2,
#     1:func3, # Retorna a última sempre
# }

# # nomes[3]()

# nomes.get(True)()



###############################################################

#1 nome class
#2 caracteristicas (Atributos)
#3 o que vai fazer (Metodos)
#4 Sua característica (Objetos)

"""
Carro

--- Características (Atributos)
marca
modelo
cor
ano
se tem rodas

--- O que faz? (Métodos)
andar
freia
dar ré

--- Objetos
carro1{
    marca fiat
    modelo touro
    cor vermelha
    ano 2024
    tem rodas
}

carro2{
    marca chevrolet
    modelo onix
    cor branca
    ano 2020
    tem rodas
}

"""

# PascalCase
class Pessoa:
        tamanho = 5
        def __init__(self, nome, idade, altura):
            self.nome = nome
            self.idade = idade
            self.altura = altura

        @classmethod
        def func_static(cls, n1=0): # Pode ser executada sem instanciar a classe
            print("Antes:", cls.tamanho)
            cls.tamanho += n1 # Altera para todos os objetos
            print("Depois:", cls.tamanho)

pessoa1 = Pessoa("Otto", 18, 1.78) #Objeto
pessoa2 = Pessoa("Dennis", 26, 1.7) #Objeto
pessoa1.func_static(10) # Altera para todos os objetos
print("-"*50)
Pessoa.func_static(1)
print("-"*50)
pessoa2.func_static()

def teste():
    print(1)

