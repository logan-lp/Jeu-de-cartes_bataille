#---------------------------------------------
#  Importation des modules
#---------------------------------------------
from random import*
from time import*

#----------------------------------------------
# Fonction création jeu de cartes
#----------------------------------------------

def jeu_de_cartes() :
    """Fonction qui retourne une liste comportant un jeu de 52 cartes."""
    return ["As ♠", "2 ♠", "3 ♠", "4 ♠"
                    , "5 ♠", "6 ♠", "7 ♠", "8 ♠"
                    , "9 ♠", "10 ♠", "Valet ♠"
                    , "Dame ♠", "Roi ♠", "As ♣", "2 ♣"
                    , "3 ♣", "4 ♣", "5 ♣", "6 ♣"
                    , "7 ♣", "8 ♣", "9 ♣", "10 ♣"
                    , "Valet ♣", "Dame ♣", "Roi ♣"
                    , "As ♥", "2 ♥", "3 ♥", "4 ♥"
                    , "5 ♥", "6 ♥", "7 ♥", "8 ♥"
                    , "9 ♥", "10 ♥", "Valet ♥"
                    , "Dame ♥", "Roi ♥", "As ♦"
                    , "2 ♦", "3 ♦", "4 ♦"
                    , "5 ♦", "6 ♦", "7 ♦", "8 ♦"
                    , "9 ♦", "10 ♦", "Valet ♦"
                    , "Dame ♦", "Roi ♦"]

#----------------------------------------------
# Fonctions d'affichage
#----------------------------------------------

def afficher_carte(jeu1, jeu2) :
    print(jeu1[0], jeu2[0])


def afficher_nombres_cartes(jeu1, jeu2, nom1, nom2) :
    nb1 = 0
    for i in jeu1:
        nb1 += 1
    nb2 = 0
    for g in jeu2:
        nb2 += 1
    print(nom1, "a un paquet de ", nb1, "cartes.")
    print(nom2, "a un paquet de ", nb2, "cartes.")


def afficher_vainqueur_tour(gagnant, nom1, nom2) :
    if gagnant == 'bataille':
        print("Bataille!")
    elif gagnant == 'joueur1':
        print(nom1, "a gagné le tour.")
    elif gagnant == 'joueur2':
        print(nom2, "a gagné le tour.")


def afficher_vainqueur_jeu(gagnant, jeu1, jeu2, nom1, nom2) :
    if gagnant == 'bataille':
        if jeu1 == []:
            print(nom2, "a gagné le jeu.")
        elif jeu2 == []:
            print(nom1, "a gagné le jeu.")
    if gagnant == 'joueur1':
        print(nom1, "a gagné le jeu.")
    elif gagnant == 'joueur2':
        print(nom2, "a gagné le jeu.")



#----------------------------------------------
# Fonctions relatives aux cartes des joueurs
#-----------------------------------------------

def valeur_carte(carte:str) :
    c = carte[0] + carte[1]
    match c:
        case "As":
            return 14
        case "Ro":
            return 13
        case "Da":
            return 12
        case "Va":
            return 11
        case _:
            return int(c)



def comparer_carte(carte_joueur1:str, carte_joueur2:str) :
    #print(valeur_carte(carte_joueur1))
    #print(valeur_carte(carte_joueur2))
    if valeur_carte(carte_joueur1) > valeur_carte(carte_joueur2):
        return 'joueur1' #print('joueur1')

    elif valeur_carte(carte_joueur1) < valeur_carte(carte_joueur2):
        return 'joueur2' #print('joueur2')

    else:
        return 'bataille' #print('bataille')


#----------------------------------------------
# Fonctions relatives aux jeux des joueurs
#-----------------------------------------------

def distribution_jeu(jeu_complet:list, nombre_cartes:int) :
    shuffle(jeu_complet)
    lst = []
    for i in range (0,nombre_cartes):
        lst.append(jeu_complet[i])
    for g in range (0,nombre_cartes):
        jeu_complet.remove(jeu_complet[0])
    return lst


def ordonner_jeu(jeu_vainqueur:list, jeu_perdant:list) :#2 cartes a la fin du paquet
    jeu_vainqueur.append(jeu_perdant[0])
    jeu_vainqueur.append(jeu_vainqueur[0])
    jeu_vainqueur.remove(jeu_vainqueur[0])
    jeu_perdant.remove(jeu_perdant[0])

def gestion_bataille(jeu_joueur1:list, jeu_joueur2:list, gagnant_bataille:str) :
    global lst_bataille
    lst_bataille = []
    if gagnant_bataille=='bataille':
        a=1

    for i in range(0,1):
        #print(i)
        lst_bataille.append(jeu_joueur1[1])
        lst_bataille.append(jeu_joueur2[1])
        jeu_joueur1.remove(jeu_joueur1[1])
        jeu_joueur2.remove(jeu_joueur2[1])
    if comparer_carte(jeu_joueur1[0], jeu_joueur2[0]) == 'bataille':
        gestion_bataille(jeu_joueur1, jeu_joueur2, gagnant_bataille)
    elif comparer_carte(jeu_joueur1[0], jeu_joueur2[0]) == 'joueur1':
        jeu_joueur1.append(lst_bataille)
        lst_bataille = []
    else:
        jeu_joueur2.append(lst_bataille)
        lst_bataille = []



def gestion_tour(gagnant:str, jeu_joueur1:list, jeu_joueur2:list) :
    if gagnant== 'joueur1':
        ordonner_jeu(jeu_joueur1, jeu_joueur2)
    else:
        perdant = jeu_joueur1
        ordonner_jeu(jeu_joueur2, jeu_joueur1)
    #if gagnant == 'bataille':
        #gestion_bataille(jeu_joueur1, jeu_joueur2, 'bataille')


def triBulles(lst):
    for i in range(len(lst),0,-1):
        liste_triée = True
        for j in range(0,i-1):
            if lst[j+1] < lst[j]:
                lst[j+1] , lst[j] = lst[j] , lst[j+1]
                liste_triée = False
        if liste_triée == True:
            break
    return lst

#---------------------------------------------
# Fonction principale
#---------------------------------------------


def jeu() :
    pass

jeu_complet = jeu_de_cartes()
nom_joueur1 = 'Logan' #input("Tapez le nom du premier joueur : ")
nom_joueur2 = 'Elena' #input("Tapez le nom du deuxième joueur : ")
jeu_joueur1 = distribution_jeu(jeu_complet, 26)
jeu_joueur2 = distribution_jeu(jeu_complet, 26)

while jeu_joueur1 != [] or jeu_joueur1 != []:
    #chercher vainqueur du tour ???
    afficher_nombres_cartes(jeu_joueur1, jeu_joueur2, nom_joueur1, nom_joueur2)
    afficher_carte(jeu_joueur1, jeu_joueur2)
    gagnant = comparer_carte(jeu_joueur1[0], jeu_joueur2[0])
    afficher_vainqueur_tour(gagnant, nom_joueur1, nom_joueur2)
    print("")
    gestion_tour(gagnant, jeu_joueur1, jeu_joueur2)
    #time.sleep(1)

if jeu_joueur1 == []:
    gagnant = 'joueur2'
else:
    gagnant = 'joueur1'
afficher_vainqueur_jeu(gagnant, jeu_joueur1, jeu_joueur2, nom_joueur1, nom_joueur2)




#print(jeu_joueur1)
#print(jeu_joueur2)
#print(comparer_carte(jeu_joueur1[0], jeu_joueur2[0]))
#gestion_tour(jeu_joueur1, jeu_joueur2, comparer_carte(jeu_joueur1[0], jeu_joueur2[0]))





#afficher_carte(jeu_joueur1, jeu_joueur2)


#shuffle(jeu_temporaire) #Mélange le paquet
#print(jeu_temporaire)


#jeu_joueur1 = ['As ♠', '5 ♥', '2 ♠']
#jeu_joueur3 = ['Dame ♠', '7 ♦', '8 ♦', 'As ♣', 'Valet ♣']
#lst1 = []
#lst2 = []
#for i in jeu_joueur1:
 #   print(valeur_carte(i))










#for i in range (0,len(jeu_joueur2)):
#    print("-", valeur_carte(jeu_joueur2[i]))
#    print("^", valeur_carte(jeu_joueur2[i-1]))
#    if valeur_carte(jeu_joueur2[i]) <= valeur_carte(jeu_joueur2[i-1]):
#        lst2.append(jeu_joueur2[i])
#        del(jeu_joueur2[i])
        #jeu_joueur2.append(jeu_joueur2[i])
        #jeu_joueur2.remove(jeu_joueur2[i])



        #jeu_joueur1.remove(i)
    #if valeur_carte(i) <= valeur_carte(i):
    #    lst1.append(i)
#print(lst2)
#print(jeu_joueur2)
