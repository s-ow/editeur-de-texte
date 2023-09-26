from tkinter import *
from tkinter import filedialog

def ouvrir(text):
    file = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])

    with open(file, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        
    text.delete('1.0', 'end')
    text.insert('1.0', contenu)