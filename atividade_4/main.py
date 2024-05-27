# # Inicializando listas para armazenar os dados dos carros
# carros = []
# consumo = []


carro = []
consumo = []

for i in range(1, 4):
    carro = input(f"Carro {i}: ")
    consumo.append(km_por_litro)

distancia = 500
preco_gasolina = 5.58

for i in range (3):
    litros_necessarios = distancia / consumo[i]
    custo = litros_necessarios * preco_gasolina
    print(f"{carro[i]} - {consumo[i]} - {litros_necessarios:.1f} litros - R${custo:.2f}")
