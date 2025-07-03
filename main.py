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