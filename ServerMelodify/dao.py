# dao.py
class DAO:
    def __init__(self, connexion):
        self.connexion = connexion

    def inserer(self, donnees):
        with self.connexion.cursor() as cur:
            cur.execute(
                "INSERT INTO music (musicname) VALUES (%s)",
                (donnees['musicname'],)
            )
            self.connexion.commit()

    def obtenir(self, id):
        with self.connexion.cursor() as cur:
            cur.execute("SELECT * FROM music WHERE id = %s", (id,))
            return cur.fetchone()

    def mettre_a_jour(self, id, nouvelles_donnees):
        with self.connexion.cursor() as cur:
            cur.execute(
                "UPDATE music SET musicname = %s WHERE id = %s",
                (nouvelles_donnees['musicname'], id)
            )
            self.connexion.commit()

    def supprimer(self, id):
        with self.connexion.cursor() as cur:
            cur.execute("DELETE FROM music WHERE id = %s", (id,))
            self.connexion.commit()
