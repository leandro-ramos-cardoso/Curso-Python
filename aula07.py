# Variáveis são utilizadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

# Variáveis sõo usadas para deixar o código mais légivel.
nome_completo = 'Leandro Ramos Cardoso'
soma_dois_mais_dois = 2 + 2
print(nome_completo, soma_dois_mais_dois)

# Nesse caso eu repeti 2x o int('1')
print(int('1'), type(int('1')))

# Para não repetir podemos usar váriáveis.
# Se precisarmos alterar de int('1') para int('2') basta trocar uma única vez.
numeroUm = int('1')
print(numeroUm, type(numeroUm))

print()

nome = 'Leandro'
idade = 37
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)
