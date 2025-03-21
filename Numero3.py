cores = ("Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta")

posicao = int(input("Digite um número de 1 a 7 para ver a cor correspondente: "))

if 1 <= posicao <= 7:
    print(f"A cor correspondente é {cores[posicao - 1]}.")
else:
    print("Número inválido! Escolha um número entre 1 e 7.")
