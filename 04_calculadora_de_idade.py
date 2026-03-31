'''Desenvolva um sistema que solicite o ano de nascimento do usuário, calcule e exiba a sua idade atual'''
from datetime import date
hoje = date.today()
#print("A data de hoje é:", hoje)
print(f"A data de hoje é:", hoje.strftime('%d/%m/%Y'))
ano_nascimento = int(input("Digite sua data de nascimento: "))
idade = hoje.year - ano_nascimento
print(idade)