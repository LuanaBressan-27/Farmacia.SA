import tkinter as tk
from tkinter import messagebox
from crud_stuff_fornecedores import add_supplier, read_suppliers

class TelaFornecedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Fornecedores")
        self.create_widgets()

    def create_widgets(self):
        # Configurações de layout usando frames
        input_frame = tk.Frame(self.root)
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, padx=10, pady=10)

        text_frame = tk.Frame(self.root)
        text_frame.grid(row=2, column=0, padx=10, pady=10)

        # Labels e campos de entrada
        labels = [
            "Nome", "Email", "Produto Fornecido",
            "Tipo de Transporte", "Cidade", "Estado"
        ]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(input_frame, text=f"{label}:").grid(row=i, column=0, sticky="e", pady=5)
            entry = tk.Entry(input_frame)
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[label.lower().replace(" ", "_")] = entry

        # Botões para operações
        tk.Button(button_frame, text="Adicionar Fornecedor", command=self.add_supplier).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Listar Fornecedores", command=self.list_suppliers).grid(row=0, column=1, padx=5)

        # Área de texto para exibir os fornecedores
        self.text_area = tk.Text(text_frame, height=10, width=80)
        self.text_area.pack()

    def add_supplier(self):
        # Obtém dados dos campos
        fields = {key: entry.get().strip() for key, entry in self.entries.items()}
        
        # Verifica se todos os campos estão preenchidos
        if all(fields.values()):
            try:
                # Chama a função para adicionar o fornecedor
                add_supplier(
                    fields["nome"], fields["email"], fields["produto_fornecido"],
                    fields["tipo_de_transporte"], fields["cidade"], fields["estado"]
                )
                messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")
                self.clear_entries()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar fornecedor: {e}")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    def list_suppliers(self):
        try:
            # Lê todos os fornecedores do banco de dados
            suppliers = read_suppliers()
            self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
            if suppliers:
                # Exibe todos os dados, incluindo "Cidade" e "Estado"
                for supplier in suppliers:
                    self.text_area.insert(
                        tk.END,
                        f"ID: {supplier[0]}, Nome: {supplier[1]}, Email: {supplier[2]}, "
                        f"Produto: {supplier[3]}, Transporte: {supplier[4]}, Cidade: {supplier[5]}, Estado: {supplier[6]}\n"
                    )
            else:
                self.text_area.insert(tk.END, "Nenhum fornecedor encontrado.\n")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao listar fornecedores: {e}")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaFornecedor(root)
    root.mainloop()
