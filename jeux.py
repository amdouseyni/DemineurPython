from affichage import *
import random as rdm
import numpy as np
def creatMineField(tab,nbLigne,nbClone):
    for i in range(nbLigne):
        for j in range(nbClone):
            tab[i,j]=putMineOrNot()
    return tab
def putMineOrNot(): #pose une mine ou pas 
    nbAlea=rdm.randint(0,1)
    if nbAlea==0 :  
        return -1   # -1 qui signifie abscence de mine 
    else :
        return 9   # 9 qui signfie presence de mine
def creuser(mineField,i,j):
    if estPresentMine(mineField[i,j])==True:
        return False
    else :
        mineField[i,j]=compteVoisinMine(mineField,i,j)
        return True 
def estPresentMine(valTest):
    if valTest==-1:
        return True 
    else :
        return False 
def compteVoisinMine(mineField,i,j):
     nbl=mineField.shape[0]
     nbc=mineField.shape[1]
     compteVoisin=0
     for k in range(i-1,i+2):
                if (k>=0 and k<nbl):
                    for l in range (j-1,j+2):
                          if(l>=0 and l<nbc):
                                if k!=i or l!=j:
                                        if mineField[k,l]==-1:
                                            compteVoisin=compteVoisin+1
     return compteVoisin
def partieGagner(mineField):
    nbLigne= mineField.shape[0]
    nbClone=mineField.shape[1]
    test=True
    i=0
    while i<nbLigne and test==True :
        j=0
        while j< nbClone and test==True:
            if mineField[i,j]==9:
                test=False 
            j=j+1
        i=i+1
    return test
def jeu(mineField,i,j):
    RetourCreuser=creuser(mineField,i,j)
    if RetourCreuser==False:
         displayMine(mineField,3,3)
         print("presence de mine!! puff tu est mort")
    else :
        RetourPartieGagne=partieGagner(mineField)
        if RetourPartieGagne==True :
            displayMine(mineField,3,3)
            print("felicitation tu as gange la partie ")
        else :
            displayMine(mineField,3,3)
            choiceCase()
            x_i=int(input("x="))
            x_j=int(input("y="))
            jeu(mineField,x_i,x_j)
def choiceCase():
            print("veuiller choisir la prochaine case à jouer en entrant les coordonnees")
if __name__=="__main__":
    print("[phase teste des fonctions]")
    tab=np.zeros((5,5),dtype=int) # creation d'un tableau vide 
    mineField=creatMineField(tab,5,5)
    print(mineField)
    print("[phase de teste de la fonction  creuser]")
    creuser(mineField,3,3)
    print(mineField)
    displayMine(mineField,5,5)


