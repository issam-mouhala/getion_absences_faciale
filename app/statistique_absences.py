import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
import matplotlib.dates as mdates
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
    SELECT date, COUNT(id) 
    FROM absence  
    WHERE date BETWEEN DATE_SUB(CURDATE(), INTERVAL 7 DAY) AND CURDATE()
    GROUP BY date
    ORDER BY date 
""")

# Initialiser les listes pour les données d'absence et les dates
list_absence = []
list_date = []

# Ajouter les données dans les listes
for date, ab in cursor.fetchall():
    list_absence.append(ab)
    list_date.append(date)

# Fermer la connexion à la base de données
conn.close()

# Tracer le graphique
plt.figure(figsize=(13, 6))

# Tracer les données
plt.plot(list_date, list_absence, marker='o', linestyle='-', color='black', label='Total d\'absences')

# Ajouter des annotations pour chaque point avec la date et le total d'absences
for i, (date, ab) in enumerate(zip(list_date, list_absence)):
    plt.annotate(f"{date.strftime('%Y-%m-%d')}: {ab}", (date, ab), 
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center', fontsize=11, color='white',
                 bbox=dict(facecolor='black', alpha=0.9))  # Fond noir avec transparence

# Formater l'axe des x pour afficher les dates de manière lisible
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gcf().autofmt_xdate()  # Rotation des dates

# Ajustement dynamique de l'axe y
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # Permet des valeurs entières sur l'axe y

# Ajouter un titre et des labels avec couleurs spécifiques
plt.title("Absences au fil du temps", color='black')  # Titre en noir
plt.xlabel("Date", fontsize=12, color='red', bbox=dict(facecolor='red', alpha=0.1))  # Couleur rouge pour l'axe x avec fond
plt.ylabel("Total des Absences", fontsize=12, color='green', bbox=dict(facecolor='green', alpha=0.1))  # Couleur verte pour l'axe y avec fond

# Afficher la légende
plt.legend()

# Afficher le graphique
plt.show()
