import tkinter as tk
from tkinter import messagebox
from crud_stuff_fornecedores import add_supplier,read_suppliers
class CRUDApp:
    def __init__(self,root):
        self.root=root
        self.root.title("FORNECEDORES")
        #criação de widgets
        self.create_widgets()
    def create_widgets(self):
        #Labels
        tk.Label(self.root,text="Nome:").grid(row=0,column=0)
        tk.Label(self.root,text="Etoque:").grid(row=1,column=0)
        tk.Label(self.root,text="Valor:").grid(row=2,column=0)
        tk.Label(self.root,text="Usuario:").grid(row=3,column=0)
        tk.Label(self.root,text="Id Produto (for update/delete):").grid(row=4,column=0)
        #criar as caixas para digitar os valores
        self.nome_entry=tk.Entry(self.root)
        self.estoque_entry=tk.Entry(self.root)
        self.valor_entry=tk.Entry(self.root)
        self.descricao_entry=tk.Entry(self.root)
        self.idproduto_entry=tk.Entry(self.root)
        self.nome_entry.grid(row=0,column=1)
        self.estoque_entry.grid(row=1,column=1)
        self.valor_entry.grid(row=2,column=1)
        self.usuario_entry.grid(row=3,column=1)
        self.idproduto_entry.grid(row=4,column=1)
        #botões do crud
        tk.Button(self.root,text="Adicionar fornecedor",command=self.add_supplier).grid(row=6,column=0,columnspan=1)
        tk.Button(self.root,text="Listar fornecedores",command=self.read_suppliers).grid(row=6,column=1,columnspan=1)
        self.text_area=tk.Text(self.root,height=10,width=80)
        self.text_area.grid(row=9,column=0,columnspan=4)
    def add_supplier(self):
        nome=self.nome_entry.get()
        estoque=self.estoque_entry.get()
        valor=self.valor_entry.get()
        if nome and estoque and valor:
            add_supplier(nome,estoque,valor)
            self.nome_entry.delete(0,tk.END)
            self.estoque_entry.delete(0,tk.END)
            self.valor_entry.delete(0,tk.END)
            messagebox.showinfo("Successo","Fornecedor adicionado com sucesso")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios")
    def read_suppliers(self):
        suppliers=read_suppliers()
        self.text_area.delete(1.0,tk.END)
        for supplier in suppliers:
            self.text_area.insert(tk.END,f"id: {supplier[0]}, nome: {supplier[1]}, produto_fornecido: {supplier[2]}, quantia_mensal: {supplier[3]}\n")
if __name__=="__main__":
    root=tk.Tk()
    app=CRUDApp(root)
    root.mainloop()