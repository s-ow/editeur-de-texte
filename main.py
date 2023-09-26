from utils.libs import *

"""
variables et commandes simples ============================================================
"""

bg = "#414853"

def quitter():
    window.quit()
def scroll_text(*args):
    text.yview(*args) 

window = Tk()
window.configure(background=bg)
window.title("Text Editor by s-ow")
window.iconbitmap("utils/icon.ico")

"""
Barre de menu ==============================================================================
"""

menu = Menu(window)
window.config(menu=menu)

menu_fichier = Menu(menu, tearoff=0)
menu.add_cascade(label="Fichier", menu=menu_fichier)

menu_fichier.add_command(label="Ouvrir", command=lambda:ouvrir(text))
menu_fichier.add_command(label="Nouveau", command=lambda:new(text))
menu_fichier.add_separator()
menu_fichier.add_command(label="Enregistrer", command=lambda:save(text))
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=quitter)

"""
Le reste ==============================================================================
"""

text = Text(window, background=bg, fg="white")
text.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)

window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

"""
scrollbar =============================================================================
"""

scrollbar = Scrollbar(window, command=text.yview)
scrollbar.grid(column=1, row=0, sticky="ns")

text.config(yscrollcommand=scrollbar.set)

window.mainloop()