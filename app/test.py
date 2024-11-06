import tkinter as tk
from tkinter import messagebox
import app,static_par_filiere,static_temps_absence,liste_absence,statistique_absences
# Fonction de commande pour chaque bouton
def start_recognition():
    app

def save_absence():
    statistique_absences

def show_absences():
    liste_absence

def show_absence_by_filiere():
    static_par_filiere

def show_absence_by_time():
    static_temps_absence

# Création de la fenêtre principale
root = tk.Tk()
root.title("Menu Principal")
root.geometry("500x500")
root.configure(bg="#2E2E2E")  # Couleur de fond sombre

# Style des boutons
button_style = {"font": ("Arial", 12, "bold"), "bg": "#00A2E8", "fg": "white", "relief": tk.FLAT}

# Fonction pour l'effet de survol
def on_enter(e):
    e.widget["bg"] = "#005f99"  # Couleur plus foncée au survol

def on_leave(e):
    e.widget["bg"] = "#00A2E8"  # Couleur d'origine

# Création des boutons avec effet de survol
btn_start_recognition = tk.Button(root, text="Lancer la reconnaissance faciale", command=start_recognition, **button_style)
btn_start_recognition.bind("<Enter>", on_enter)
btn_start_recognition.bind("<Leave>", on_leave)

btn_save_absence = tk.Button(root, text="Enregistrer les absences", command=save_absence, **button_style)
btn_save_absence.bind("<Enter>", on_enter)
btn_save_absence.bind("<Leave>", on_leave)

btn_show_absences = tk.Button(root, text="Afficher la liste des absences", command=show_absences, **button_style)
btn_show_absences.bind("<Enter>", on_enter)
btn_show_absences.bind("<Leave>", on_leave)

btn_show_absence_by_filiere = tk.Button(root, text="Absences par filière", command=show_absence_by_filiere, **button_style)
btn_show_absence_by_filiere.bind("<Enter>", on_enter)
btn_show_absence_by_filiere.bind("<Leave>", on_leave)

btn_show_absence_by_time = tk.Button(root, text="Absences par tranche horaire", command=show_absence_by_time, **button_style)
btn_show_absence_by_time.bind("<Enter>", on_enter)
btn_show_absence_by_time.bind("<Leave>", on_leave)

# Titre du menu
title_label = tk.Label(root, text="Gestion des Absences", font=("Helvetica", 18, "bold"), fg="white", bg="#2E2E2E")
title_label.pack(pady=(20, 10))

# Placement des boutons dans la fenêtre
btn_start_recognition.pack(pady=10, ipadx=20, ipady=10)
btn_save_absence.pack(pady=10, ipadx=20, ipady=10)
btn_show_absences.pack(pady=10, ipadx=20, ipady=10)
btn_show_absence_by_filiere.pack(pady=10, ipadx=20, ipady=10)
btn_show_absence_by_time.pack(pady=10, ipadx=20, ipady=10)

# Boucle principale de Tkinter
root.mainloop()
