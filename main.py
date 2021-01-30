from jeux import *
from affichage import *
import random as rdm
import numpy as np
print("bienvenu dans le jeux de démineur ")
test =creatMineField(5,5)
print("vois-ci le champs de mine ")
displayMine(test)
print(test)
print("creuse en entrant les coordonnes d'une case (x,y) avec 0 <= x <5 et 0 <= y<5")
x_i=int(input("abscisse="))
y_j=int(input("ordonne="))
PartieGagner=False 
PartiePerdu=False
while(PartieGagner==False and PartiePerdu==False):
        PartiePerdu=creuser(test,x_i,y_j)
        displayMine(test)
        if PartiePerdu==True:
            print("presence de mine!! puff tu est mort")
        else :
            PartieGagner=partieGagner(test)
            if PartieGagner==True:
                print("felicitation tu as gange la partie ")
            else :
                x_i=int(input("x="))
                y_j=int(input("y="))
        if (PartieGagner==True or PartiePerdu==True):
            print("veux tu rejouer ? si oui entre 1 si no 0 ")
            val=int(input("val="))
            if (val==1):
                test=creatMineField()
                displayMine(test)
                print("choisi la prochaine à déminer en entrant ses coordonees")
                x_i=int(input("x="))
                y_j=int(input("y="))
                PartieGagner=False 
                PartiePerdu=False
            else :
                print("merci à la prochaine")
                