===============================================================================
CALCULADORA DE SISTEMA LINEAR — MÉTODO DE ELIMINAÇÃO DE GAUSS
===============================================================================

📘 DESCRIÇÃO
-------------------------------------------------------------------------------
Este projeto implementa em Python o método de **Eliminação de Gauss**, uma técnica
clássica para resolver sistemas lineares da forma:

A · x = b

onde A é a matriz dos coeficientes, x o vetor de incógnitas e b o vetor de termos
independentes. O algoritmo realiza operações elementares sobre a matriz aumentada
[A|b] até atingir uma forma triangular superior, seguida de substituição regressiva
para obter as soluções.

Além da versão em terminal, o projeto inclui agora uma **interface gráfica moderna**
desenvolvida em **Tkinter**, permitindo montar e resolver sistemas de forma interativa
e visual.


🧮 FUNCIONAMENTO DO ALGORITMO
-------------------------------------------------------------------------------
O método é dividido em três etapas principais:

1. ESCALONAMENTO (Eliminação de Gauss)
   Elimina os elementos abaixo da diagonal principal, transformando a matriz em
   forma triangular superior. Inclui pivotamento parcial para maior estabilidade
   numérica.

2. SUBSTITUIÇÃO REGRESSIVA
   Após o escalonamento, resolve o sistema triangular obtido para determinar os
   valores das variáveis.

3. VERIFICAÇÃO DA SOLUÇÃO
   Substitui os resultados no sistema original e calcula o erro máximo, garantindo
   que a solução é consistente.


🖥️ INTERFACE GRÁFICA (TKINTER)
-------------------------------------------------------------------------------
A interface foi construída com **Tkinter puro**, utilizando elementos estilizados e
cores em tons de azul para uma melhor experiência visual.

Ela permite:
- Escolher o tamanho do sistema (até 4×4);
- Inserir manualmente os coeficientes e termos independentes;
- Visualizar o processo completo de resolução (escalonamento, substituição e verificação);
- Exibir resultados no console integrado com rolagem e cores temáticas.

⚙️ ESTRUTURA DO CÓDIGO
-------------------------------------------------------------------------------
O projeto é modular e composto pelos seguintes arquivos:

Arquivo                  | Descrição
--------------------------|----------------------------------------------
Sistema_Linear.py         | Implementa o algoritmo matemático da eliminação de Gauss.
interface_grafica.py      | Interface gráfica Tkinter para interação com o usuário.
README.txt                | Este arquivo de documentação.

Principais funções do módulo de cálculo:

Função                    | Descrição
---------------------------|----------------------------------------------
imprimir_sistema()         | Exibe o sistema linear formatado.
imprimir_matriz()          | Mostra a matriz aumentada [A|b].
encontrar_pivo()           | Encontra o pivô de maior valor absoluto em uma coluna.
trocar_linhas()            | Realiza o pivotamento de linhas.
escalonamento()            | Executa o processo de eliminação de Gauss.
substituicao_regressiva()  | Calcula as variáveis do sistema triangular.
verificar_solucao()        | Recalcula o sistema e mostra o erro máximo.
resolver_sistema()         | Coordena todas as etapas da resolução.


💻 COMO EXECUTAR
-------------------------------------------------------------------------------
1. Clone o repositório:
   git clone https://github.com/PedroSCL/Calculadora-de-Sistema-Linear.git
   cd Calculadora-de-Sistema-Linear

2. Execute a versão com interface gráfica:
   python interface_grafica.py

3. (Opcional) Execute a versão em console:
   python Sistema_Linear.py

4. (Opcional) Modifique os coeficientes das matrizes A e B para testar outros sistemas.


📈 TRATAMENTO DE ERROS
-------------------------------------------------------------------------------
O programa realiza verificações automáticas para evitar falhas numéricas e inconsistências:

- Pivôs muito pequenos (< 1e-10) são tratados para evitar divisão por zero;
- Detecta sistemas singulares (sem solução única);
- Compensa pequenas diferenças numéricas (~1e-15) de ponto flutuante;
- Exibe mensagens de erro amigáveis na interface.


🧩 REQUISITOS
-------------------------------------------------------------------------------
- Python 3.8+
- Nenhuma biblioteca externa necessária (Tkinter já incluso).


👨‍💻 AUTOR
-------------------------------------------------------------------------------
Pedro Henrique  
📍 Brasília, DF — Brasil  
💼 Estagiário de Dados no Banco do Brasil  
🎓 Estudante de Ciência da Computação (6º semestre)

LinkedIn: https://www.linkedin.com/in/pedroscl  
GitHub: https://github.com/PedroSCL
