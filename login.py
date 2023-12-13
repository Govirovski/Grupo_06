from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector 
from mysql.connector import Error
import chat_bot 

#----------------- conexion y funciones  ---------------------------

def abrir_ventana_crud():
    ventana_crud = Toplevel(root)
    ventana_crud.title("CRUD de Usuarios")


    def crear_usuario():
        usuario = usuario_entry.get()
        contraseña = contraseña_entry.get()

        if not usuario or not contraseña:
            messagebox.showerror("Error de registro", "Por favor, ingrese un correo y una contraseña.")
            return
        

        mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password='root',
            db='grupo06'
        )

        mycursor = mydb.cursor()

        query = "INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)"
        values = (usuario, contraseña)

        try:
            mycursor.execute(query, values)
            mydb.commit()
            messagebox.showinfo("Registro exitoso", "¡Usuario {} creado con éxito.".format(usuario))
            limpiar_campos()
        except mysql.connector.IntegrityError as err:
            if "Duplicate entry" in str(err):
                messagebox.showerror("Error de registro", "El correo electrónico ya está registrado.")
            else:
                messagebox.showerror("Error de registro", "Error: {}".format(err))

        mydb.close()


    def mostrar_usuarios():
        mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password='root',
            db='grupo06'
        )

        mycursor = mydb.cursor()

        query = "SELECT correo FROM usuarios"

        mycursor.execute(query)
        usuarios = mycursor.fetchall()

        if usuarios:
            messagebox.showinfo("Usuarios", "Usuarios registrados:\n\n{}".format("\n".join([user[0] for user in usuarios])))
        else:
            messagebox.showinfo("Usuarios", "No hay usuarios registrados.")

        mydb.close()


    def actualizar_usuario():
        usuario = usuario_entry.get()
        nueva_contraseña = nueva_contraseña_entry.get()

        mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password='root',
            db='grupo06'
        )

        mycursor = mydb.cursor()

        query = "SELECT correo FROM usuarios"
        mycursor.execute(query)
        usuarios = mycursor.fetchall()

        if not usuarios:
            messagebox.showinfo("Error de actualización", "No hay usuarios registrados.")
            mydb.close()
            return

        query = "UPDATE usuarios SET contraseña = %s WHERE correo = %s"
        values = (nueva_contraseña, usuario)


        try:
            mycursor.execute(query, values)
            mydb.commit()
            messagebox.showinfo("Actualización exitosa", "Contraseña de {} actualizada con éxito.".format(usuario))
            limpiar_campos()
        except mysql.connector.Error as err:
            messagebox.showerror("Error de actualización", "Error: {}".format(err))

        mydb.close()


    def eliminar_usuario():
        usuario = usuario_entry.get()

        mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password='root',
            db='grupo06'
        )

        mycursor = mydb.cursor()

        query = "SELECT correo FROM usuarios"
        mycursor.execute(query)
        usuarios = mycursor.fetchall()

        if not usuarios:
            messagebox.showinfo("Error de eliminación", "No hay usuarios registrados.")
            mydb.close()
            return

        query = "DELETE FROM usuarios WHERE correo = %s"
        values = (usuario,)

        try:
            mycursor.execute(query, values)
            mydb.commit()
            messagebox.showinfo("Eliminación exitosa", "Usuario {} eliminado con éxito.".format(usuario))
            limpiar_campos()
        except mysql.connector.Error as err:
            messagebox.showerror("Error de eliminación", "Error: {}".format(err))

        mydb.close()



    usuario_entry = Entry(ventana_crud, textvariable=StringVar())
    usuario_entry.grid(row=0, column=1, padx=10, pady=10)

    contraseña_entry = Entry(ventana_crud, show="*", textvariable=StringVar())
    contraseña_entry.grid(row=1, column=1, padx=10, pady=10)

    nueva_contraseña_entry = Entry(ventana_crud, show="*", textvariable=StringVar())
    nueva_contraseña_entry.grid(row=2, column=1, padx=10, pady=10)


    usuario_label = Label(ventana_crud, text="Correo:")
    usuario_label.grid(row=0, column=0, sticky='e', padx=10, pady=10)

    contraseña_label = Label(ventana_crud, text="Contraseña:")
    contraseña_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)

    nueva_contraseña_label = Label(ventana_crud, text="Nueva Contraseña:")
    nueva_contraseña_label.grid(row=2, column=0, sticky='e', padx=10, pady=10)

    
    crear_usuario_button = Button(ventana_crud, text="Crear Usuario", command=crear_usuario)
    crear_usuario_button.grid(row=3, column=0, padx=10, pady=10)

    mostrar_usuarios_button = Button(ventana_crud, text="Mostrar Usuarios", command=mostrar_usuarios)
    mostrar_usuarios_button.grid(row=3, column=1, padx=10, pady=10)

    actualizar_usuario_button = Button(ventana_crud, text="Actualizar Contraseña", command=actualizar_usuario)
    actualizar_usuario_button.grid(row=4, column=0, padx=10, pady=10)

    eliminar_usuario_button = Button(ventana_crud, text="Eliminar Usuario", command=eliminar_usuario)
    eliminar_usuario_button.grid(row=4, column=1, padx=10, pady=10)

    ventana_crud.mainloop()



def verificar_login():
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()

    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password='root',
        db='grupo06'
    )

    mycursor = mydb.cursor()

    query = "SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s"
    values = (usuario, contraseña)
    

    mycursor.execute(query, values)
    resultado = mycursor.fetchone()

    if resultado:
        messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido, {}!".format(usuario))
        limpiar_campos()
        

        chat_bot.run_chat(usuario)
    else:
        messagebox.showerror("Error de inicio de sesión", "Correo o contraseña incorrectos")

    mydb.close()


def registrar():
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()

    if not usuario or not contraseña:
        messagebox.showerror("Error de registro", "Por favor, ingrese un correo y una contraseña.")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password='root',
        db='grupo06'
    )

    mycursor = mydb.cursor()

    query = "INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)"
    values = (usuario, contraseña)

    try:
        mycursor.execute(query, values)
        mydb.commit()
        messagebox.showinfo("Registro exitoso", "¡Bienvenido, {}!".format(usuario))
        limpiar_campos()
    except mysql.connector.IntegrityError as err:
        if "Duplicate entry" in str(err):
            messagebox.showerror("Error de registro", "El correo electrónico ya está registrado.")
        else:
            messagebox.showerror("Error de registro", "Error: {}".format(err))

    mydb.close()


def salir_app():
    valor = messagebox.askquestion("Salir", "¿Deseas Salir?")
    if valor == "yes":
        root.destroy()


def limpiar_campos():
    usuario_entry.set("")
    contraseña_entry.set("")


def licencia():

        messagebox.showinfo("Licencia", """----------Creado por-----------
                            \nLos Lederes 
                            \nGrupo 6
                            \n------------------------------------""")


# interfaz
# style
primary_color = "#3498db"  # Blue
secondary_color = "#2ecc71"  # Green
background_color = "#ecf0f1"  # Light Gray
text_color = "#2c3e50"  # Dark Gray

#-------------------- root -----------------------

root = Tk()
root.title("Inicio de sesión")
root.configure(bg=background_color)

#-------------------- barra menu-----------------------

barraMenu=Menu(root)
root.config(menu=barraMenu)
root.geometry("300x300") 


ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=licencia)
ayudaMenu.add_command(label="Acerda de...", command=licencia)

barraMenu.add_command(label="Salir", command=salir_app)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)

#-------------------- comienzo de entry----------------------

miFrame = Frame(root, bg=background_color)
miFrame.pack()

usuario_entry = StringVar()
contraseña_entry = StringVar()

cuadro_user = Entry(miFrame, textvariable=usuario_entry, bg=background_color)
cuadro_user.grid(row=0, column=1, padx=10, pady=10)

cuadro_contraseña = Entry(miFrame, show="*", textvariable=contraseña_entry, bg=background_color)
cuadro_contraseña.grid(row=1, column=1, padx=10, pady=10)

#------------------- label ------------------------------

contraseña_label = Label(miFrame, text="Correo :", bg=background_color, fg=text_color)
contraseña_label.grid(row=0, column=0, sticky='e', padx=10, pady=10)

usuario_label = Label(miFrame, text="Contraseña:", bg=background_color, fg=text_color)
usuario_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)

#------------------- botones ------------------------------

iniciar_sesion_button = ttk.Button(root, text="Iniciar Sesión", command=verificar_login, style='TButton', cursor="hand2")
iniciar_sesion_button.pack(pady=10)

crear_usuario_button = ttk.Button(root, text="Registrarse", command=registrar, style='TButton', cursor="hand2")
crear_usuario_button.pack(pady=10)

crud_button = ttk.Button(root, text="Abrir CRUD", command=abrir_ventana_crud, style='TButton', cursor="hand2")
crud_button.pack(pady=10)

# abrir_chat_button = Button(root, text="Abrir ChatBot", command=abrir_ventana_chat)
# abrir_chat_button.pack(pady=10)

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc")

#------------------ cierre programa------------------------

root.mainloop()