#q1
class Habitant:
    def __init__(self,nom,age,adresse,animaux=None):
        self.__nom= nom
        self.__age= age
        self.__adresse = adresse
        if animaux is None:
            self.__animaux={}
        else:
            self.__animaux= animaux

    def get_nom(self) ->str: 
        return self.__nom
    def get_age(self) ->int:
        return self.__age
    def get_adresse(self) ->str:
        return self.__adresse
    def get_animaux(self) ->dict:
        return self.__animaux
        
    def set_nom(self, nom:str):
        self.__nom=nom
    def set_age(self, age:int):
        self.__age=age
    def set_adresse(self, adresse:str):
        self.__adresse=adresse
    def set_animaux(self, animaux:dict):
        self.__animaux=animaux

    def affichage_adresse(self):
        print(f"{self.__nom} habite a {self.__adresse}")

    def compte_animal(self,animal):
        if animal in self.__animaux:
            return self.__animaux[animal]
        else:
            return 0    
    #q2
    @property 
    def age(self):
        return self.__age
        
    @age.setter
    def age(self, age:int):
        self.__age=age
        if age<0:
            raise ValueError("une ValueError aurait du etre levee")

animaux= {"vaches": 3, "moutons": 5}
h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})    
h1.age = 26
assert h1.age == 26
h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass