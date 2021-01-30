
import random as rdm
import numpy as np

def creatMineField(nbLigne=5,nbClone=5):
    tab=np.zeros((nbLigne,nbClone),dtype=int)
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
        return  True  # la partie est terminée
    else :
        mineField[i,j]=compteVoisinMine(mineField,i,j)
        return False   # on continue à jouer 
def estPresentMine(valTest):
    if valTest==9:
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
                                        if mineField[k,l]==9:
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
            if mineField[i,j]==-1:
                test=False 
            j=j+1
        i=i+1
    return test




