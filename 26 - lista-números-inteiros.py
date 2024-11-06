# Esse código tem como objetivo que o usuário adicionar 5 valores para a lista
# Logo em seguida, a lista vai retornar o maior, o menor e a soma de todos os valores

lista = [] # lista sem valores

#Adicionando os valores
while len(lista) < 5:
    valor = float(input("Digite um número para a lista: "))
    lista.append(valor)

# Retornando os valores
print(f'\nMenor valor = {min(lista)}') # valor menor 
print(f'Maior valor = {max(lista)}') # valor maior
print(f'Soma da lista = {sum(lista)}') # soma da lista

print("\nFim do código...")