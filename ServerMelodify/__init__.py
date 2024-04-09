from database import DatabaseConnection
from dao import DAO
import psycopg2

# Paramètres de connexion à la base de données
url = "pedago.univ-avignon.fr"
dbname = "etd"  # Nom de la base de données
user = "uapv2200700"  # Votre nom d'utilisateur
password = "kDfUsr"  # Votre mot de passe

# Chaîne de connexion
connexion_string = f"host={url} dbname={dbname} user={user} password={password}"

try:
    # Utiliser psycopg2 pour établir une connexion
    db_connexion = psycopg2.connect(connexion_string)

    if db_connexion:
        dao = DAO(db_connexion)

        # Insérer de nouvelles données
        #dao.inserer({'musicname': 'cfigh'})

        # Obtenir des données

        # Mettre à jour des données
        #dao.mettre_a_jour(1, {'musicname': 'nezga'})

        # Supprimer des données
        dao.supprimer(1)
        print(dao.obtenir(1))


except psycopg2.Error as e:
    print(f"Erreur lors de la connexion à la base de données: {e}")
finally:
    # Fermeture de la connexion à la base de données
    if db_connexion:
        db_connexion.close()
