def main():
    votos_chapa1 = 0
    votos_chapa2 = 0
    votos_chapa3 = 0
    votos_em_branco = 0
    votos_nulos = 0

    for i in range(10):
        voto = int(input(f"Eleito {i+1}, vote na chapa desejada (1, 2, 3,) ou digite 0 para voto em branco: "))
        if voto == 1:
            votos_chapa1 += 1
        elif voto == 2:
            votos_chapa2 += 1
        elif voto == 3:
            votos_chapa3 += 1
        elif voto == 0:
            votos_em_branco += 1
        else:
            votos_nulos += 1
    total_votos_validos = votos_chapa1 + votos_chapa2 + votos_chapa3
    total_votos = total_votos_validos + votos_em_branco + votos_nulos

    if total_votos_validos > 0:
        percentual_mais_votado = max(votos_chapa1, votos_chapa2, votos_chapa3) / total_votos_validos * 100
        if percentual_mais_votado > 50:
            print("Resultado final: ")
            print(f"Chapa 1: {votos_chapa1} votos")
            print(f"Chapa 2: {votos_chapa2} votos")
            print(f"Chapa 3: {votos_chapa3} votos")
            print(f"Votos em branco: {votos_em_branco}")
            print(f"Votos nulos: {votos_nulos}")
            print("A Chapa", end=" ")
            if votos_chapa1 > votos_chapa2 and votos_chapa1 > votos_chapa3:
                print("1 é o vencedor no primeiro turno.")
            elif votos_chapa2 > votos_chapa1 and votos_chapa2 > votos_chapa3:
                print("2 é o vencedor no primeiro turno.")
            else:
                print("3 é o vencedor no primeiro turno.")
            return
    
    print("Rusltado final:")
    print(f"Chapa 1: {votos_chapa1} votos")
    print(f"Chapa 2: {votos_chapa2} votos")
    print(f"Chapa 3: {votos_chapa3} votos")
    print(f"Votos em branco: {votos_em_branco}")
    print(f"Votos nulos: {votos_nulos}")
    print("Nenhum candidato obteve mais de 50% dos votos válidos. Haverá um segundo turno.")

if __name__ == "__main__":
    main()