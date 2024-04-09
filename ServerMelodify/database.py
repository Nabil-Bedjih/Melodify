# database.py
import psycopg2
from psycopg2.extras import RealDictCursor

class DatabaseConnection:
    def __init__(self, dbname, user, password, host, port):
        self.connexion_params = {
            "dbname": dbname,
            "user": user,
            "password": password,
            "host": host,
            "port": port
        }
        self.connexion = None

    def ouvrir_connexion(self):
        try:
            self.connexion = psycopg2.connect(**self.connexion_params, cursor_factory=RealDictCursor)
            return self.connexion
        except psycopg2.Error as e:
            print(f"Erreur lors de la connexion à la base de données: {e}")
            return None

    def fermer_connexion(self):
        if self.connexion:
            self.connexion.close()
