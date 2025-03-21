numeros = (
    int(input("Digite o primeiro número: ")),
    int(input("Digite o segundo número: ")),
    int(input("Digite o terceiro número: ")),
    int(input("Digite o quarto número: "))
)

print(f"\nO número 9 apareceu {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O primeiro número 3 apareceu na posição {numeros.index(3) + 1}.")
else:
    print("O número 3 não foi digitado.")

print("Números pares digitados:", [num for num in numeros if num % 2 == 0])
