# Atividade 01: Crie uma variavel chamada "saudacao", em seguida coloque
# uma atribuicao e dentro de dado armazenado escreva "Hello World"

print("hello world")


# Atividade 02: Crie um programa que peca ao usuario para digitar:
# 1.Seu nome;
# 2.Sua idade;
# 3.Sua altura;
# 4.Em seguida, imprima esses valores e seus respectivos tipos.

nome = str(input("digite seu nome: "))
idade = int(input("informe sua idade: "))
altura = float(input("informe sua altura: "))

print(f"ola, meu nome é {nome} tenho {idade} anos e tenho {altura} de altura.")



# Objetivo: Criar um Programa que Peça as 4 Notas
# Bimestrais e Mostre a Média


n_01 = float(input("informe a primeira nota: "))
n_02 = float(input("informe a segunda nota: "))
n_03 = float(input("informe a terceira nota: "))
n_04 = float(input("informe a quarta nota: "))

m_final = (n_01 + n_02 + n_03 + n_04) /4

print(f"sua media final foi: {m_final}")



# Objetivo: Faça um programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês, calcule o salário total e exiba o resultado (Considere que você trabalha
# 20 dias no mês).


ganho_hora = float(input("Quanto ganha por hora?:"))
horas_semanais = float(input("quantas horas por semana?:"))
H_mes = (horas_semanais * 4)
salario_T = (ganho_hora * H_mes)

print(f"seu salario mensal e de {salario_T}")




# Objetivo: Peça ao usuário para digitar seu nome, idade e cidade
# natal. Use uma f-string para formatar e exibir uma mensagem
# com essas informações.


nome = str(input("digite seu nome: "))
idade = int(input("iforme sua idade: "))
C_natal = str(input("informe sua cidade natal: "))

print(f"Ola, meu nome é {nome} tenho {idade} anos e a minha cidade natal é {C_natal}!")