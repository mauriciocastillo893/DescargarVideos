import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        # Mostrar un cuadro de diálogo para que el usuario elija la ubicación de descarga
        save_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Video files", "*.mp4")])
        if save_path:
            stream.download(output_path=save_path)
            status_label.config(text="Descarga completa en " + save_path)
        else:
            status_label.config(text="Descarga cancelada")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Crear una ventana de la aplicación
app = tk.Tk()
app.title("Descargador de Videos")

# Obtener el ancho y alto de la pantalla
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Calcular el centro de la pantalla
x_center = (screen_width - 500) // 2  # 500 es el ancho de la ventana
y_center = (screen_height - 300) // 2  # 300 es la altura de la ventana

# Configurar la geometría de la ventana para centrarla
app.geometry(f"500x300+{x_center}+{y_center}")

# Crear un marco (frame) para centrar los elementos dentro de la ventana
frame = ttk.Frame(app)
frame.pack(expand=True, fill='both', padx=20, pady=20)

# Crear una etiqueta y un campo de entrada para la URL
url_label = ttk.Label(frame, text="URL del video:")
url_label2 = ttk.Label(frame, text="Desarrollado por: Mauricio Castillo")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
url_label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
url_entry = ttk.Entry(frame)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Botón para iniciar la descarga
download_button = ttk.Button(frame, text="Descargar", command=download_video)
download_button.grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el estado de la descarga
status_label = ttk.Label(frame, text="")
status_label.grid(row=2, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
app.mainloop()
