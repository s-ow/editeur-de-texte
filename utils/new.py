from tkinter import *
from tkinter import filedialog, ttk, messagebox

def new(text):
    if text.get("1.0", "end-1c"):
        resultat = messagebox.showwarning("Avertissement", "Êtes-vous sûr de vouloir effacer ? Aucune sauvegarde ne sera faite.", type=messagebox.OKCANCEL)
        if resultat == "ok":
            text.delete('1.0', 'end')
        if resultat == "cancel":
            pass
    else:
        text.delete('1.0', 'end')