import tkinter as tk
from tkinter import messagebox
from Funcionario_mensal import Funcionario_pago_mensal
from Funcionario_hora import Funcionario_pago_hora
from Funciona_comissao import Funcionario_pago_comissao
from Funcionario_projeto import Projetista

# Função para abrir o formulário de cada tipo de funcionário
def abrir_formulario(tipo_funcionario):
    def processar_pagamento():
        try:
            nome = nome_entry.get()
            matricula = int(matricula_entry.get())
            
            if tipo_funcionario == 'Mensalista':
                salario_total = float(salario_entry.get())
                funcionario = Funcionario_pago_mensal(nome, matricula, salario_total)

            elif tipo_funcionario == 'Horista':
                horas_trabalhadas = float(horas_entry.get())
                valor_hora = float(valor_hora_entry.get())
                funcionario = Funcionario_pago_hora(nome, matricula, horas_trabalhadas, valor_hora)

            elif tipo_funcionario == 'Comissionado':
                salario_base = float(salario_base_entry.get())
                valor_vendas = float(valor_vendas_entry.get())
                taxa_comissao = float(taxa_comissao_entry.get())
                funcionario = Funcionario_pago_comissao(nome, matricula, salario_base, valor_vendas, taxa_comissao)

            elif tipo_funcionario == 'Projetista':
                valor_por_projeto = float(valor_projeto_entry.get())
                quant_projeto = int(quant_projeto_entry.get())
                funcionario = Projetista(nome, matricula, valor_por_projeto, quant_projeto)

            funcionario.calcular_salario()
            messagebox.showinfo("Sucesso", f"Salário processado para {nome}")
            form.destroy()

        except ValueError as e:
            messagebox.showerror("Erro", f"Erro ao processar pagamento: {e}")

    # Configuração da janela do formulário específico
    form = tk.Toplevel(root)
    form.title(f"Cadastro de {tipo_funcionario}")

    # Campos comuns a todos os tipos de funcionários
    tk.Label(form, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    nome_entry = tk.Entry(form)
    nome_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Matrícula:").grid(row=1, column=0, padx=5, pady=5)
    matricula_entry = tk.Entry(form)
    matricula_entry.grid(row=1, column=1, padx=5, pady=5)

    # Campos específicos de cada tipo de funcionário
    if tipo_funcionario == 'Mensalista':
        tk.Label(form, text="Salário Total:").grid(row=2, column=0, padx=5, pady=5)
        salario_entry = tk.Entry(form)
        salario_entry.grid(row=2, column=1, padx=5, pady=5)

    elif tipo_funcionario == 'Horista':
        tk.Label(form, text="Horas Trabalhadas:").grid(row=2, column=0, padx=5, pady=5)
        horas_entry = tk.Entry(form)
        horas_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form, text="Valor Hora:").grid(row=3, column=0, padx=5, pady=5)
        valor_hora_entry = tk.Entry(form)
        valor_hora_entry.grid(row=3, column=1, padx=5, pady=5)

    elif tipo_funcionario == 'Comissionado':
        tk.Label(form, text="Salário Base:").grid(row=2, column=0, padx=5, pady=5)
        salario_base_entry = tk.Entry(form)
        salario_base_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form, text="Valor Vendas:").grid(row=3, column=0, padx=5, pady=5)
        valor_vendas_entry = tk.Entry(form)
        valor_vendas_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form, text="Taxa Comissão (%):").grid(row=4, column=0, padx=5, pady=5)
        taxa_comissao_entry = tk.Entry(form)
        taxa_comissao_entry.grid(row=4, column=1, padx=5, pady=5)

    elif tipo_funcionario == 'Projetista':
        tk.Label(form, text="Valor por Projeto:").grid(row=2, column=0, padx=5, pady=5)
        valor_projeto_entry = tk.Entry(form)
        valor_projeto_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form, text="Quantidade de Projetos:").grid(row=3, column=0, padx=5, pady=5)
        quant_projeto_entry = tk.Entry(form)
        quant_projeto_entry.grid(row=3, column=1, padx=5, pady=5)

    # Botão para processar o pagamento
    processar_button = tk.Button(form, text="Processar Pagamento", command=processar_pagamento)
    processar_button.grid(row=5, column=0, columnspan=2, pady=10)

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Pagamento de Funcionários")

# Botões para abrir cada tipo de formulário
tk.Label(root, text="Selecione o tipo de funcionário para cadastrar:").pack(pady=10)
tk.Button(root, text="Mensalista", command=lambda: abrir_formulario('Mensalista')).pack(pady=5)
tk.Button(root, text="Horista", command=lambda: abrir_formulario('Horista')).pack(pady=5)
tk.Button(root, text="Comissionado", command=lambda: abrir_formulario('Comissionado')).pack(pady=5)
tk.Button(root, text="Projetista", command=lambda: abrir_formulario('Projetista')).pack(pady=5)

# Iniciar o loop da aplicação
root.mainloop()