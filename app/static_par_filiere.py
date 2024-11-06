import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from matplotlib.ticker import MaxNLocator

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
    SELECT filiere, COUNT(filiere) 
    FROM users u JOIN absence a ON a.id=u.id 
    GROUP BY filiere
""")

list_filiere = []
list_nombre_absences = []

# Ajouter les données dans les listes
for f, ab in cursor.fetchall():
    list_nombre_absences.append(ab)
    list_filiere.append(f)

x = np.array(list_filiere)
y = np.array(list_nombre_absences)

# Liste de couleurs pour chaque filière (modifiable selon le nombre de filières)
colors = plt.cm.viridis(np.linspace(0, 1, len(x)))  # Utilisation d'un gradient de couleurs
# Tracer le graphique
plt.figure(figsize=(10, 6))
bars = plt.bar(x, y, color=colors)
print(bars)

# Ajouter les valeurs en haut de chaque barre
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom', fontsize=15, color='black')

# Ajustement de l'axe Y pour afficher uniquement des valeurs entières
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

# Titre et labels avec couleurs
plt.title("Absences par filière", color='black')  # Titre en noir
plt.xlabel("Filière", fontsize=14, color='red', bbox=dict(facecolor='red', alpha=0.1))  # Couleur rouge pour l'axe X avec fond
plt.ylabel("Total des Absences", fontsize=12, color='green', bbox=dict(facecolor='green', alpha=0.1))  # Couleur verte pour l'axe Y avec fond

# Afficher le graphique
plt.show()

# Fermer la connexion à la base de données
cursor.close()
conn.close()
