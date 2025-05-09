from tkinter import *
from tkinter import ttk
from DataBase import Database  # Certifique-se de que este módulo está correto
from tkinter import messagebox


# Tela de login
jan = Tk()
jan.title("Login de Usuários")
jan.geometry("600x300")
jan.configure(background="purple")
jan.resizable(width=False, height=False)

Titulo = Label(jan, text="Login:", font=("Century Gothic", 25), bg="red", fg="White")
Titulo.place(x=1, y=50)

# Adicionar campos de usuário e senha
usuarioLabel = Label(jan, text="Usuário: ", font=("Century Gothic", 10), bg="ORANGE", fg="White")
usuarioLabel.place(x=1, y=125)
usuarioEntry = ttk.Entry(jan, width=30)
usuarioEntry.place(x=60, y=125)

senhaLabel = Label(jan, text="Senha: ", font=("Century Gothic", 10), bg="ORANGE", fg="White")
senhaLabel.place(x=1, y=155)
senhaEntry = ttk.Entry(jan, width=30, show="*")  # Oculte a senha com "*"
senhaEntry.place(x=55, y=155)


# Função de login
def Login():
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

    # Conectar ao banco de dados
    try:
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        # Consulta para verificar as credenciais
        cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND senha = %s", (usuario, senha))
        VerifiyLogin = cursor.fetchone()

        if VerifiyLogin:
            messagebox.showinfo(title="Info Login", message="Acesso Confirmado. Bem-vindo!")
        else:
            messagebox.showinfo(title="Info Login", message="Acesso Negado. Verifique se o cadastro está no sistema.")

    except Exception as e:
        messagebox.showerror(title="Erro de Conexão", message=f"Ocorreu um erro: {e}")

    finally:
        # Fecha a conexão com o banco
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


# Função para registrar novo usuário
def registrar():
    # Remover botões de Login
    LoginButton.place_forget()
    RegisterButton.place_forget()

    # Inserir widgets de cadastro
    NomeLabel = Label(jan, text="Nome:", font=("Century Gothic", 10), bg="orange", fg="White")
    NomeLabel.place(x=250, y=125)
    NomeEntry = ttk.Entry(jan, width=30)
    NomeEntry.place(x=305, y=125)

    EmailLabel = Label(jan, text="Email:", font=("Century Gothic", 10), bg="orange", fg="White")
    EmailLabel.place(x=250, y=155)
    EmailEntry = ttk.Entry(jan, width=30)
    EmailEntry.place(x=305, y=155)

    # Função para registrar no banco de dados
    def RegistrarNoBanco():
        nome = NomeEntry.get()
        email = EmailEntry.get()
        usuario = usuarioEntry.get()
        senha = senhaEntry.get()

        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de Registro", message="Preencha todos os campos!")
        else:
            try:
                db = Database()
                conn = db.get_connection()
                cursor = conn.cursor()

                # Verificar se o usuário já existe
                cursor.execute("SELECT * FROM usuario WHERE usuario = %s", (usuario,))
                VerifiyLogin = cursor.fetchone()
                if VerifiyLogin:
                    messagebox.showerror(title="Erro de Registro", message="Usuário já cadastrado!")
                else:
                    # Inserir novo usuário
                    cursor.execute("INSERT INTO usuario (nome, email, usuario, senha) VALUES (%s, %s, %s, %s)",
                                   (nome, email, usuario, senha))
                    conn.commit()
                    messagebox.showinfo(title="Registro", message="Usuário registrado com sucesso!")

                    # Limpar campos após o registro
                    NomeEntry.delete(0, END)
                    EmailEntry.delete(0, END)
                    usuarioEntry.delete(0, END)
                    senhaEntry.delete(0, END)

            except Exception as e:
                messagebox.showerror(title="Erro de Conexão", message=f"Ocorreu um erro: {e}")

            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()

    Register = ttk.Button(jan, text="Registrar", width=15, command=RegistrarNoBanco)
    Register.place(x=150, y=225)

    # Função para voltar à tela de login
    def VoltarLogin():
        NomeLabel.place_forget()
        NomeEntry.place_forget()
        EmailLabel.place_forget()
        EmailEntry.place_forget()
        Register.place_forget()
        Voltar.place_forget()

        # Trazer de volta os widgets de login
        LoginButton.place(x=150,y=180)
        RegisterButton.place(x=300,y=180)

    Voltar = ttk.Button(jan, text="Voltar", width=15, command=VoltarLogin)
    Voltar.place(x=300, y=225)


# Botões principais
LoginButton = ttk.Button(jan, text="Login", width=15, command=Login)
LoginButton.place(x=150, y=180)

RegisterButton = ttk.Button(jan, text="Registrar", width=15, command=registrar)
RegisterButton.place(x=300, y=180)
jan.mainloop()