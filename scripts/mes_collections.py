import numpy as np

class Mes_collections: 
    def __init__(self) -> None:
        pass

    #Creer une matrice  de taille nxm remplie de d'une valeur
    def matrice_remplie_de(self, m,n,valeur):
        return np.full((m, n), valeur)


    #matrice diagonal supérieur et inferieur
    def matrice_diag_inf_0(self,m,n, mu0, beta0):
        for s in range(0, n+1):
          taille = n + m - s
          C_0= np.zeros((taille, taille))
          for i in range(1, taille):
            C_0[i, i-1] = mu0 / (beta0 * s + mu0) # [i,i-1] Ici on rempli la diagonal inférieur
        return C_0
    
    #matrice diagonal supérieur et superieur
    def matrice_diag_inf_1(self,m,n, mu1, beta1):
        for s in range(0, n+1):
          taille = n + m - s
          C_1= np.zeros((taille, taille))
          for i in range(1, taille):
            C_1[i, i-1] = mu1 / (beta1 * s + mu1) # [i,i-1] Ici on rempli la diagonal inférieur
        return C_1
    
          