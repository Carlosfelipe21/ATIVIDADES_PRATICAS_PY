# Atividade 01:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).


numero = int(input("digite um numero: "))

for tabuada in range(1, 11):
    print(f"{numero} * {tabuada} = {numero*tabuada}")




# Atividade 02:
# Soma de Números de 1 a 100:
# Crie um programa que use um laço for para somar
# todos os números de 1 a 100 e exiba o resultado.


soma = 0
for numero in range(1, 101):
    soma += numero
print(f"a soma dos numero de 1 a 100 é {soma}")




# Atividade 03:
# Caractere por Caractere:
# Escreva um programa que solicite uma palavra ao usuário e use um
# laço for para exibir cada caractere da palavra em uma linha separada.


palavra = str(input("Digite uma palavra: "))
for caractere in palavra:
    print(caractere)




# Atividade 04:
# Contagem Regressiva de 10 a 1:
# Desenvolva um programa que use um laço for para fazer uma
# contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".


for contagem in range(10, 0, -1):
    print(contagem)
print("feliz ano novo!")




# Atividade 05:
# Contagem de Números Positivos e Negativos:
# Escreva um programa que solicite ao usuário 10 números e use um
# laço for com uma condicional para contar quantos são positivos e
# quantos são negativos.
    

positivo = 0
negativo = 0

for c in range(10):
    numero = int(input("digite dez numeros positivos e negativos: "))

    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
print(f"""
    Numeros Positivos:
      {positivo}
    Numeros Negativos:
      {negativo}
    """)
    



# Atividade 06:
# Soma de Números Pares:
# Escreva um programa que use um laço for para somar
# todos os números pares de 1 a 50 e exiba o resultado final.


soma = 0

for numero in range(51):
    if numero % 2 == 0:
        soma += numero
print(f"A soma dos numero pares de 1 a 50 é {soma}!")




# Atividade 07:
# Contagem de Vogais em uma Palavra:
# Crie um programa que solicite uma palavra ao usuário e use um laço for com
# uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.


palavra = str(input("digite uma palavra: "))
contador_vogais = 0

for caractere in palavra:
    if caractere.lower() in "aeiou":
        contador_vogais += 1
print(f"o numeros de vogais é {contador_vogais}")




# Atividade 08:
# Cálculo de Média de Notas:
# Escreva um programa que solicite 5 notas de alunos. Use um laço for
# para somar as notas e uma condicional para exibir a média e a
# classificação ("Aprovado" para média >= 6,
# "Reprovado" para média < 6).


soma = 0
for n in range(5):
    nota = float(input("digite suas notas: "))
    soma += nota
    media = soma / 5
if media >= 6:
    print(f"sua media foi {media}. Parabens!")
    print("aprovado!")
else:
    print(f"sua media foi {media}.")
    print("reprovado!")



# Atividade 09:
# Verificar Números Pares e Impares com Interrupção:
# Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
# identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.


for c in range(1, 21):
    if c % 2 == 0:
        print(f"{c} é par.")
    elif c % 2 != 0:
        print(f"{c} é impar.")
    if c == 15:
        break




# Atividade 10:
# Contar Números Positivos e Negativos:
# Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
# são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.


positivo = 0
negativo = 0

for n in range(10):
    numero = int(input("Digite um número (positivo, negativo ou zero para parar): "))
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    else:
        print("numero 0 inserido interrompendo programa.")
        break
print(f"""
    numero positivos: {positivo}
    numeros negativos: {negativo}
""")




# Atividade 11:
# Verificar Múltiplos de 5 e Parar:
# Escreva um programa que use um laço for para imprimir números de 1 a 30.
# Use uma condicional para verificar se um número é múltiplo de 5 e outro
# para verificar se é maior que 20 e interromper o loop com break.


for n in range(1, 31):
    if n % 5 == 0:
        print(f"{n} é multiplo de 5.")
    elif n > 20:
        break




# Atividade 12:
# Soma de Números com Desconto:
# Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
# calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
# interrompa o loop com break.


soma = 0
for p in range(5):
    preco = float(input("informe o valor dos produtos: "))
    soma += preco
    if soma > 100:
        desconto = soma * 0.90
        print(f"o produto com 10% de desconto ficou de: {desconto}.")
        break
else:
    print(f"o valor dos produtos e de: {soma}")
       

