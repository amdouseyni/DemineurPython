import numpy as np
import random as rdm
from jeux import creatMineField
def displayMine(mineField,nbLigne,nbClone):
    displayLigne(nbLigne) #affiche une ligne
    print(" ")            # passe au ligne suivant
    for i in range(nbLigne):
        for j in range(nbClone):
            displayClone(nbClone,mineField[i,j]) # affiche une clone 
        print("|") #ajoute un barre à la fin 
        displayLigne(nbLigne) # afiche encore une ligne 
        print(" ")# aller à la ligne 
def displayLigne(l):
    for i in range(l):
        print("----",end=" ")
    print('-',end=" ")
def displayClone(c,valTab):
    if valTab==-1 or valTab==9:
        print("| * ",end=" ")
    else :
        print("|",valTab," ",end="")

if __name__=="__main__":
    print("[phase teste des fonctions]")
    print(" ")
    tab=np.zeros((5,5),dtype=int) # creation d'un tableau vide 
    mineField=creatMineField(tab,5,5)
    displayMine(mineField,5,5)
    mineField[4,3]=2
    displayMine(mineField,5,5)