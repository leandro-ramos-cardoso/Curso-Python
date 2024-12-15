# Conversão de tipos, coercão
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1)
print('a' + 'b') # Concatenou duas strings (Uniu)

# print('1' + 1)
print('1', type('1'))

# Convertendo de str (string) para int (inteiro)
print(int('1'), type(int('1')))

# Para fazer uma soma de 1 + 1 onde o dado veio como str tera que converter para int
# print('1' + 1)

# Convertendo
print('1 + 1 é igual a 2 do tipo', type(int('1') + 1))

# Convertendo para bool
print(bool(' '))

# Convertendo para str
print(str(11) + 'b')

# Convertendo para float
print(float(11))
