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