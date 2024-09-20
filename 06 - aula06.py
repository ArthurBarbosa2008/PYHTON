# Esse código tem a função de analisar a sua idade e determinar se você pode ou não votar

idade = int(input("Digite a sua idade: "))

if idade <= 16 and idade > 0:
    print("A sua idade é insuficiente para votar nesse ano")

elif (idade >= 16 and idade < 18) or (idade > 70 and idade < 100):
    print("Seu voto será opcional nesse ano")

elif idade >= 18 and idade < 71:
    print("Seu voto será obrigatório nesse ano")

elif idade > 99:
    print("Você provavelmente não está mais vivo :(")

elif idade < 1:
    print("Você ainda não nasceu :(")