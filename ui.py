import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from bgRemover import remove_background

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        input_label.config(text=file_path)

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        output_label.config(text=file_path)

def process_image():
    input_path = input_label.cget("text")
    output_path = output_label.cget("text")
    if input_path and output_path:
        remove_background(input_path, output_path)

root = tk.Tk()
root.title("Background Remover")
root.geometry("400x300")

# Usamos ttk para estilizar
style = ttk.Style()
style.configure("TButton", padding=6, background="#000", foreground="black",round=20 )

style.configure("TLabel", font=("Arial", 10))




tk.Label(root, text="Input Image:").pack(pady=10)

input_label = tk.Label(root, text="")
input_label.pack(pady=5)
 

# Botón para seleccionar imagen
select_button = ttk.Button(root, text="Select Input Image", command=select_image)
select_button.pack(pady=10)


tk.Label(root, text="Output Image:").pack()
output_label = tk.Label(root, text="")
output_label.pack()
tk.Button(root, text="Save Output Image As", command=save_image).pack()





# Botón para procesar la imagen
remove_button = ttk.Button(root, text="Remover Fondo", command=process_image)
remove_button.pack(pady=10)

# Ejecutar el loop principal de la ventana
root.mainloop()
