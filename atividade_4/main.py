def calcular_consumo_combustivel(modelo_carro, consumo_km_1, distancia, preco_gasolina):
    consumo_litros = distancia / consumo_km_1
    custo_total = consumo_litros * preco_gasolina
    return {
        'consumo_litros': consumo_litros,
        'custo_total': custo_total,
    }

modelos_carros = [
    input("Modelo do carro 1: "),
    input("Modelo do carro 2: "),
    input("Modelo do carro 3: "),
]

consumos_km_1 = [
    float(input("Consumo de combustível do carro 1 (Km/L): "))
    float(input("Consumo de combustível do carro 2 (Km/L): "))
    float(input("Consumo de combustível do carro 3 (Km/L): "))
]

distancia = float(input("Distancia a ser percorrida (KM): "))
preco_gasolina = float(input("Preço da gasolina (R$/L): "))

resultados = []
for modelo_carro, consumos_km_1 in zip(modelos_carros, consumos_km_1):
    resultado = calcular_consumo_combustivel(
        modelo_carro, consumos_km_1, distancia, preco_gasolina)
    resultados.append({
        'modelo_carro': modelo_carro,
        **resultado,
    })

for resultado in resultados:
    print(f"\n**{resultado['modelo_carro']}**")
    print(f"Consumo de combustivel: {resultado['consumo_litros']:.2f}")
    print(f"Custo total: R${resultado['custo_total']:.2f}")

carro_mais_economico = min(resultados, key=lambda x: x['consumo_litros'])
print(f"\n**Carro mais econômico:** {carro_mais_economico['modelo_carro']}")