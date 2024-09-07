import calculatrice
import mes_collections
 

def main():
    calc = calculatrice.Calculatrice()     #on mets le modul aprés la class pour pouvoir utilisé simplement "calc"
    col = mes_collections.Mes_collections() # on mets le modul aprés la class pour pouvoir utilisé simplement "col"


        

    # # add = calc.addition(2,9)
    # # print(f'Addition de a + b est égal à {add}')
    # # div = calc.division(9,0)
    # # print(f'la division de a et  b est égal à {div}')
    # # som_n=calc.somme_n_premiers_entiers(9)
    # # print(f'la somme des entiers est  {som_n}')
    # # calc.singne(-0)
    # print(calc.fonction_valeur_absolue(-44))
    # log=calc.fonction_logarithm(2)
    # print(f'le logarithm est néperien  {log}')
    # base=calc.fonction_logarithm_a_base(2,10)
    # print(f'le logarithm est à base  {base}') 
    # A = calc.Air_du_disque(2)
    # print(f'lair du disque est   {A}')
    # V = calc.Volume_du_conne(2,1)
    # print(f'le volume du conne est   {V}')
    # jeu=calc.Jeu()
    # dé,gain=jeu
    # print(dé,gain)
    # mult=calc.multiple(10000)
    # print( f'le nombre de multiple est {mult}')
    # mult=calc.multiple_gen(13,23,10000)
    # print( f'le nombre de multiple dans le cas gen  est {mult}')
    # mat=col.matrice_remplie_de(10,30,1)
    # print(mat)
    # mat_inf0=col.matrice_diag_inf_0(3,3,1,1)
    # print(mat_inf0)
    # mat_inf1=col.matrice_diag_inf_1(3,3,1,1)
    # print(mat_inf1)
    # mat_sup1 = col.matrice_diag_sup_1(5,5,4,1)
    # print(mat_sup1)
    
    # fus_app=col.fusion_lis_app(["a","b","c"],[1,2,3,4])
    # print(fus_app)
    # fus_conc=col.fusion_list_app_concat(["a","b","c"],[1,2,3])
    # # print(fus_conc)
    # A = list([[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [9, 10, 11, 12],
    #           [13, 14, 15, 16]])
    # print(A)

    # B = list([[16, 15, 14, 13],
    #           [12, 11, 10, 9],
    #           [8, 7, 6, 5],
    #           [4, 3, 2, 1]])
    # prod_mat = col.produit_matr (A,B)
    # print(f'le produit matriciel entre entre A et B est {prod_mat} ')
    A= {"a","b","e",2,3}
    print(A)
    B={"e","f","a",3}
    print(B)
    U,I,P,D=col.operation_ensemblist(A,B)
    print(f'les oprération sont : {U}, {I}, {P},{D}')

    # print(f'les oprération sont : A uninion B est égal à :{U}, Intersection entre A et  B est égal à : {I}, 
    #       A privé de B est égal à{P}, La différence de symétrique entre A et B est égal à : {D}')




if __name__ == "__main__":     
    main()
 

