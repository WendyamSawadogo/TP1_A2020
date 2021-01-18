# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 20:01:48 2020

@author: HP Pro
"""

"Nom: SAWADOGO"
"Prénoms: Abdoul Raouf Wendyam Issoufou"

redemarrage=True

#boucle permettant le redémarrage du programme
while redemarrage:
    
    nombre=input("Veuillez entrer un entier positif (ou nul pour terminer): ")
    
    
   #vérification de la valeur numérique du nombre 
    a=nombre.isnumeric()
    
    
    
    if not a:
        
        print("Erreur la valeur entrée n'est pas correcte")
    
    if a:
        
        nombre=int(nombre)
        
        #fin du programme dans le cas ou le nombre est 0
        if nombre==0:  
             
                redemarrage=False
        
        if nombre==1:
            
            print("La décomposition est : 1")
                  
        if nombre>1:
            
          #initialisation de la séquence vide 'facteurs' contenant 
            facteurs=()
            dernier_indice=0
        
            #boucle permettant de trouver le plus petit diviseur du nombre et de l'inclure dans 'facteur'
            for i in range(2,nombre+1):
                
                
                    while nombre%i==0:
                        
                        facteurs=facteurs+(i,)
                        nombre=nombre//i
                        
                        #mise en mémoire de la valeur du dernier diviseur
                        dernier_indice=dernier_indice+1
                    
              
             
            
            print("Sa décomposition en produit de facteurs premiers est: ",end='')

#affichage du contenu de la séquence 'facteurs'
            for entier in facteurs:
                
                #condition d'affichage du symbole '*' entre les facteurs
                if facteurs.index(entier)==dernier_indice-1:
                    
                    print(entier,end='')
                    
                else:
                    
                    print(entier,end='*')
                
                    
                    

        