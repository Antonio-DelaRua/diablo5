import tkinter as tk
from PIL import ImageTk, Image

class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 100
        self.hambre = 100
        
    def alimentar(self):
        self.felicidad += 10
        self.hambre += 10
        
        if self.felicidad > 100:
            self.felicidad = 100
        if self.hambre > 100:
            self.hambre = 100
        
        self.actualizar_etiquetas()
        
    def jugar(self):
        self.felicidad += 20
        self.hambre -= 10
        
        if self.felicidad > 100:
            self.felicidad = 100
        if self.hambre < 0:
            self.hambre = 0
        
        self.actualizar_etiquetas()
        
    def dormir(self):
        self.felicidad -= 10
        
        if self.felicidad < 0:
            self.felicidad = 0
        
        self.actualizar_etiquetas()
        
    def disminuir_felicidad_hambre(self):
        self.felicidad -= 5
        self.hambre -= 5
        
        if self.felicidad < 0:
            self.felicidad = 0
        if self.hambre < 0:
            self.hambre = 0
        
        self.actualizar_etiquetas()
        
    def actualizar_etiquetas(self):
        etiqueta_felicidad.config(text="Felicidad: " + str(self.felicidad))
        etiqueta_hambre.config(text="Hambre: " + str(self.hambre))
        ventana.update_idletasks()
        
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mascota Virtual")

# Crear una instancia de la mascota
mascota = MascotaVirtual("Luna")

# Cargar la imagen de la silueta del gato
imagen_gato = Image.open("cat.png")
imagen_gato = imagen_gato.resize((200, 200))  # Ajusta el tamaño de la imagen según tus necesidades
imagen_gato = ImageTk.PhotoImage(imagen_gato)

# Crear un componente Label para mostrar la imagen del gato
etiqueta_gato = tk.Label(ventana, image=imagen_gato)
etiqueta_gato.pack()

# Crear etiquetas para mostrar el estado de la mascota
etiqueta_nombre = tk.Label(ventana, text="Nombre: " + mascota.nombre)
etiqueta_nombre.pack()

etiqueta_felicidad = tk.Label(ventana, text="Felicidad: " + str(mascota.felicidad))
etiqueta_felicidad.pack()

etiqueta_hambre = tk.Label(ventana, text="Hambre: " + str(mascota.hambre))
etiqueta_hambre.pack()

# Crear botones para interactuar con la mascota
boton_alimentar = tk.Button(ventana, text="Alimentar", command=mascota.alimentar)
boton_alimentar.pack()

boton_jugar = tk.Button(ventana, text="Jugar", command=mascota.jugar)
boton_jugar.pack()

boton_dormir = tk.Button(ventana, text="Dormir", command=mascota.dormir)
boton_dormir.pack()

# Iniciar un temporizador para disminuir la felicidad y el hambre cada segundo
ventana.after(1000, mascota.disminuir_felicidad_hambre)

# Ejecutar la ventana principal
ventana.mainloop()
