"""
===============================================================================
RESOLUÇÃO DE SISTEMAS LINEARES - MÉTODO DE ELIMINAÇÃO DE GAUSS
===============================================================================

INTRODUÇÃO TEÓRICA:
O método de eliminação de Gauss é uma técnica para resolver sistemas de equações 
lineares do tipo Ax = b através de operações elementares sobre linhas da matriz 
aumentada [A|b], transformando-a em forma triangular superior.

ALGORITMO:
1. ESCALONAMENTO: Eliminar elementos abaixo da diagonal principal
2. SUBSTITUIÇÃO REGRESSIVA: Resolver o sistema escalonado

ERROS NUMÉRICOS:
Pequenos erros (da ordem de 1e-15) são normais devido às limitações da 
aritmética de ponto flutuante. Erros menores que 1e-10 indicam solução correta.
"""

def imprimir_sistema(matriz, termos):
    n = len(matriz)
    print("\nSistema de equações:")
    for i in range(n):
        eq = ""
        for j in range(n):
            coef = matriz[i][j]
            if j == 0:
                eq += f"{coef:6.2f}x{j+1}"
            else:
                sinal = "+" if coef >= 0 else "-"
                eq += f" {sinal} {abs(coef):5.2f}x{j+1}"
        eq += f" = {termos[i]:6.2f}"
        print(f"  {eq}")

def imprimir_matriz(matriz, termos, titulo):
    print(f"\n{titulo}:")
    n = len(matriz)
    for i in range(n):
        linha = "[ "
        for j in range(n):
            linha += f"{matriz[i][j]:8.3f} "
        linha += f"| {termos[i]:8.3f} ]"
        print(f"  {linha}")

def encontrar_pivo(matriz, coluna, linha_inicial):
    # Pivotamento parcial - encontra o maior elemento em valor absoluto
    melhor_linha = linha_inicial
    maior_valor = abs(matriz[linha_inicial][coluna])
    
    for i in range(linha_inicial + 1, len(matriz)):
        valor_atual = abs(matriz[i][coluna])
        if valor_atual > maior_valor:
            maior_valor = valor_atual
            melhor_linha = i
    
    return melhor_linha, maior_valor

def trocar_linhas(matriz, termos, linha1, linha2):
    if linha1 != linha2:
        matriz[linha1], matriz[linha2] = matriz[linha2], matriz[linha1]
        termos[linha1], termos[linha2] = termos[linha2], termos[linha1]
        print(f"  Trocando L{linha1+1} com L{linha2+1}")

def escalonamento(matriz, termos):
    """Transforma a matriz em forma triangular superior"""
    n = len(matriz)
    
    print("\nETAPA 1 - ESCALONAMENTO:")
    print("=" * 40)
    
    for k in range(n):
        print(f"\nProcessando coluna {k+1}:")
        
        # Encontrar melhor pivô
        pivo_linha, valor_pivo = encontrar_pivo(matriz, k, k)
        
        # Verificar se o sistema tem solução
        if valor_pivo < 1e-10:
            print(f"Erro: Pivô muito pequeno ({valor_pivo:.2e})")
            return False
        
        # Trocar linhas se necessário
        if pivo_linha != k:
            trocar_linhas(matriz, termos, k, pivo_linha)
        
        pivo = matriz[k][k]
        print(f"  Pivô: {pivo:.3f}")
        
        # Eliminar elementos abaixo do pivô
        for i in range(k + 1, n):
            if abs(matriz[i][k]) > 1e-10:
                fator = matriz[i][k] / pivo
                print(f"  L{i+1} = L{i+1} - ({fator:.3f}) * L{k+1}")
                
                for j in range(k, n):
                    matriz[i][j] -= fator * matriz[k][j]
                termos[i] -= fator * termos[k]
        
        imprimir_matriz(matriz, termos, f"Após eliminar coluna {k+1}")
    
    return True

def substituicao_regressiva(matriz, termos):
    """Resolve o sistema triangular superior"""
    n = len(matriz)
    solucao = [0.0] * n
    
    print("\nETAPA 2 - SUBSTITUIÇÃO REGRESSIVA:")
    print("=" * 40)
    
    for i in range(n - 1, -1, -1):
        print(f"\nCalculando x{i+1}:")
        
        # Calcular soma dos termos conhecidos
        soma = 0
        for j in range(i + 1, n):
            soma += matriz[i][j] * solucao[j]
        
        # Verificar divisão por zero
        if abs(matriz[i][i]) < 1e-10:
            print(f"Erro: divisão por zero na linha {i+1}")
            return None
        
        # Calcular solução
        solucao[i] = (termos[i] - soma) / matriz[i][i]
        print(f"  x{i+1} = ({termos[i]:.3f} - {soma:.3f}) / {matriz[i][i]:.3f} = {solucao[i]:.6f}")
    
    return solucao

def verificar_solucao(matriz_original, termos_originais, solucao):
    """Verifica se a solução está correta"""
    print("\nVERIFICAÇÃO:")
    print("=" * 30)
    
    n = len(matriz_original)
    erro_max = 0
    
    for i in range(n):
        resultado = 0
        for j in range(n):
            resultado += matriz_original[i][j] * solucao[j]
        
        erro = abs(resultado - termos_originais[i])
        erro_max = max(erro_max, erro)
        
        print(f"Equação {i+1}: {resultado:.6f} ≈ {termos_originais[i]:.6f} (erro: {erro:.2e})")
    
    print(f"\nErro máximo: {erro_max:.2e}")
    if erro_max < 1e-10:
        print("Solução verificada com sucesso!")
    else:
        print("Erro significativo - verificar cálculos")

def resolver_sistema(A, B):
    """Função principal que resolve o sistema linear"""
    n = len(A)
    
    # Fazer cópias dos dados originais
    matriz = [linha[:] for linha in A]
    termos = B[:]
    
    print("RESOLUÇÃO DE SISTEMA LINEAR")
    print("=" * 50)
    print(f"Sistema {n}x{n}")
    
    imprimir_sistema(matriz, termos)
    imprimir_matriz(matriz, termos, "Matriz aumentada inicial")
    
    # Escalonamento
    if not escalonamento(matriz, termos):
        return None
    
    # Substituição regressiva
    solucao = substituicao_regressiva(matriz, termos)
    if solucao is None:
        return None
    
    # Verificação
    verificar_solucao(A, B, solucao)
    
    return solucao

def main():
    # Sistema de exemplo 4x4
    A = [
        [1, 2, 3, 4],
        [2, -1, 1, 3],
        [3, 1, 2, -1],
        [4, 3, -1, 2]
    ]
    
    B = [40, 20, 12, 23]
    
    solucao = resolver_sistema(A, B)
    
    if solucao:
        print("\nSOLUÇÃO FINAL:")
        print("=" * 20)
        for i, valor in enumerate(solucao):
            print(f"x{i+1} = {valor:.6f}")
    else:
        print("\nErro: Sistema sem solução única")

if __name__ == "__main__":
    main()
