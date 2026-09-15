#question 1

pieces_stock = {
    "ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
    "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(dictio, modele, piece):
    result = dictio[modele][piece]
    return result
assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

#question 2

def consommer_piece(dictio, modele, piece, quantite):
    result= dictio[modele][piece] - quantite
    return result

def ajouter_modele(pieces_stock, modele,moteurs=0, capteurs=0, roues=0):
    pieces_stock[modele] = {"moteurs":moteurs, "capteurs": capteurs, "roues": roues}
    return pieces_stock

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
#assert(pieces_stock["ModeleA"]["moteurs"]) == 7

ajouter_modele(pieces_stock, "ModeleC", moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == {"moteurs": 4, "capteurs": 10, "roues": 16}

def total_pieces(pieces_stock):
    pieces_stock[modele] = {"moteurs": moteurs, "capteurs": capteurs, "roues": roues}
    for modele in pieces_stock:
        if mot not in somme:
            somme[mot] = pieces_stock[modele][mot]
        else:
            somme[mot] = somme[mot] + pieces_stock[modele][mot]
    return somme
    
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}