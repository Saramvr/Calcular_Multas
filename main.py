def multa_localidade(velocidade: float) -> int:
    if velocidade < 50:
        return 0
    elif velocidade >= 120:
        return 320
    elif velocidade >= 90:
        return 120
    elif velocidade > 50:
        return 60
    return 0

def multa_fora_localidade(velocidade: float) -> int:
    if velocidade < 50:
        return 0
    elif velocidade >= 120:
        return 120
    elif velocidade > 90:
        return 60
    return 0

def multa_autoestrada(velocidade: float) -> int:
    if velocidade < 50:
        return 0
    elif velocidade > 175:
        return 360
    elif velocidade > 150:
        return 120
    elif velocidade > 120:
        return 60
    return 0

def main():
    while True:
        print("Onde circulava o veículo?")
        print("Escolha uma opção:")
        print("1 - Localidade")
        print("2 - Fora da localidade")
        print("3 - Autoestrada")
        print()
        
        try:
            loc = int(input("Introduza o local: "))
        except ValueError:
            print("Por favor, introduza um número válido para o local.")
            continue

        if loc not in (1, 2, 3):
            print("Opção inválida! Tente novamente.")
            continue

        try:
            velocidade = float(input("Introduza a velocidade do carro (km/h): "))
            if velocidade < 0:
                print("Velocidade não pode ser negativa.")
                continue
        except ValueError:
            print("Valor inválido para a velocidade.")
            continue

        if loc == 1:
            multa = multa_localidade(velocidade)
            local = "localidade"
        elif loc == 2:
            multa = multa_fora_localidade(velocidade)
            local = "fora da localidade"
        else:
            multa = multa_autoestrada(velocidade)
            local = "autoestrada"

        if multa == 0:
            print(f"Na {local}, com {velocidade} km/h, não há multa.")
        else:
            print(f"Na {local}, com {velocidade} km/h, a multa é de {multa}€.")

        print()
        continuar = input("Quer continuar? (s/n): ").lower()
        if continuar != 's':
            print("Programa terminado. Obrigado! ")
            break

if __name__ == "__main__":
    main()    