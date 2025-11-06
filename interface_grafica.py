import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
from io import StringIO
from Sistema_Linear import resolver_sistema


class SistemaLinearGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Sistema Linear - Método de Gauss")
        self.root.geometry("1000x770") 
        self.root.minsize(900, 650)
        self.root.configure(bg="#dce3f0")

        self.tamanho = 3
        self.entradas_matriz = []
        self.entradas_termos = []

        self.criar_estilo()
        self.criar_interface()

    # ---------- ESTILO ----------
    def criar_estilo(self):
        self.cor_primaria = "#1e4a7d"
        self.cor_secundaria = "#2d73d2"
        self.cor_fundo = "#e7ecf5"
        self.cor_card = "#ffffff"
        self.cor_texto = "#1b1b1b"

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TLabel", background=self.cor_card, font=("Segoe UI", 11))
        style.configure("TLabelframe", background=self.cor_card, font=("Segoe UI", 11, "bold"))
        style.configure("TLabelframe.Label", background=self.cor_card, foreground=self.cor_primaria)
        style.configure("TEntry", font=("Segoe UI", 10), relief="flat")
        style.configure("TButton",
                        font=("Segoe UI", 10, "bold"),
                        background=self.cor_secundaria,
                        foreground="white",
                        padding=6)
        style.map("TButton",
                  background=[("active", "#1e56a0")],
                  relief=[("pressed", "groove")])

    # ---------- INTERFACE ----------
    def criar_interface(self):
        # Cabeçalho colorido com emoji separado (mantém cor original)
        header = tk.Frame(self.root, bg=self.cor_primaria, height=75)
        header.pack(fill="x")

        header_inner = tk.Frame(header, bg=self.cor_primaria)
        header_inner.pack(pady=12)

        tk.Label(header_inner, text="Calculadora de Sistema Linear",
                 bg=self.cor_primaria, fg="white",
                 font=("Segoe UI", 22, "bold")).pack(side="left")

        # Container principal
        main = tk.Frame(self.root, bg=self.cor_fundo)
        main.pack(fill="both", expand=True, padx=25, pady=20)

        # Card principal
        card = tk.Frame(main, bg=self.cor_card, bd=0, relief="flat", highlightthickness=0)
        card.pack(fill="both", expand=True, padx=10, pady=10)
        card.grid_columnconfigure(0, weight=1)

        # ---- Configuração ----
        frame_tamanho = ttk.Labelframe(card, text="⚙️ Configuração do Sistema", padding=15)
        frame_tamanho.pack(fill="x", pady=10, padx=15)

        ttk.Label(frame_tamanho, text="Tamanho do sistema:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_tamanho = ttk.Combobox(frame_tamanho, values=["2x2", "3x3", "4x4", "5x5"],
                                          state="readonly", width=10)
        self.combo_tamanho.set("3x3")
        self.combo_tamanho.grid(row=0, column=1, padx=5, pady=5)
        self.combo_tamanho.bind("<<ComboboxSelected>>", self.alterar_tamanho)
        ttk.Button(frame_tamanho, text="Gerar Campos", command=self.gerar_campos).grid(row=0, column=2, padx=15)

        # ---- Matrizes ----
        frame_matrizes = tk.Frame(card, bg=self.cor_card)
        frame_matrizes.pack(pady=10)

        self.frame_matriz = ttk.Labelframe(frame_matrizes, text="Matriz de Coeficientes (A)", padding=10)
        self.frame_matriz.grid(row=0, column=0, padx=20)
        self.frame_termos = ttk.Labelframe(frame_matrizes, text="Termos Independentes (b)", padding=10)
        self.frame_termos.grid(row=0, column=1, padx=20)

        # ---- Botões ----
        frame_botoes = tk.Frame(card, bg=self.cor_card)
        frame_botoes.pack(pady=15)
        ttk.Button(frame_botoes, text="Resolver Sistema", command=self.resolver).grid(row=0, column=0, padx=6)
        ttk.Button(frame_botoes, text="Limpar Campos", command=self.limpar).grid(row=0, column=1, padx=6)
        ttk.Button(frame_botoes, text="Exemplo 4x4", command=self.carregar_exemplo).grid(row=0, column=2, padx=6)

        # ---- Área de resultado ----
        frame_resultado = ttk.Labelframe(card, text="📊 Resultado e Processo", padding=10)
        frame_resultado.pack(fill="both", expand=True, padx=15, pady=(10, 25), ipady=50)


        self.texto_resultado = scrolledtext.ScrolledText(
            frame_resultado,
            height=40,
            width=110,
            bg="#f4f7fc",
            fg="#0a244a",
            font=("Consolas", 11),
            relief="flat",
            wrap="word",
            insertbackground="#1e4a7d",
            borderwidth=0
        )
        self.texto_resultado.pack(fill="both", expand=True, padx=6, pady=6)

        # tags coloridas
        self.texto_resultado.tag_config("titulo", foreground=self.cor_primaria, font=("Consolas", 11, "bold"))
        self.texto_resultado.tag_config("resultado", foreground="#1459c3", font=("Consolas", 11, "bold"))
        self.texto_resultado.tag_config("erro", foreground="#c62828", font=("Consolas", 11, "bold"))

        self.gerar_campos()

    # ---------- FUNÇÕES ----------
    def alterar_tamanho(self, event=None):
        self.tamanho = int(self.combo_tamanho.get()[0])

    def gerar_campos(self):
        for widget in self.frame_matriz.winfo_children():
            widget.destroy()
        for widget in self.frame_termos.winfo_children():
            widget.destroy()

        self.entradas_matriz = []
        self.entradas_termos = []

        for i in range(self.tamanho):
            linha = []
            for j in range(self.tamanho):
                e = ttk.Entry(self.frame_matriz, width=8, justify="center")
                e.grid(row=i, column=j, padx=3, pady=3)
                e.insert(0, "0")
                linha.append(e)
            self.entradas_matriz.append(linha)

        for i in range(self.tamanho):
            ttk.Label(self.frame_termos, text=f"b{i+1}:").grid(row=i, column=0, padx=5, pady=3)
            e = ttk.Entry(self.frame_termos, width=8, justify="center")
            e.grid(row=i, column=1, padx=5, pady=3)
            e.insert(0, "0")
            self.entradas_termos.append(e)

    def carregar_exemplo(self):
        self.combo_tamanho.set("4x4")
        self.tamanho = 4
        self.gerar_campos()

        A = [
            [1, 2, 3, 4],
            [2, -1, 1, 3],
            [3, 1, 2, -1],
            [4, 3, -1, 2]
        ]
        b = [40, 20, 12, 23]

        for i in range(4):
            for j in range(4):
                self.entradas_matriz[i][j].delete(0, tk.END)
                self.entradas_matriz[i][j].insert(0, str(A[i][j]))
            self.entradas_termos[i].delete(0, tk.END)
            self.entradas_termos[i].insert(0, str(b[i]))

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
            A = [[float(self.entradas_matriz[i][j].get()) for j in range(self.tamanho)] for i in range(self.tamanho)]
            B = [float(self.entradas_termos[i].get()) for i in range(self.tamanho)]
            return A, B
        except ValueError:
            messagebox.showerror("Erro", "Insira apenas números válidos!")
            return None, None

    def resolver(self):
        A, B = self.coletar_dados()
        if not A:
            return

        self.texto_resultado.delete(1.0, tk.END)
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        try:
            solucao = resolver_sistema(A, B)
            sys.stdout = old_stdout
            saida = captured_output.getvalue()

            self.texto_resultado.insert(tk.END, "PROCESSO DE ELIMINAÇÃO DE GAUSS:\n", "titulo")
            self.texto_resultado.insert(tk.END, saida + "\n")

            if solucao:
                self.texto_resultado.insert(tk.END, "=" * 60 + "\n", "titulo")
                self.texto_resultado.insert(tk.END, "RESULTADO FINAL:\n", "titulo")
                self.texto_resultado.insert(tk.END, "=" * 60 + "\n", "titulo")
                for i, valor in enumerate(solucao):
                    self.texto_resultado.insert(tk.END, f"x{i + 1} = {valor:.6f}\n", "resultado")

        except Exception as e:
            sys.stdout = old_stdout
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
            self.texto_resultado.insert(tk.END, f"ERRO: {str(e)}", "erro")

        self.texto_resultado.see(tk.END)


def main():
    root = tk.Tk()
    SistemaLinearGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
