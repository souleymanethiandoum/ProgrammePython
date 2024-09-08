class DataCollections: 
    def __init__(self,liste,dictionnaire=None): # init permet de définir les attributs(parametres) de la classe(objet) et de leur assigner  des valeurs initiales
      
        self.liste=liste                   
        self.dictionnaire=dictionnaire

    
    def Ajouter_un_elmt_liste(self,elmt):
        self.liste.append(elmt)

    def supprimer_un_elmt_liste(self,elmt): 
        self.liste.remove(elmt)

    def Ajout_un_elmt_dict(self,cle,valeur):
        self.dictionnaire[cle]=valeur
    def afficher_dict(self):
        clef=self.dictionnaire.keys()
        valeurs=self.dictionnaire.values()
        paire = self.dictionnaire.items()
        print(f'affiche les clefs : {clef}')
        print(f'affiche les valeus : {valeurs}')
        print(f'affiche les paire : {paire}')        # Affiche clef valeur
        
        









        