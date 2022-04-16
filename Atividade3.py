#Crie um programa que apresente o nome de uma pessoa e seu salário do mês de abril e mostre no formato padrão.

pessoa = input("Insira seu primeiro nome: ")
valor = input("Insira seu salário do mês de abril: ")

parte1valor = valor[0:1]
parte2valor = valor[1:3]

pessoavalor = "O salário de" + pessoa + "no mês de abril foi de R$" + parte1valor + "." + parte2valor + "," + "00" + "reais" 

print(pessoavalor)