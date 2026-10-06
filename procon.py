# ============================================================
# PROGRAMA: Monitoramento de Preços - Procon
# DISCIPLINA: Algoritmos e Lógica de Programação
# ============================================================

def main():
    print("==========================================")
    print("    SISTEMA DE MONITORAMENTO DE PREÇOS    ")
    print("==========================================")
    print()

    # --- PRODUTO 1 ---
    print("--- DADOS DO PRODUTO 1 ---")
    nomeProd1 = input("Digite o nome do produto: ")
    precoAnt1 = float(input("Digite o preço no mês anterior (R$): "))
    precoAtual1 = float(input("Digite o preço no mês atual (R$): "))
    variacao1 = ((precoAtual1 - precoAnt1) / precoAnt1) * 100

    if variacao1 > 0:
        situacao1 = "AUMENTO"
    elif variacao1 < 0:
        situacao1 = "QUEDA"
    else:
        situacao1 = "ESTÁVEL"
    print()

    # --- PRODUTO 2 ---
    print("--- DADOS DO PRODUTO 2 ---")
    nomeProd2 = input("Digite o nome do produto: ")
    precoAnt2 = float(input("Digite o preço no mês anterior (R$): "))
    precoAtual2 = float(input("Digite o preço no mês atual (R$): "))
    variacao2 = ((precoAtual2 - precoAnt2) / precoAnt2) * 100

    if variacao2 > 0:
        situacao2 = "AUMENTO"
    elif variacao2 < 0:
        situacao2 = "QUEDA"
    else:
        situacao2 = "ESTÁVEL"
    print()

    # --- PRODUTO 3 ---
    print("--- DADOS DO PRODUTO 3 ---")
    nomeProd3 = input("Digite o nome do produto: ")
    precoAnt3 = float(input("Digite o preço no mês anterior (R$): "))
    precoAtual3 = float(input("Digite o preço no mês atual (R$): "))
    variacao3 = ((precoAtual3 - precoAnt3) / precoAnt3) * 100

    if variacao3 > 0:
        situacao3 = "AUMENTO"
    elif variacao3 < 0:
        situacao3 = "QUEDA"
    else:
        situacao3 = "ESTÁVEL"
    print()

    # --- RELATÓRIO FINAL ---
    print("==========================================")
    print("    RELATÓRIO DE MONITORAMENTO DE PREÇOS  ")
    print("==========================================")
    print(f"PRODUTO 1: {nomeProd1}")
    print(f"Preço Ant.: R$ {precoAnt1:.2f} | Atual: R$ {precoAtual1:.2f}")
    print(f"Variação: {variacao1:.2f}% | Situação: {situacao1}")
    print("------------------------------------------")
    print(f"PRODUTO 2: {nomeProd2}")
    print(f"Preço Ant.: R$ {precoAnt2:.2f} | Atual: R$ {precoAtual2:.2f}")
    print(f"Variação: {variacao2:.2f}% | Situação: {situacao2}")
    print("------------------------------------------")
    print(f"PRODUTO 3: {nomeProd3}")
    print(f"Preço Ant.: R$ {precoAnt3:.2f} | Atual: R$ {precoAtual3:.2f}")
    print(f"Variação: {variacao3:.2f}% | Situação: {situacao3}")
    print("==========================================")

if __name__ == "__main__":
    main()
