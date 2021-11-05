# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

# =============================================================================
# 
# =============================================================================

def exctrationDeStock (nomFichier) :
    
    
    Viandes=[]
    Poissons=[]
    LegumesManger=[]
    Féculents=[]
    TypesPates=[]
    SaucesPates=[] # à rajouter dans le tableau
    FromagePates=[] #à rajouter dans tableau
    LegumesAccompagnement=[]
    
    monFichier= open (nomFichier,'r')
    for lig in monFichier:
        ligne= monFichier.readline()
        #traiter la ligne comme il faut
        
        #Ligne = ligne.split()
        
        
        #Viande= (Ligne[0],Ligne[1])
        #Viandes.append(Viande)
        #etc
        #
    
    monFichier.close    
        
    Stock=Viandes+Poissons+LegumesManger+Féculents+TypesPates+SaucesPates+FromagePates+LegumesAccompagnement  
        
        
    return Viandes,Poissons,LegumesManger,Féculents,TypesPates,SaucesPates,FromagePates,LegumesAccompagnement
        

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
        
    