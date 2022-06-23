# My robot aspirator

def calculDeLaSurfaceANettoyer(listeZones):
    surfaceANettoyer = 0
    for zone in listeZones:
        longueur = zone.get("longueur") / 100
        largeur = zone.get("largeur") / 100
        calcul = longueur * largeur
        print(str(longueur) + " x " + str(largeur) + " = " + str(calcul))
        surfaceANettoyer += calcul
    return surfaceANettoyer


def tempsNettoyageEnMinutes(surfaceANettoyer, tempsPourUnMetreCarre):
    return round(surfaceANettoyer * tempsPourUnMetreCarre)


parameters = ("robot_aspirator", 2)

zone1 = {"longueur": 500, "largeur": 150}
zone2 = {"longueur": 309, "largeur": 480}
zone3 = {"longueur": 101, "largeur": 480}
zone4 = {"longueur": 90, "largeur": 220}

zones = [zone1, zone2, zone3, zone4]

surfaceANettoyer = calculDeLaSurfaceANettoyer(zones)
print("La surface à nettoyer est de:" + str(surfaceANettoyer) + "m2")

tempsEstime = tempsNettoyageEnMinutes(surfaceANettoyer, parameters[1])
print("Le temps estime pour le nettoyage est de :"+str(tempsEstime) +" minutes")

if tempsEstime > 55:
    print(parameters[0]+" dit qu'il va prendre un peu de temps pour nettoyer entierement la chambre")
else:
    print(parameters[0]+"je serai rapide")

