from datetime import datetime

nome = 'Fulano'
sobrenome = 'De Tal'
idade = datetime.now().year - 2022
ano_nascimento = datetime.now().year - idade
maior_de_idade = 18
altura_metros = 1.10


print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade, 'anos')
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', idade >= maior_de_idade)
print('Altura em metros:', altura_metros)
