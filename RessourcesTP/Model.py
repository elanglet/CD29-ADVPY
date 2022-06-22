from typing import List

from RESTModel.Article import Article


class Model:

    __instance = None

    def __init__(self):
        self.__articles = [
            Article(1, "Java 18", "Robert DUPONT", "Java 18 est sorti, et il est passionnant !"),
            Article(2, "Flask", "Etienne LANGLET", "Savez-vous utiliser Flask pour construire des REST REST ?")
        ]

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Model()
        return cls.__instance

    def rechercher_tous_les_articles(self) -> List[Article]:
        return self.__articles

    def rechercher_article_par_id(self, id: int):
        return list(filter(lambda a: a.id == id, self.__articles))[0]

    def ajouter_article(self, article: Article) -> int:
        article.id = len(self.__articles) + 1
        self.__articles.append(article)
        return article.id
