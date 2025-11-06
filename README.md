 Calculadora de Sistema Linear — Eliminação de Gauss
=================================================================

📘 Descrição
------------
Este projeto implementa em **Python** o **método de Eliminação de Gauss**, uma técnica clássica para resolver sistemas lineares da forma:

A · x = b

onde `A` é a matriz dos coeficientes, `x` o vetor de incógnitas e `b` o vetor de termos independentes.  
O algoritmo realiza operações elementares de linha sobre a matriz aumentada [A|b] para transformá-la em uma forma triangular superior, seguida de substituição regressiva para encontrar as soluções.


🧮 Funcionamento do Algoritmo
-----------------------------
O método é dividido em três etapas principais:

1. ESCALONAMENTO (Eliminação de Gauss)  
   Elimina os elementos abaixo da diagonal principal, transformando a matriz em forma triangular superior.  
   Inclui pivotamento parcial para maior estabilidade numérica.

2. SUBSTITUIÇÃO REGRESSIVA  
   Após o escalonamento, resolve-se o sistema triangular obtido para determinar os valores das variáveis.

3. VERIFICAÇÃO DA SOLUÇÃO  
   Recalcula os valores substituindo no sistema original e exibe o erro máximo, garantindo que a solução é consistente.


⚙️ Estrutura do Código
-----------------------
O script é composto por funções modulares e bem documentadas:

Função | Descrição
--------|-----------
imprimir_sistema() | Exibe o sistema linear formatado.
imprimir_matriz() | Mostra a matriz aumentada [A|b].
encontrar_pivo() | Encontra o pivô de maior valor absoluto em uma coluna.
trocar_linhas() | Realiza a troca de linhas quando necessário (pivotamento).
escalonamento() | Executa o processo de eliminação de Gauss.
substituicao_regressiva() | Calcula os valores das variáveis a partir do sistema escalonado.
verificar_solucao() | Compara os resultados obtidos com o sistema original e calcula o erro.
resolver_sistema() | Função principal que coordena todas as etapas.
main() | Define o sistema 4×4 de exemplo e executa o programa.


🧠 Exemplo de Execução
-----------------------
Sistema de exemplo:
1x₁ + 2x₂ + 3x₃ + 4x₄ = 40  
2x₁ - 1x₂ + 1x₃ + 3x₄ = 20  
3x₁ + 1x₂ + 2x₃ - 1x₄ = 12  
4x₁ + 3x₂ - 1x₃ + 2x₄ = 23

Saída esperada (resumida):

RESOLUÇÃO DE SISTEMA LINEAR
==================================================
Sistema 4x4

ETAPA 1 - ESCALONAMENTO:
...

ETAPA 2 - SUBSTITUIÇÃO REGRESSIVA:
x4 = 1.234567
x3 = 2.345678
x2 = 3.456789
x1 = 4.567890

VERIFICAÇÃO:
Erro máximo: 3.25e-12
Solução verificada com sucesso!


💻 Como Executar
-----------------
1. Clone o repositório:
   git clone https://github.com/PedroSCL/Calculadora-de-Sistema-Linear.git
   cd Calculadora-de-Sistema-Linear

2. Execute o programa:
   python Sistema_Linear.py

3. (Opcional) Modifique o sistema A e B no final do arquivo para testar outros exemplos.


📈 Tratamento de Erros
-----------------------
O programa detecta e trata casos como:
- Pivôs muito pequenos (< 1e-10) → evita divisão por zero.  
- Sistemas singulares (sem solução única).  
- Pequenas diferenças numéricas (~1e-15) causadas por limitações da aritmética de ponto flutuante.


🧩 Requisitos
--------------
- Python 3.8+
- Nenhuma biblioteca externa é necessária (somente bibliotecas padrão).


👨‍💻 Autor
-----------
Pedro Henrique  
📍 Brasília, DF — Brazil  
💼 Estagiário de Dados no Banco do Brasil  
🎓 Estudante de Ciência da Computação (6º semestre)

LinkedIn: https://www.linkedin.com/in/pedroscl  
GitHub: https://github.com/PedroSCL
