# Atividade 01:
# Contagem de 1 a 10:
# Crie um programa que use um laço while
# para contar de 1 a 10 e exibir cada número.


contador = 1
while contador <= 10:
    print(contador)
    contador += 1



# Atividade 02:
# Soma de Números de 1 a 100:
# Escreva um programa que use um laço while para
# somar os números de 1 a 100 e exiba o resultado.


soma = 0
contador = 1
while contador <= 100:
    soma += contador
    contador += 1
print(f"a somas dos numeros de 1 a 100 é: {soma}.")




# Atividade 03:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).


numero = int(input("digite um numero: "))
contador = 0
while contador < 10:
    contador += 1
    print(f"{numero} * {contador} = {numero*contador} ")
    



# Atividade 04:
# Contagem Regressiva:
# Desenvolva um programa que use um laço while para exibir
# uma contagem regressiva de 10 até 1 e, em seguida, exiba
# "Feliz Ano Novo"



contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print("feliz ano novo")




# Atividade 05:
# Contagem até o Número Inserido:
# Crie um programa que solicite um número ao usuário e use
# um laço while para contar de 1 até o número inserido,
# exibindo apenas os números ímpares.



numero = int(input("digite um numero: "))
contador = 1
while contador <= numero:
    if contador % 2 != 0:
        print(contador)
    contador += 1




# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.


numero = int(input("digite um numero: "))
soma = 0
while numero >= 0:
    soma += numero
    numero = int(input("digite um numero negativo."))
    
    if numero < 0:
        print(f"a somas dos numero positivos inseridos é: {soma}")




# Atividade 07:
# Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.



numero = int(input("digite um numero: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    if resultado % 2 != 0:
        print(f"{numero} * {contador} = {resultado}")
    contador += 1
        

    
# Atividade 08:
# Média de Notas:
# Desenvolva um programa que solicite as notas dos alunos até
# que o usuário digite -1. Calcule e exiba a média das notas
# inseridas.

# pedi ajuda ao chatGPT


soma_notas = 0
quantidade_de_notas = 0
nota = float(input("digite sua nota : "))

while nota >= 0:
    soma_notas += nota
    quantidade_de_notas += 1
    nota = float(input("digite um numero negativo para encerra: "))
if quantidade_de_notas  > 0:
    media = soma_notas / quantidade_de_notas
    print(f"A média das notas é: {media:.2f}")
else:
    print("nada inserido")
    
   





# Atividade 09:
# Contagem até 10:
# Crie um programa que use um laço while para contar de 1 a 10
# e termine quando atingir 10.


contador = 1
while True:
    print(contador)
    if contador == 10:
        break
    contador += 1



# Atividade 10:
# Soma até 50:
# Escreva um programa que use um laço while para somar
# números consecutivos começando de 1 e termine quando
# a soma atingir ou ultrapassar 50.


contador = 1
soma = 0
while True:
    soma += contador
    print(contador)
    if contador >= 50:
        print(f"a soma dos numeros foi {soma}.")
        break
    contador += 1



# Atividade 11:
# Entrada Válida:
# Crie um programa que solicite ao usuário um número entre 1 e 10.
# Continue pedindo até que o usuário forneça um valor válido.


numero = int(input("digite um numero de 1 a 10: "))
while numero < 1 or numero > 10:
    print("numero invalido! tente novamente.")
    numero = int(input("digite um numero de 1 a 10: "))
print(f"voce digitou corretamente.{numero:.2f}")



# Atividade 12:
# Senha Correta:
# Desenvolva um programa que peça ao usuário para digitar uma
# senha e continue pedindo até que a senha correta (previamente
# definida) seja inserida.


senha = ""
while senha != "12345":
    senha = input("digite sua senha: ")
    if senha == "12345":
        print("acesso permitido.")
        break





# Desafios Praticos

# 1 - Soma de Números Pares:
# Crie um programa que use um laço while para somar
# todos os números pares de 1 a 100 e exiba o resultado.


soma = 0
contador = 1

while contador <= 100:
    print(contador)
    if contador % 2 == 0:
        soma += contador
    contador += 1
print(f"a soma dos numero pares de 1 a 100 é {soma}")



# 2 - Números Ímpares de 1 a 50:
# Escreva um programa que use um laço while
# para exibir todos os números ímpares de 1 a 50.


contador = 1
while contador <= 50:
    if contador % 2 != 0:
        print(contador)
    contador += 1
