#Exercícios
#1 - Faça um programa que exiba seu nome na tela.

print("dOmInIqUe WaCkErHaGe")

#2 - Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

num1=int(input("Digite um numero: ")) 
num2=int(input("Digite outro numero: ")) 

soma = num1 + num2 

print("A soma dos números é: ",soma)

#3 - Escreva um programa que exiba o resultado de 5a × 2b, em que A vale 3 e B vale 5.

A=3
B=5

resultado=(5*A)*(2*B) 

print("o resultado fica: ",resultado)

#4 – Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

kmtragem=int(input("Digite aqui a quilometragem percorrida: "))
dias=float(input("Digite aqui a quantidade de dias que o carro foi alugado: "))

kmtragem_valor = 60
dias_taxa = 0.15

custo = (kmtragem * kmtragem_valor) + (dias * dias_taxa)

print("O custo total do carro fica: ",custo)

#5 – Usando type() identifique e mostre na tela o tipo das seguintes variáveis: 5, ‘Pedro’, 
# 0.58, 890, 1==1,  ‘O vento levou’.

print('Pedro', type('Pedro'))
print('5', type(5))
print('0.58', type(0.58))
print('890', type(890))
print('1==1', type(1==1))
print('O vento levou', type('O vento levou'))

#6 – Faça um programa que leia o salário de um colaborador e quanto ele irá receber de aumento. 
# Mostre o resultado do salário acrescentando o aumento digitado.

salario=float(input("Digite aqui o seu salario: "))
aumento=float(input("Digite aqui quanto voce ira receber de aumento: "))

salario_novo = salario + aumento

print("O seu novo salario sera: ",salario_novo)

#7 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
#Exiba o valor do desconto e o preço a pagar.

preco=float(input("Digite aqui o preco da mercadoria: "))
desconto=float(input("Digite aqui o desconto do produto: "))

desconto = desconto * 0.01
total_desconto = desconto * preco
preco_total = preco - total_desconto

print("O valor do desconto sera: ",total_desconto)
print("O preco a pagar sera: ",preco_total)

#8 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario=float(input("Digite aqui o seu salario: "))

if salario >= 1250:
    #aumento = salario * 0.1
    #salario = salario + aumento
else:
    #aumento = salario * 0.15
    #salario = salario + aumento

print("O seu novo salario sera: ",salario)

#9 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve 
# perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação 
# mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a 
# comprar dividido pelo número de meses a pagar.

valor_casa=float(input("Digite o valor da casa a comprar: "))
salario=float(input("Digite o seu salario atual: "))
quantidade_anos=int(input("Digite a quantidade de anos a pagar: "))

quantidade_anos = quantidade_anos * 12
prestacao = valor_casa / quantidade_anos

if prestacao <= (salario * 0.3):
    print("O seu emprestimo bancario foi aprovado!")
else:
    print("O seu emprestimo bancario foi rejeitado.")

print("O valor da prestacao sera de: ", prestacao)





