class Personne:
    def __init__(self, nom):
        self.nom = nom
        self.atribut = "une valeur"

    def __repr__(self):
        return "Personne : nom({})".format(self.nom)

    def __getattr__(self, nom):
        print("pas d'ettaribut {} ici".format(nom))
