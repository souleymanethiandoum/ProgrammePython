import numpy as np

class Mes_collections: 
    def __init__(self) -> None:
        pass
    
# Collections Python (tableaux)
    # Il existe quatre types de données de collection dans le langage de programmation Python :
            
    #    1)La liste est une collection ordonnée et modifiable. Elle autorise les membres en double.
    #    2)Tuple est une collection ordonnée et immuable(inchangeable) . Autorise les membres en double.
    #    3)Un ensemble est une collection non ordonnée, non modifiable* et non indexée. Aucun membre en double.
    #    4)Le dictionnaire est une collection ordonnée** et modifiable. Aucun membre en double.

#Les liste 

    #fusion deux listes: il y a plusieurs  methodes pour le faire (opération direct L2+L1 ou ajour élement par elemnt avec append())
    # On peux utliser extend() qui permet d'ajouter toute type collection dans la liste


    def fusion_lis_app(self,L2,L1):
       for x in L1:
         L2 = np.append(L2,x) #Append modifie L2 directement
       return L2       #Retourner la liste fusionnée
    
    def fusion_list_app_concat(self,L1,C):
       L1 = np.append(L1,C)                #np.append retourne un nouveau tableau avec C ajouté à L1 on pouvez utiliser aussi np.concatenate
       return L1


   #Produit matriciel entre deux matrice
   #on note que si on a des vecteur ligne ceci devient un produit sclaire entre deux vecteur

    def produit_matr(self,A,B):  #le nombre de collone de A doit être égal au nombre de ligne de B
       prod_mat=np.dot(A,B)
       return prod_mat
    
           

    #On rappelle que l'indexation des matrice commence par 0 en python c-à-d le premier element est de M
    # est M[0,0] l'lement situé à la ligne 2 et a la colonne 3 est M[1,2]
        #Creer une matrice  de taille nxm remplie de d'une valeur

    def matrice_remplie_de(self, m,n,valeur):
        return np.full((m, n), valeur)


    #matrice diagonale supérieure et inferieure
    #Diagonal inférieure
    def matrice_diag_inf_0(self,m,n, mu0, beta0):
        for s in range(0, n+1):
          taille = n + m - s
          C_0= np.zeros((taille, taille))
          for i in range(1, taille):
            C_0[i, i-1] = mu0 / (beta0 * s + mu0) # [i,i-1] Ici on rempli la diagonal inférieur
        return C_0
    
   #matrice diagonal inférieur 
    def matrice_diag_inf_1(self,m,n, mu1, beta1):
        for s in range(0, n+1):
          taille = n + m - s
          C_1= np.zeros((taille, taille))
          for i in range(1, taille):
            C_1[i, i-1] = mu1 / (beta1 * s + mu1) # [i,i-1] Ici on rempli la diagonal inférieur
        return C_1
    

    
    #matrice diagonal supérieur et inferieur
    def matrice_diag_sup_0(self,m,n, mu0, beta0):
        for s in range(0, n+1):
          taille = n + m - s
          D_0= np.zeros((taille, taille))
          for i in range(taille):
            if i < taille - 1: #Cette condition s'assure que i reste strictement inférieur à taille - 1 pour ne pas remplire 
                              #l'ement situé à la position (taille-1,taille-1) et sarreter à l'element (taille-1,taille-2)
                D_0[i, i+1] = mu0 * s / (beta0 * s + mu0)# [i,i+1] Ici on rempli la diagonal supérieur
        return D_0

    def matrice_diag_sup_1(self,m,n, mu1, beta1):
        for s in range(0, n+1):
          taille = n + m - s
          D_1= np.zeros((taille, taille)) #matrice remplie de zeros
          for i in range(taille):
            if i < taille - 1: #Cette condition s'assure que i reste strictement inférieur à taille - 1 pour ne pas remplire 
                              #l'ement situé à la position (taille-1,taille-1) et sarreter à l'element (taille-1,taille-2)
                D_1[i, i+1] = mu1 * s / (beta1 * s + mu1)# [i,i+1] Ici on rempli la diagonal supérieur
        return D_1  
    
#les set (ou ensemble )
        # Il est également possible d'utiliser le constructeur set((a,b,c)) pour créer un ensemble ou {a,b,c}.
        #Pour ajouter des éléments d’un autre ensemble à l’ensemble actuel, utilisez la ""update()"" méthode.
        #Ajouter des éléments depuis tropicaldans thisset voici le syntax ""thisset.update(tropical)""
        #L'objet dans la update()méthode n'a pas besoin d'être un ensemble, il peut s'agir de n'importe quel objet itérable (tuples, listes, dictionnaires, etc.).
   

  #Fonction qui retourne toutes les opérations ensemblistes (union, intersection,...)
    def operation_ensemblist(self,A,B):
       Union = A | B
       Intersect = A & B
       Priv = A - B #L’ensemble renvoyé contient des éléments qui existent uniquement dans le premier ensemble,
                                  #et non dans les deux ensembles on note (A/B).
       diff_sym = A ^ B  # C'est la réunion des élements qui ne sont pas  la fois dans A  et dans B
       #A = set.update(A,B)  #La méthode update() insère les éléments de l'ensemble B dans l'ensemble A
       return Union, Intersect, Priv,diff_sym                      

    
          