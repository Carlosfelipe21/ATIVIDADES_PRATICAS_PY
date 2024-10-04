# Atividade 01:
# Comparação de Idades:
# Peça ao usuário duas idades e use operadores de comparação para
# verificar se a primeira idade é maior, menor ou igual à segunda.


# idade_1 = int(input("informe sua idade: "))
# idade_2 = int(input("informe a outra idade: "))

# print(idade_1 > idade_2)
# print(idade_1 < idade_2)
# print(idade_1 == idade_2)



# Atividade 02:
# Verificar Igualdade de Strings:
# Peça ao usuário duas palavras e use operadores
# de comparação para verificar se elas são iguais.


# palavra_01 = str(input("digite uma palavra: "))
# palavra_02 = str(input("informe outra palavra: "))

# print(palavra_01 == palavra_02)



# Atividade 03:
# Verificação de Maioridade e Habilitação:
# Crie um programa que peça a idade do usuário e se ele possui habilitação
# (sim ou não). Use operadores lógicos para verificar se ele é maior de idade
# (>= 18) e possui habilitação.



# idade = int(input("informe sua idade: "))
# cnh = input("voce possui habilitaçao?(sim | nao): ")

# print(idade >= 18)
# print(cnh)



#  Atividade 04:
# Verificação de Notas Aprovadas:
# Escreva um programa que peça duas notas de um aluno. Use operadores
# lógicos para verificar se as duas notas são maiores ou iguais a 6.




# n_01 = float(input("informe a primeira nota: "))
# n_02 = float(input("informe a segunda nota: "))

# print(n_01 >= 6)
# print(n_02 >= 6)



# Atividade 05:
# Desconto em Preço:
# Peça ao usuário para inserir o preço de um produto e, em seguida,
# use o operador de atribuição -= para aplicar um desconto de 5%.


# produto = "bicicleta"
# V_produto = float(input("informe o valor do produtro: "))
# D = (V_produto - (V_produto*5/100))

# print(F"O produto com o desconto ficou por {D}R$.")

#nao conseguir fazer de outra forma estou estudando pra isso


# Atividade 06:
# Dobro do Valor:
# Solicite ao usuário um número e use o operador de
# atribuição *= para dobrar o valor e exibir o resultado.



# numero = float(input("informe um numero: "))

# dobro = (numero * 2)
# print(dobro)


#nao conseguir fazer de outra forma estou estudando pra isso



# Atividade 07:
# Verificação de Caracteres em uma String:
# Crie um programa que peça ao usuário uma frase e um caractere.
# Use o operador de associação in para verificar se o caractere está
# presente na frase.


# frase = str(input("escreva uma frase: "))
# caractere = str(input("informe um caractere: "))

# resultado = (caractere) in (frase)

# print(resultado)




# Atividade 08:
# Verificação de Palavras em uma Frase:
# Peça ao usuário para inserir uma frase e uma palavra.
# Use in para verificar se a palavra está na frase.


# frase = str(input("escreva uma frase: "))
# palavra = str(input("informe uma palavra: "))

# resultado = (palavra) in (frase)

# print(resultado)


# Atividade 09:
# Verificar Par ou Ímpar:
# Crie um programa que peça ao usuário um número e use a
# estrutura condicional if para verificar se ele é par ou ímpar.



# numero = int(input("informe um numero: "))

# if numero % 2 == 0:
#     print("o numero e par.")
# else:
#     print("o numero e impar")




# Atividade 10:
# Verificar Nota para Aprovado:
# Crie um programa que peça a nota de um aluno e
# use if para verificar se ele foi aprovado (nota >= 6).



# nota = float(input("informe sua nota: "))

# if nota >= 6:
#     print("parabens você foi aprovado.")
# else:
#     print("Reprovado.")






# ou negativAtividade 11:
# Verificar Par ou Ímpar e Positivo ou Negativo:
# Escreva um programa que peça um número e use if para verificar
# se ele é par ou ímpar e também se é positivo ou negativo.o.



# numero = int(input("informe um numero: "))

# if numero % 2 == 0:
#    print("o numero e par.")
# else:
#    print("o numero e impar")

# if numero > 0:
#     print("O numero e positivo")
# if numero < 0:
#     print("O numero e negativo")







# Atividade 12:
# Verificar Classificação de IMC:
# Crie um programa que calcule o Índice de Massa Corporal (IMC)
# e use if para classificar o resultado em "Abaixo do peso"
# ,"Peso normal" "Sobrepeso" e "Obesidade".



# imc = float(input("informe seu peso: "))

# if imc < 50:
#     print("abaixo do peso.")
# elif imc == 50:
#     print("peso normal.")
# elif imc <= 70:
#     print("sobrepeso.")
# else:
#     print("obesidade.")





# Atividade 13:
# Sistema de Login Simples:
# Desenvolva um programa que peça ao usuário um nome de usuário
# e uma senha e use if para verificar se são iguais a "admin" e "1234"
# ,respectivamente.





# usuario = str(input("informe seu nome de usuario: "))
# senha = input("informe sua senha: ")

# if usuario == "felipe21" and senha == "1234":
#     print("usuario e senha correta.")
# elif usuario != "felipe21" and senha == "1234":
#     print("usuario invalido.")
# else:
#     print("senha incorreta.")





# Atividade 14:
# Verificar Status de Taxa de Desconto:
# Crie um programa que peça ao usuário o preço original de um produto e
# a quantidade comprada. Use if para verificar se a quantidade é maior que
# 10 para aplicar um desconto de 10% sobre o total.



produto = "carro"
preco = float(input("informe o preço do carro: "))
Q = int(input("informe a quantidade: "))

desconto = (preco - (preco*10/100))

if Q > 10:
    print(f"Menos 10% de Desconto o valor fica de {desconto}R$")
else:
    print("sem desconto")