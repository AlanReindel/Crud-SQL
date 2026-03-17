import tkinter as tk
import mysql.connector


class App:

    # construtor da classe
    def __init__(self, root):

        self.root = root
        self.root.title("CRUD Usuários")

        # campos
        tk.Label(root, text="Nome").grid(row=0, column=0)
        self.nome = tk.Entry(root)
        self.nome.grid(row=0, column=1)

        tk.Label(root, text="Email").grid(row=1, column=0)
        self.email = tk.Entry(root)
        self.email.grid(row=1, column=1)

        tk.Label(root, text="Endereço").grid(row=2, column=0)
        self.endereco = tk.Entry(root)
        self.endereco.grid(row=2, column=1)

        tk.Label(root, text="ID").grid(row=3, column=0)
        self.id = tk.Entry(root)
        self.id.grid(row=3, column=1)

        # botões
        tk.Button(root, text="Criar", command=self.create_user).grid(row=4, column=0)
        tk.Button(root, text="Listar", command=self.read_users).grid(row=4, column=1)
        tk.Button(root, text="Atualizar", command=self.update_user).grid(row=5, column=0)
        tk.Button(root, text="Deletar", command=self.delete_user).grid(row=5, column=1)

        # área de resultado
        self.texto = tk.Text(root, height=10, width=40)
        self.texto.grid(row=6, column=0, columnspan=2)

    # conexão com banco
    def conectar(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_usuario"
        )

    # CREATE
    def create_user(self):

        nome = self.nome.get()
        email = self.email.get()
        endereco = self.endereco.get()

        con = self.conectar()
        cursor = con.cursor()

        sql = "INSERT INTO usuarios (nome,email,endereco) VALUES (%s,%s,%s)"
        valores = (nome, email, endereco)

        cursor.execute(sql, valores)

        con.commit()

        self.texto.insert(tk.END, "Usuário criado\n")

        con.close()

    # READ
    def read_users(self):

        con = self.conectar()
        cursor = con.cursor()

        cursor.execute("SELECT * FROM usuarios")

        dados = cursor.fetchall()

        self.texto.delete(1.0, tk.END)

        for linha in dados:
            self.texto.insert(tk.END, str(linha) + "\n")

        con.close()

    # UPDATE
    def update_user(self):

        id_usuario = self.id.get()
        nome = self.nome.get()
        email = self.email.get()

        con = self.conectar()
        cursor = con.cursor()

        sql = "UPDATE usuarios SET nome=%s,email=%s WHERE id=%s"
        valores = (nome, email, id_usuario)

        cursor.execute(sql, valores)

        con.commit()

        self.texto.insert(tk.END, "Usuário atualizado\n")

        con.close()

    # DELETE
    def delete_user(self):

        id_usuario = self.id.get()

        con = self.conectar()
        cursor = con.cursor()

        sql = "DELETE FROM usuarios WHERE id=%s"

        cursor.execute(sql, (id_usuario,))

        con.commit()

        self.texto.insert(tk.END, "Usuário deletado\n")

        con.close()


# inicia aplicação
root = tk.Tk()
app = App(root)
root.mainloop()