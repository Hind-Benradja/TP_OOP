from multipledispatch import dispatch

from abc import ABC, abstractmethod
class Habitant(ABC):
    def __init__(self, nom, prenom, age, adresse):
        self.nom= nom
        self.prenom= prenom
        self.age= age
        self.adresse= adresse

    #ex8.1 
    def __str__(self):
        return f"{self.nom}, {self.age} ans, habite a {self.adresse}"
    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        pass

try: 
    h1= Habitant("Elise", "Aldric",21, "Rue A")
    assert False, "uneTypeError aurait dû être levée !"
except TypeError:
    print("Succès : Il est bien impossible d'instancier Habitant directement.")

#q3
class Adulte(Habitant):
    @dispatch(str, str, int, str)
    def __init__(self, nom, prenom, age, adresse):
        if age<18:
            raise ValueError("Un adulte doit avoir au moins 18 ans.")
        super().__init__(nom, prenom, age, adresse)

    @dispatch(str, int, str)
    def __init__(self, nom, age, adresse):
        if age<18:
            raise ValueError("Un adulte doit avoir au moins 18 ans.")
        super().__init__(nom, "", age, adresse)
    def calcul_nombre_annee_avant_retraite(self):
        if self.age >= 62:
            return f"Deja a la retraite"
        else:
            return 62 - self.age
    

        
class Enfant(Habitant):
    @dispatch(str, int, str)
    def __init__(self,nom,age, adresse):
        if age >=18:
            raise ValueError("Un enfant doit avoir moins de 18 ans.")
        super().__init__(nom, "", age, adresse)

    @dispatch(str, str, int, str)
    def __init__(self,nom,prenom,age, adresse):
        if age >=18:
            raise ValueError("Un enfant doit avoir moins de 18 ans.")
        super().__init__(nom, prenom, age, adresse,)

    def calcul_nombre_annee_avant_retraite(self):
            return f"Erreur: un enfant ne peut pas calculer sa retraite"
#ex8.2
def affichage(hab: Habitant):
    print(str(hab))



adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant = Enfant("Martin", "Lucas", 12, "Rue B")
print(adulte)
assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()

try:
    Enfant("Oups", 25, "Rue C")
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass