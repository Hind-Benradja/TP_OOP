#q1
class Habitant:
    def __init__(self, nom, age, adresse, animaux=None):
        self.nom=nom
        self.age=age
        self.adresse=adresse
        if animaux is None:
            self.animaux={}
        else:
            self.animaux= animaux
#q2
    def affichage_adresse(self):
        print(f"{self.nom} habite a {self.adresse}")

    def compte_animal(self,animal):
        if animal in self.animaux:
            return self.animaux[animal]
        else:
            return 0


animaux= {"vaches": 3, "moutons": 5}
h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})            
assert h1.nom == "Aldric"


assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() 