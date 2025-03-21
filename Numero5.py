times = ("Flamengo", "Palmeiras", "Grêmio", "São Paulo", "Internacional",
         "Atlético-MG", "Cruzeiro", "Santos", "Corinthians", "Botafogo")

print("Os três primeiros colocados:", times[:3])
print("Os últimos três colocados:", times[-3:])
print("Times em ordem alfabética:", sorted(times))

time_escolhido = input("Digite o nome de um time para ver sua posição: ")

if time_escolhido in times:
    print(f"O time {time_escolhido} está na posição {times.index(time_escolhido) + 1}.")
else:
    print("Time não encontrado na lista.")
