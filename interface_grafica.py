import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import sys
from io import StringIO

# Importar as funções do seu arquivo original
from Sistema_Linear import resolver_sistema

class SistemaLinearGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Sistema Linear - Método de Gauss")
        self.root.geometry("800x600")
        
        # Variável para armazenar o tamanho do sistema
        self.tamanho = 3
        self.entradas_matriz = []
        self.entradas_termos = []
        
        self.criar_interface()
    
    def criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        titulo = ttk.Label(main_frame, text="Resolução de Sistemas Lineares", 
                          font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Frame para seleção do tamanho
        frame_tamanho = ttk.Frame(main_frame)
        frame_tamanho.grid(row=1, column=0, columnspan=3, pady=10)
        
        ttk.Label(frame_tamanho, text="Tamanho do sistema:").grid(row=0, column=0, padx=5)
        
        self.combo_tamanho = ttk.Combobox(frame_tamanho, values=['2x2', '3x3', '4x4', '5x5'], 
                                         state="readonly", width=10)
        self.combo_tamanho.set('3x3')
        self.combo_tamanho.grid(row=0, column=1, padx=5)
        self.combo_tamanho.bind('<<ComboboxSelected>>', self.alterar_tamanho)
        
        ttk.Button(frame_tamanho, text="Gerar Campos", 
                  command=self.gerar_campos).grid(row=0, column=2, padx=10)
        
        # Frame para a matriz de coeficientes
        self.frame_matriz = ttk.LabelFrame(main_frame, text="Matriz de Coeficientes (A)", 
                                          padding="10")
        self.frame_matriz.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        # Frame para termos independentes
        self.frame_termos = ttk.LabelFrame(main_frame, text="Termos Independentes (b)", 
                                          padding="10")
        self.frame_termos.grid(row=2, column=2, pady=10, padx=10, sticky=(tk.W, tk.E))
        
        # Botões
        frame_botoes = ttk.Frame(main_frame)
        frame_botoes.grid(row=3, column=0, columnspan=3, pady=10)
        
        ttk.Button(frame_botoes, text="Resolver Sistema", 
                  command=self.resolver, style="Accent.TButton").grid(row=0, column=0, padx=5)
        ttk.Button(frame_botoes, text="Limpar Campos", 
                  command=self.limpar).grid(row=0, column=1, padx=5)
        ttk.Button(frame_botoes, text="Exemplo 4x4", 
                  command=self.carregar_exemplo).grid(row=0, column=2, padx=5)
        
        # Área de resultado
        frame_resultado = ttk.LabelFrame(main_frame, text="Resultado e Processo", padding="10")
        frame_resultado.grid(row=4, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultado, height=15, width=90)
        self.texto_resultado.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar redimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        frame_resultado.columnconfigure(0, weight=1)
        frame_resultado.rowconfigure(0, weight=1)
        
        # Gerar campos iniciais
        self.gerar_campos()
    
    def alterar_tamanho(self, event=None):
        tamanho_str = self.combo_tamanho.get()
        self.tamanho = int(tamanho_str[0])
    
    def gerar_campos(self):
        # Limpar campos existentes
        for widget in self.frame_matriz.winfo_children():
            widget.destroy()
        for widget in self.frame_termos.winfo_children():
            widget.destroy()
        
        self.entradas_matriz = []
        self.entradas_termos = []
        
        # Criar campos para a matriz
        for i in range(self.tamanho):
            linha_entradas = []
            for j in range(self.tamanho):
                entry = ttk.Entry(self.frame_matriz, width=8, justify="center")
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, "0")
                linha_entradas.append(entry)
            self.entradas_matriz.append(linha_entradas)
        
        # Criar campos para termos independentes
        for i in range(self.tamanho):
            ttk.Label(self.frame_termos, text=f"b{i+1}:").grid(row=i, column=0, padx=5)
            entry = ttk.Entry(self.frame_termos, width=8, justify="center")
            entry.grid(row=i, column=1, padx=5, pady=2)
            entry.insert(0, "0")
            self.entradas_termos.append(entry)
    
    def carregar_exemplo(self):
        # Carregar exemplo 4x4
        self.combo_tamanho.set('4x4')
        self.tamanho = 4
        self.gerar_campos()
        
        # Matriz de exemplo
        exemplo_A = [
            [1, 2, 3, 4],
            [2, -1, 1, 3],
            [3, 1, 2, -1],
            [4, 3, -1, 2]
        ]
        exemplo_B = [40, 20, 12, 23]
        
        # Preencher campos
        for i in range(4):
            for j in range(4):
                self.entradas_matriz[i][j].delete(0, tk.END)
                self.entradas_matriz[i][j].insert(0, str(exemplo_A[i][j]))
            
            self.entradas_termos[i].delete(0, tk.END)
            self.entradas_termos[i].insert(0, str(exemplo_B[i]))
    
    def limpar(self):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                self.entradas_matriz[i][j].delete(0, tk.END)
                self.entradas_matriz[i][j].insert(0, "0")
            
            self.entradas_termos[i].delete(0, tk.END)
            self.entradas_termos[i].insert(0, "0")
        
        self.texto_resultado.delete(1.0, tk.END)
    
    def coletar_dados(self):
        try:
            # Coletar matriz A
            A = []
            for i in range(self.tamanho):
                linha = []
                for j in range(self.tamanho):
                    valor = float(self.entradas_matriz[i][j].get())
                    linha.append(valor)
                A.append(linha)
            
            # Coletar vetor B
            B = []
            for i in range(self.tamanho):
                valor = float(self.entradas_termos[i].get())
                B.append(valor)
            
            return A, B
        
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira apenas números nos campos!")
            return None, None
    
    def resolver(self):
        A, B = self.coletar_dados()
        if A is None or B is None:
            return
        
        # Limpar área de resultado
        self.texto_resultado.delete(1.0, tk.END)
        
        # Capturar a saída do print
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            # Resolver o sistema
            solucao = resolver_sistema(A, B)
            
            # Restaurar stdout
            sys.stdout = old_stdout
            
            # Mostrar resultado na interface
            output = captured_output.getvalue()
            self.texto_resultado.insert(tk.END, output)
            
            if solucao:
                self.texto_resultado.insert(tk.END, "\n" + "="*50 + "\n")
                self.texto_resultado.insert(tk.END, "RESUMO DA SOLUÇÃO:\n")
                self.texto_resultado.insert(tk.END, "="*50 + "\n")
                for i, valor in enumerate(solucao):
                    self.texto_resultado.insert(tk.END, f"x{i+1} = {valor:.6f}\n")
        
        except Exception as e:
            sys.stdout = old_stdout
            messagebox.showerror("Erro", f"Erro durante o cálculo: {str(e)}")
            self.texto_resultado.insert(tk.END, f"ERRO: {str(e)}")
        
        # Rolar para o final
        self.texto_resultado.see(tk.END)

def main():
    root = tk.Tk()
    app = SistemaLinearGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()