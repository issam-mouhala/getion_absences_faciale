import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host='localhost',  
    user='root',       
    password='',       
    database='mini-project'  
)

cursor = conn.cursor()

# Exécuter la requête pour récupérer les données d'absence
cursor.execute("""
    SELECT absence.date, absence.time, username, filiere
    FROM users
    INNER JOIN absence ON absence.id = users.id
    ORDER BY date, time 
""")

# Initialiser les données pour le tableau
data = []
for date, time, nom, filiere in cursor.fetchall():
    data.append((nom.capitalize(), filiere, date, time))

# Création de la fenêtre principale
root = tk.Tk()
root.title("Liste des étudiants avec avertissements")
root.geometry("1080x540")
title_label = tk.Label(root, text="Informations des absences", font=("Helvetica", 16, "bold"), fg="#333")
title_label.pack(pady=10)  

# Fonction pour filtrer les données en fonction de la recherche par nom
def search_data():
    search_term = search_entry.get().capitalize()
    for row in table.get_children():
        table.delete(row)
    i=0
    for row in data:
        
        if search_term in row[0]:
            i+=1
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            table.insert("", "end", values=row, tags=(tag,))

# Barre de recherche
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
search_label = tk.Label(search_frame, text="Rechercher par nom:", font=("Helvetica", 14))
search_label.pack(side="left")
search_entry = tk.Entry(search_frame, font=("Helvetica", 14))
search_entry.pack(side="left", padx=5)
search_button = tk.Button(search_frame, text="Rechercher", font=("Helvetica", 14), command=search_data)
search_button.pack(side="left")

# Style de la table
style = ttk.Style()
style.configure("Treeview",
                background="#E8E8E8",
                foreground="black",
                rowheight=30,
                fieldbackground="#E8E8E8",
                font=("Helvetica", 18, "italic"))
style.configure("Treeview.Heading", font=("Helvetica", 20, "bold"), foreground="red")
style.map("Treeview", background=[("selected", "#4CAF50")])

# Création de la frame pour la table avec scrollbar
outer_frame = tk.Frame(root, bd=0)
outer_frame.pack(pady=20)

# Barre de défilement verticale
scrollbar = tk.Scrollbar(outer_frame)
scrollbar.pack(side="right", fill="y")

# Définition de la table avec Treeview
table = ttk.Treeview(outer_frame, columns=("Nom", "Filiere", "Date", "Heure"), show="headings", yscrollcommand=scrollbar.set)
scrollbar.config(command=table.yview)

table.heading("Nom", text="Nom")
table.heading("Filiere", text="Filiere")
table.heading("Date", text="Date")
table.heading("Heure", text="Heure")

# Style des colonnes
table.column("Nom", anchor="center", width=250)
table.column("Filiere", anchor="center", width=250)
table.column("Date", anchor="center", width=250)
table.column("Heure", anchor="center", width=250)

# Insertion de données avec lignes alternées
for i, row in enumerate(data):
    tag = "evenrow" if i % 2 == 0 else "oddrow"
    table.insert("", "end", values=row, tags=(tag,))

# Application des couleurs de ligne alternées
table.tag_configure("evenrow", background="#A9A9A9")
table.tag_configure("oddrow", background="#ffffff")

# Ajout de la table dans la frame interne
table.pack()

# Lancement de l'application et fermeture de la connexion après
def on_close():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
