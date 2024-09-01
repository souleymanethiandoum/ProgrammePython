import math 

class Calculatrice:
    def __init__(self) -> None:
        pass

    def addition(self,a,b):
        return a+b
    
    def soustraction(self,a,b):
        return a-b
    
    def multiplication(self,a,b):
        return a*b
    
    def puissance(self,a,n):
        return a**n
    
    def division(self,a,b):
        if b==0:
            raise ValueError("Division par zéro non permise.")
        return a/b
    
    def division_entiere(self,a,b):
        return a//b
    
    def modulo(self,a,b): #reste de la division de a par b
        return a%b
    
    def racine_carre(self,a):
        if a<0:
            raise ValueError("a ne peut pas être négatif.")
        return math.sqrt(a)
    
    def somme_n_premiers_entiers(self,n):
        som=0
        for i in range(n+1):
            som=som+i
        return   som 
    
    def somme_n_premiers_while(selt,n):
        som=0
        i=1
        while i <= n:
            som = i + som
            i = i + 1
        return som    

    def singne(self,n):
        if n > 0:
            print("n est positif")
        elif n < 0 :
            print(" n est négatif") 
        else:
            print("n est zéro")       




         
    