#question 1

releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(tup) :
    a, b, c = tup
    resultat = f"Capteur {a} : {b} {c}"
    return resultat

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

#question 2

def recalibrer(releves, mot, num):
    nouveaux_releves=[]
    for releve in releves:
        a, b, c = releve
        if a == mot:
            temp= (a, num, c)
            nouveaux_releves.append(temp)
        else:
            nouveaux_releves.append(releve)
        
    return nouveaux_releves
nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

assert nouveaux_releves[0]== ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3

