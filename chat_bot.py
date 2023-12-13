import tkinter as tk
from tkinter import ttk
import re
import random
import webbrowser
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password='root',
    db='grupo06'
)
cursor = db.cursor()

def run_chat(usuario):

    def get_response(user_input):
        split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
        response = check_all_messages(split_message)
        return response

    def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
        message_certainty = 0
        has_required_words = True

        for word in user_message:
            if word in recognized_words:
                message_certainty += 1

        percentage = float(message_certainty) / float(len(recognized_words))

        for word in required_word:
            if word not in user_message:
                has_required_words = False
                break
        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def check_all_messages(message):    
        highest_prob = {}

        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)


        cursor.execute("SELECT palabra_clave, respuesta FROM respuestas")
        rows = cursor.fetchall()

        for row in rows:
            keyword, respuesta_db = row 
            keyword_list = keyword.split(',')
            
            keyword_list = [k.strip().lower() for k in keyword_list]

            response(respuesta_db, keyword_list, single_response=True)  

        best_match = max(highest_prob, key=highest_prob.get)

        return unknown() if highest_prob[best_match] < 1 else best_match


    def unknown():
        cursor.execute("SELECT respuesta FROM respuestas WHERE palabra_clave = 'desconocida'")
        desconocida_respuestas = cursor.fetchone()

        if desconocida_respuestas:
            respuestas_desconocidas = desconocida_respuestas[0].split(';')
            respuesta = random.choice(respuestas_desconocidas)
        else:
            respuesta = "Lo siento, ha ocurrido un error."

        return respuesta
 
    def abrir_video_youtube(video_id):
        url = f"https://www.youtube.com/watch?v={video_id}"
        webbrowser.open(url)

    def enviar_mensaje():
        user_input = entrada_texto.get()
        respuesta = get_response(user_input) 
        conversacion.config(state=tk.NORMAL)
        conversacion.insert(tk.END, "Tú : " + user_input + "\n")

        if respuesta == "Ver tus notas":
            abrir_video_youtube("JWrzWkerkxY&t=27s")
            respuesta = "\n Ver tus notas - https://intranet.certus.edu.pe/Login/Login/Portal \n Abriendo video de ayuda..."
        
        if respuesta == "Ver lineamientos":
            abrir_video_youtube("ZibUpdSDQ1E")
            respuesta = "\n Abriendo video de ayuda..."

        conversacion.insert(tk.END, "Sukuna : " + respuesta + "\n", "bot_text")
        conversacion.config(state=tk.DISABLED)
        entrada_texto.delete(0, tk.END)
    
    def cerrar_sesion():
        ventana.destroy()
        
        
    

    # Style
    style = ttk.Style()

    # Configurar el Entry
    style.configure("CustomEntry.TEntry", padding=(5, 5, 5, 5), font=('Helvetica', 12), background='#E6E6FA', foreground='#000000')  # Entry

    # Configurar el botón "Enviar"
    style.configure("Enviar.TButton", padding=(10, 5, 10, 5), font=('Helvetica', 12), background='#4B0082', foreground='white')  # Enviar

    # Configurar el botón "Cerrar Sesión"
    style.configure("CerrarSesion.TButton", padding=(10, 5, 10, 5), font=('Helvetica', 12), background='#4B0082', foreground='white')  # Cerrar Sesión

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("ChatBot")

    # Configurar el área de conversación
    conversacion = tk.Text(ventana, wrap=tk.WORD, bg='#DDA0DD', fg='white', font=('Helvetica', 12), height=10, width=40)  # Texto
    conversacion.pack()

    conversacion.tag_config("bot_text", foreground="white", background="#4B0082")  # Configurar etiquetas

    # Configurar la entrada de texto
    entrada_texto = ttk.Entry(ventana, style="CustomEntry.TEntry", width=30)  # Entry
    entrada_texto.pack()

    # Botón para enviar mensajes
    enviar_boton = ttk.Button(ventana, text="Enviar", command=enviar_mensaje, style="Enviar.TButton")  # Enviar
    enviar_boton.pack(pady=10)

    # Botón para cerrar sesión
    cerrar_sesion_boton = ttk.Button(ventana, text="Cerrar Sesión", command=cerrar_sesion, style="CerrarSesion.TButton")  # Cerrar Sesión
    cerrar_sesion_boton.pack(pady=10)

    # Ejecutar la aplicación
    ventana.mainloop()

