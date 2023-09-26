from tkinter import *
from tkinter import filedialog, ttk


def save(text):
    texte = text.get("1.0", "end-1c")

    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")], initialfile="Sans titre.txt")

    file = open(path, "w+")
    file.write(texte)
    file.close()