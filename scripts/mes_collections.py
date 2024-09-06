import numpy as np

class Mes_collections: 
    def __init__(self) -> None:
        pass

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
        

    
          