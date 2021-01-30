
def displayMine(mineField):
    nbLigne=mineField.shape[0]
    nbClone=mineField.shape[1]
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
