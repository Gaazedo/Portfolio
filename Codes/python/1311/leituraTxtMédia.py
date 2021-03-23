arquivo = open('filmes_notas.txt', 'r')
linha = arquivo.readline()

dados = linha.split(':')

print(dados[1])