from ex4 import Habitant


class Village: 
    def __init__(self,nom):
        self.nom=nom
        self.habitants=[]
    
    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):        
        self.habitants.append(Habitant(nom, age, adresse, animaux))

    def ajouter_habitant_agregation(self, habitant):
        self.habitants.append(habitant)

    def afficher_habitants(self):
        for habitant in self.habitants:
            print(f"{habitant.get_nom()}")

    def get_habitants(self):
        return self.habitants

pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})

elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)

autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages

assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()

#q3 
#ajouter_habitant_agregation illustre une relation d’agrégation car si Village est supprimé, Habitant existera toujours, tandis 
#que ajouter_habitant_composition illustre une relation de composition car si Village est supprimé, alors Habitant aussi, il n'existera plus.