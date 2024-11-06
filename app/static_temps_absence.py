import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host='localhost',  
    user='root',       
    password='',       
    database='mini-project'  
)

cursor = conn.cursor()

# Exécuter la requête pour récupérer les données d'absence par heure
cursor.execute("""
    SELECT time, COUNT(time)
    FROM absence  
    GROUP BY time 
""")
list_time = []
list_nb = []

# Ajouter les données dans les listes
for t, nb in cursor.fetchall():
    list_time.append(t)
    list_nb.append(nb)

# Fermer la connexion à la base de données
conn.close()

# Préparation des données pour le graphique
y = np.array(list_nb)
mylabels = list_time

# Créer le graphique en camembert
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(y, labels=mylabels, autopct='%1.1f%%', startangle=90, 
                                  textprops={'color': 'white', 'bbox': dict(facecolor='black', alpha=0.8, edgecolor='none')})

# Personnaliser les labels de pourcentage
for autotext in autotexts:
    autotext.set_bbox(dict(facecolor='black', edgecolor='none', alpha=0.8))  # Fond noir des pourcentages
    autotext.set_color('white')  # Texte en blanc

# Titre et légende
plt.title("Temps d'absences", color='black')  # Titre en noir
plt.legend(wedges, mylabels, title="Temps", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Afficher le graphique
plt.show()
