# FORMATACAO DE STRING (FSTRING)

# CALCULO DE IMC (Indice de massa corporea)
# Autor: Leandro Ramos Cardoso

nome = 'Leandro Ramos Cardoso'
altura = 1.77
peso = 75.5
imc = peso / (altura ** 2)

# Leandro Ramos Cardoso tem 1.77 de altura,
# pesa 75.5 quilos e seu IMC é
# 34343433

linha1 = f'{nome} tem {altura:,.2f} de altura'
linha2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha1)
print(linha2)
