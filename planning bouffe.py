# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from openpyxl import Workboook
wb = Workbook()
filepath = "C:\Users\Pierre-Jean Martin\Documents\PJ\Jeux\planning bouff\Meal_Chooser/exemple.x"
wb.save(filepath)

# =============================================================================
# 
# =============================================================================

def extraction_de_stock(nomFichier) :
    '''
    Entrée: le nom du fichier de stock au format CSV en chaine de caractère
    Sortie: un tableau 2-dimensionnel contenant un tableau avec le type de nourriture en chaine de caractère, et un autre contenant des 2-uplets des produits et de leur quantité ordonné en ligne par tableau 
    Action: extrait les données du fichier CSV
    '''
    stock = []
    ordreNourriture=[]
    monFichier=open(nomFichier,'r')
    stockBrut = monFichier.readlines()
    count=0
    while count<len(stockBrut)//2:
        ligneTemporaire=[]
        for number, produit in zip(stockBrut[count*2+1].split(','),stockBrut[count*2].split(',')):
            if ('\n' in produit) or ('\n' in number):
                ligneTemporaire.append([produit[:-1], int(number[:-1])])
            else:
                ligneTemporaire.append([produit, int(number)])
        ordreNourriture.append(ligneTemporaire[0][0])
        stock.append(ligneTemporaire[1:])
        count+=1

    monFichier.close()
                
    return [ordreNourriture, stock]

def extraction_de_plats(nomFichier):
    plat = []
    lignes = open(nomFichier, 'r').readlines()
    for i in lignes[1:]:
        tmp = i.split(',')
        tmp = [tmp[0], tmp[1][:-1].split(' / ')]
        plat.append(tmp)
    return plat
        

def Manquant (plat):
    """
    Trouve les ingrédients manquants à partir du Plat choisi en comparant la présence ou non dans le stock des ingrédients qui composent le plat
    """
    ListesCourses=[]
    for ingr in Ingrédients:
        for ingredient in Stock: #penser à définir stock en variable globale ou gérer ca
            
            #si le nom correspond, on fait la soustraction de la quantité d'ingrédient nécessaire à la qté dingredient dans stock
            #et si négatif on ajoute à liste de courses avec la quantité à acheter
            
            if ingr[0] == ingredient[0] :
                ingredient[1]= ingredient[1]-ingr[1]
            
            if ingredient[1]<0:
                element=(ingredient[0],abs(ingredient[1]))
                ListesCourses.append(element)
            
            if ingredient[1] == 0:
                element=(ingredient[0],1)
                ListesCourses.append(element)
    
    return  ListeCourses

def gerer_stock ():


def choisirplat (modechoix) :
    
    """
    Permet de choisir un plat dans le fichier correspondant au mode de choix
    1 plat mix à partir de stock + complétition des manques sur liste course
    2 plat mix + création d'une liste de course selon ce qui manque dans le stock 
    3 plat "complet" -> pas de mix à faire
    
    /!\ penser à faire gaffe aux dates, qui seront implémentées plus tard
    
    """    
    
    if modechoix == 1:
        Plat= "Lol1"
        
    elif modechoix == 2:
        Plat="Lol2"
        
    elif modechoix == 3:
        Plat="Lol3"
        
    ListeCourses = Manquant(Plat)
    
    return Plat,ListeCourses


def créerPlanningSemaine (choixmode):
    
    ListeSemaine=[]
    
    ProgrammeCuisine=[]
    #contient les recettes
    
    for i in range (0,7):
        Plat=choisirplat(choixmode)[0]
        ListeSemaine.append(Plat[0])
        
    
    
    
    print("\n \t Lundi \t Mardi \t Mercredi \t Jeudi \t Vendredi \t Samedi \t Dimanche \t \n Plats",ListeSemaine[0],'\t',ListeSemaine[1],'\t',ListeSemaine[2],'\t',ListeSemaine[3],'\t',ListeSemaine[4],'\t',ListeSemaine[5],'\t',ListeSemaine[6])
        
    

print(extraction_de_plats("mesPlats.csv"))