# Solicita as informações ao usuário
nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade em estoque: "))

# Armazena os dados em uma tupla
produto = (nome, preco, quantidade)

# Exibe as informações formatadas
print("\nInformações do produto:")
print(f"Nome: {produto[0]}")
print(f"Preço: R$ {produto[1]:.2f}")
print(f"Quantidade em estoque: {produto[2]}")
