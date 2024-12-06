# Argumentos não nomeados = 12, 34
# Argumentos nomeados (nome_argumento = . Ex é o sep.)
print(12, 34, 1000, sep='-', end='\n@');
print(56, 78, sep="*");
print(56, 78, sep="**");

# Quebra de linha tem caracteres diferentes em SO diferentes.

# Linux ou MAC = LF (\n)
# Windows = CRLF (\r\n)

# No argumento end por padrao ele passa a quebra de linha, mas podemos usar qualquer caracteres que desejarmos.