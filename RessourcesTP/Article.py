class Article:

    def __init__(self, id, titre, auteur, texte):
        self.__id = id
        self.__titre = titre
        self.__auteur = auteur
        self.__texte = texte

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, titre):
        self.__titre = titre

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, auteur):
        self.__auteur = auteur

    @property
    def texte(self):
        return self.__texte

    @texte.setter
    def texte(self, texte):
        self.__texte = texte

    def serialize(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'auteur': self.auteur,
            'texte': self.texte
        }

