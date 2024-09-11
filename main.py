import tkinter as tk
from tkinter import messagebox
import numpy as np
from decimal import Decimal
import sympy as sp

# Função do Menu
def MENU():
    root = tk.Tk()
    root.title("Menu Principal")
    root.geometry("400x300")
    root.configure(bg='lightblue')
    
    tk.Label(root, text="Bem-vindo ao Calculador!", font=("Arial", 16, "bold"), bg='lightblue').pack(pady=20)
    
    tk.Button(root, text='Usar GUI', command=GUI, font=("Arial", 12), bg='lightgreen').pack(pady=10, padx=20, fill='x')
    tk.Button(root, text='Não usar GUI', command=shell, font=("Arial", 12), bg='lightcoral').pack(pady=10, padx=20, fill='x')

    root.mainloop()

# Função GUI
def GUI():
    janela = tk.Tk()
    janela.title("MENU")
    janela.geometry("300x500")
    janela.configure(bg='lightblue')
    
    tk.Label(janela, text='Selecione uma opção', font=("Arial", 14, "bold"), bg='lightblue').pack(pady=20)
    
    tk.Button(janela, text='Bhaskara (Raiz real)', command=GUIbhaskarair, font=("Arial", 12), bg='lightgreen').pack(pady=10, padx=20, fill='x')
    tk.Button(janela, text='Bhaskara com raízes complexas', command=GUIbhaskaraI, font=("Arial", 12), bg='lightgreen').pack(pady=10, padx=20, fill='x')
    tk.Button(janela, text='Logarítmos', command=logaritimo, font=("Arial", 12), bg='lightgreen').pack(pady=10, padx=20, fill='x')
    tk.Button(janela, text='Produtos Notáveis', command=prod, font=("Arial", 12), bg='lightgreen').pack(pady=10, padx=20, fill='x')
    tk.Button(janela, text='Integrais', command=GUI_integrais, font=("Arial", 12), bg='lightgreen').pack(pady=10, padx=20, fill='x')

    janela.mainloop()

# Função para a tela de Bhaskara com raízes reais
def GUIbhaskarair():
    bhaskara = tk.Tk()
    bhaskara.title("Bhaskara (Raiz real)")
    bhaskara.geometry("300x250")
    bhaskara.configure(bg='lightblue')
    
    tk.Label(bhaskara, text='Equação de segundo grau', font=("Arial", 14, "bold"), bg='lightblue').pack(pady=10)
    
    tk.Label(bhaskara, text='a', bg='lightblue').pack(pady=5)
    a = tk.Entry(bhaskara, font=("Arial", 12))
    a.pack(pady=5)
    
    tk.Label(bhaskara, text='b', bg='lightblue').pack(pady=5)
    b = tk.Entry(bhaskara, font=("Arial", 12))
    b.pack(pady=5)
    
    tk.Label(bhaskara, text='c', bg='lightblue').pack(pady=5)
    c = tk.Entry(bhaskara, font=("Arial", 12))
    c.pack(pady=5)
    
    def resolver():
        try:
            a_val = float(a.get())
            b_val = float(b.get())
            c_val = float(c.get())
            delta = b_val**2 - 4*a_val*c_val
            if delta > 0:
                x1 = (-b_val + np.sqrt(delta)) / (2 * a_val)
                x2 = (-b_val - np.sqrt(delta)) / (2 * a_val)
                messagebox.showinfo("Resultado", f"Raízes reais: x1 = {x1:.2f}, x2 = {x2:.2f}")
            elif delta == 0:
                x = -b_val / (2 * a_val)
                messagebox.showinfo("Resultado", f"Raiz única: x = {x:.2f}")
            else:
                messagebox.showinfo("Resultado", "Não existem raízes reais")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")
    
    tk.Button(bhaskara, text='Resolver', command=resolver, font=("Arial", 12), bg='lightgreen').pack(pady=10)
    
    bhaskara.mainloop()

# Função para a tela de Bhaskara com raízes complexas
def GUIbhaskaraI():
    bhaskaraI = tk.Tk()
    bhaskaraI.title("Bhaskara (Raiz complexa)")
    bhaskaraI.geometry("300x250")
    bhaskaraI.configure(bg='lightblue')
    
    tk.Label(bhaskaraI, text='a', bg='lightblue').pack(pady=5)
    a = tk.Entry(bhaskaraI, font=("Arial", 12))
    a.pack(pady=5)
    
    tk.Label(bhaskaraI, text='b', bg='lightblue').pack(pady=5)
    b = tk.Entry(bhaskaraI, font=("Arial", 12))
    b.pack(pady=5)
    
    tk.Label(bhaskaraI, text='c', bg='lightblue').pack(pady=5)
    c = tk.Entry(bhaskaraI, font=("Arial", 12))
    c.pack(pady=5)
    
    def resolver():
        try:
            a_val = float(a.get())
            b_val = float(b.get())
            c_val = float(c.get())
            delta = b_val**2 - 4*a_val*c_val
            
            if delta >= 0:
                x1 = (-b_val + np.sqrt(delta)) / (2 * a_val)
                x2 = (-b_val - np.sqrt(delta)) / (2 * a_val)
                messagebox.showinfo("Resultado", f"Raízes reais: x1 = {x1:.2f}, x2 = {x2:.2f}")
            else:
                real_part = -b_val / (2 * a_val)
                imaginary_part = np.sqrt(-delta) / (2 * a_val)
                messagebox.showinfo("Resultado", f"Raízes complexas: x1 = {real_part:.2f} + {imaginary_part:.2f}i, x2 = {real_part:.2f} - {imaginary_part:.2f}i")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")
    
    tk.Button(bhaskaraI, text='Resolver', command=resolver, font=("Arial", 12), bg='lightgreen').pack(pady=10)
    
    bhaskaraI.mainloop()

# Função para a tela de Logaritmos
def logaritimo():
    log = tk.Tk()
    log.title("Logaritmo")
    log.geometry("300x250")
    log.configure(bg='lightblue')
    
    tk.Label(log, text='Número', font=("Arial", 12), bg='lightblue').pack(pady=10)
    
    numero = tk.Entry(log, font=("Arial", 12))
    numero.pack(pady=10)
    
    tk.Label(log, text='Base', font=("Arial", 12), bg='lightblue').pack(pady=10)
    base = tk.Entry(log, font=("Arial", 12))
    base.pack(pady=10)
    
    def resolver():
        try:
            num = float(numero.get())
            base_val = float(base.get())
            if base_val <= 0 or base_val == 1:
                messagebox.showerror("Erro", "A base deve ser maior que 0 e diferente de 1")
                return
            log_base = np.log(num) / np.log(base_val)
            messagebox.showinfo("Resultado", f"Logaritmo de {num} na base {base_val}: {log_base:.2f}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")
    
    tk.Button(log, text='Resolver', command=resolver, font=("Arial", 12), bg='lightgreen').pack(pady=10)
    
    log.mainloop()

# Função para a tela de Produtos Notáveis
def prod():
    prod = tk.Tk()
    prod.title("Produtos Notáveis")
    prod.geometry("300x250")
    prod.configure(bg='lightblue')

    tk.Label(prod, text='Número 1', font=("Arial", 12), bg='lightblue').pack(pady=10)

    numero1 = tk.Entry(prod, font=("Arial", 12))
    numero1.pack(pady=10)

    tk.Label(prod, text='Número 2', font=("Arial", 12), bg='lightblue').pack(pady=10)

    numero2 = tk.Entry(prod, font=("Arial", 12))
    numero2.pack(pady=10)

    def resolver():
        try:
            num1 = float(numero1.get())
            num2 = float(numero2.get())
            soma = num1 + num2
            produto = num1 * num2
            messagebox.showinfo("Resultado", f"Soma: {soma:.2f}, Produto: {produto:.2f}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")

    tk.Button(prod, text='Resolver', command=resolver, font=("Arial", 12), bg='lightgreen').pack(pady=10)

    prod.mainloop()

# Função para a tela de Integrais
def GUI_integrais():
    integrais = tk.Tk()
    integrais.title("Integrais")
    integrais.geometry("300x250")
    integrais.configure(bg='lightblue')

    tk.Label(integrais, text='Função', font=("Arial", 12), bg='lightblue').pack(pady=10)

    funcao = tk.Entry(integrais, font=("Arial", 12))
    funcao.pack(pady=10)

    tk.Label(integrais, text='Variável', font=("Arial", 12), bg='lightblue').pack(pady=10)
    variavel = tk.Entry(integrais, font=("Arial", 12))
    variavel.pack(pady=10)

    def resolver():
        try:
            func = funcao.get()
            var = variavel.get()
            if not func or not var:
                raise ValueError("Por favor, insira uma função e uma variável")
            func = sp.sympify(func)
            integral = sp.integrate(func, sp.Symbol(var))
            messagebox.showinfo("Resultado", f"Integral: {integral}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")

    tk.Button(integrais, text='Resolver', command=resolver, font=("Arial", 12), bg='lightgreen').pack(pady=10)

    integrais.mainloop()

# Função do Shell
def shell():
    shell = tk.Tk()
    shell.title("Shell")
    shell.geometry("300x250")
    shell.configure(bg='lightblue')

    tk.Label(shell, text='Calculadora (Shell)', font=("Arial", 14, "bold"), bg='lightblue').pack(pady=10)
    
    # Adicione aqui widgets e funcionalidades para a calculadora em shell
    
    shell.mainloop()

# Executando o menu principal
MENU()
