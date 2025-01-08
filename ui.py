import tkinter as tk
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

tk.Label(root, text="Input Image:").pack()
input_label = tk.Label(root, text="")
input_label.pack()
tk.Button(root, text="Select Input Image", command=select_image).pack()

tk.Label(root, text="Output Image:").pack()
output_label = tk.Label(root, text="")
output_label.pack()

tk.Button(root, text="Remove Background", command=process_image).pack()
tk.Button(root, text="Save Output Image As", command=save_image).pack()


root.mainloop()
