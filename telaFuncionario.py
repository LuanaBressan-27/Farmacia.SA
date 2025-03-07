import tkinter as tk
from tkinter import messagebox
from Crud_Funcionario import create_user,read_users,update_user,delete_user

class CRUDApp:
    def __init__(self,root):
        self.root = root
        self.root.title("CRUD FUNCIONARIO")

        # Criaçao de WIDGETS 
        self.create_widgets()

    def create_widgets(self):
        #Labels
        tk.Label(self.root,text="Nome:").grid(row=0,column=0)    
        tk.Label(self.root,text="Email:").grid(row=1,column=0) 
        tk.Label(self.root,text="Data_de_nascimento:").grid(row=2,column=0) 
        tk.Label(self.root,text="Ddata de contrato:").grid(row=3,column=0) 
        tk.Label(self.root,text="Telefone:").grid(row=4,column=0)
        tk.Label(self.root,text="Cidade:").grid(row=5,column=0) 
        tk.Label(self.root,text="Estado:").grid(row=6,column=0)
        tk.Label(self.root,text="Bairro:").grid(row=7,column=0)


        tk.Label(self.root,text="User ID(for update/delete)").grid(row=7,column=0)  

        #CRIAR AS CAIXAS PARA DIGITAR OS VALORES
        self.nome_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.data_de_nascimento_entry = tk.Entry(self.root)
        self.data_de_contrato_entry = tk.Entry(self.root)
        self.telefone_entry = tk.Entry(self.root)
        self.cidade_entry = tk.Entry(self.root)
        self.estado_entry = tk.Entry(self.root)
        self.bairro_entry = tk.Entry(self.root)
        self.user_id_entry = tk.Entry(self.root)

        self.nome_entry.grid(row=0,column=1)
        self.email_entry.grid(row=1,column=1)
        self.data_de_nascimento_entry.grid(row=2,column=1)
        self.data_de_contrato_entry.grid(row=3,column=1)
        self.telefone_entry.grid(row=4,column=1)
        self.cidade_entry.grid(row=5,column=1)
        self.estado_entry.grid(row=6,column=1)
        self.bairro_entry.grid(row=7,column=1)
        self.user_id_entry.grid(row=8,column=1)

    #BOTOES DO CRUD
        tk.Button(self.root,text="Criar Registro",command=self.create_user).grid(row=8,column=0,columnspan=1)
        tk.Button(self.root,text="Listar Registro",command=self.create_user).grid(row=8,column=1,columnspan=1)
        tk.Button(self.root,text="Alterar Registro",command=self.create_user).grid(row=9,column=0,columnspan=1)
        tk.Button(self.root,text="Excluir Registro",command=self.create_user).grid(row=9,column=1,columnspan=1)

    def create_user(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        data_de_nascimento = self.data_de_nascimento_entry.get()
        data_de_contrato = self.data_de_contrato_entry.get()
        telefone = self.telefone_entry.get()
        cidade = self.cidade_entry.get()
        estado = self.estado_entry.get()
        bairro = self.bairro_entry.get()
        
        
    
        if nome and email and data_de_nascimento and data_de_contrato and telefone and cidade and estado and bairro:
            create_user(nome,email, data_de_nascimento, data_de_contrato,telefone,cidade,estado,bairro)
            self.nome_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.data_de_nascimento_entry.delete(0,tk.END)
            self.data_de_contrato_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.cidade_entry.delete(0,tk.END)
            self.estado_entry.delete(0,tk.END)
            self.bairro_entry.delete(0,tk.END)
            messagebox.showerror("Success","Funcionario registrado com sucesso")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatórios")
    
    def read_users(self):
        users = read_users()
        self.text_area.delete(1.0,tk.END)
        for user in users:
            self.text_area.insert(tk.END,f"ID: {user[0]},Nome:{user[1]}, Telefone:{user[2]},Email:{user[3]}\n")

    def update_user(self):
        user_id = self.user_id_entry.get()
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        data_de_nascimento = self.data_de_nascimento_entry.get()
        data_de_contrato = self.data_de_contrato_entry.get()
        telefone = self.telefone_entry.get()
        cidade = self.cidade_entry.get()
        estado = self.estado_entry.get()
        bairro = self.bairro_entry.get()

        if user_id and nome and email and data_de_nascimento and data_de_contrato and telefone and cidade and estado and bairro:
            update_user(user_id,nome,email, data_de_nascimento,data_de_contrato,telefone,cidade,estado,bairro)
            self.nome_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.data_de_nascimento_entry.delete(0,tk.END)
            self.data_de_contrato_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.cidade_entry.delete(0,tk.END)
            self.estado_entry.delete(0,tk.END)
            self.bairro_entry.delete(0,tk.END)
            messagebox.showerror("Success","Registro alterado com sucesso")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatórios")

    def delete_user(self):
        user_id = self.user_id_entry .get()
        if user_id:
            delete_user(user_id)
            self.user_id_entry.delete(0,tk.END)
            messagebox.showerror("Success", "Registro excluido com sucesso!")
        else:
            messagebox.showerror("Error", "ID do funcionaio é obrigatoria")

if __name__=="__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
