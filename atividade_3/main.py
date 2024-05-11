# votos = [0, 0, 0, 0, 0]  # Índice 0: Chapa 1, 1: Chapa 2, 2: Chapa 3, 3: Branco, 4: Nulo

# for i in range(10):
#   while True:
#     try:
#       voto = int(input(f"Membro {i+1}, digite o número da sua chapa (1, 2, 3), 4 para branco ou 5 para nulo: "))
#       if 1 <= voto <= 5:
#         votos[voto-1] += 1
#         break
#       else:
#         print("Voto inválido. Digite um número entre 1 e 5.")
#     except ValueError:
#       print("Entrada inválida. Digite um número inteiro.")

# print("\n--- Resultados da Eleição ---")
# print(f"Chapa 1: {votos[0]} votos")
# print(f"Chapa 2: {votos[1]} votos")
# print(f"Chapa 3: {votos[2]} votos")
# print(f"Votos em branco: {votos[3]}")
# print(f"Votos nulos: {votos[4]}")

# total_votos_validos = sum(votos[:3])  # Soma os votos das chapas 1, 2 e 3

# chapa_vencedora = votos.index(max(votos[:3])) + 1  # Encontra o índice da chapa com mais votos e soma 1 para obter o número da chapa

# if votos[chapa_vencedora - 1] > total_votos_validos / 2:
#   print(f"\nA Chapa {chapa_vencedora} venceu no primeiro turno!")
# else:
#   print("\nNenhuma chapa obteve maioria absoluta. Haverá segundo turno!")

votos = [0, 0, 0, 0, 0,]

for i in range(10):
    while True:
        try:
            voto = int(input(f"Menbro {i+1}, digite o número da sua chapa (1, 2, 3), 4 para branco ou 5 para nulo: "))
            if 1 <= votos <= 5:
                votos[voto-1] += 1
                break
            else:
                print("Voto inválido. Digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

print("\n--- Resultados da Eleição ---")
print(f"Chapa 1: {votos[0]} votos")
print(f"Chapa 2: {votos[1]} votos")
print(f"Chapa 3: {votos[2]} votos")
print(f"Votos em branco: {votos[3]}")
print(f"Votos nulos: {votos[4]}")

total_votos_validos = sum(votos[:3])

chapa_vencedora = votos.index(max(votos[:3])) + 1

if votos[chapa_vencedora - 1] > total_votos_validos:
    print(f"\nA chapa {chapa_vencedora} venceu no primeiro turno!")
else:
    print("\nNenhuma chapa obteve maioria absoluta. Haverá segundo turno!")