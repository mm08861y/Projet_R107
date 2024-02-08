import time
from random import*

tableau=[]
running = True
while running:
    a = int(input("Donner la taille du tableau: "))
    min = int(input("Donner la valeur min : "))
    max = int(input("Donner la valeur max : "))
    if 10000 >= max > min >= 0 and a >= 1:
        running = False
    elif max < min or a < 1:
        print("Attention!!")
    elif max > 10000 or min < 0:
        print("Choisir le min et le max dans l'intervalle [0,10000]")

def tabl():
    for i in range(a):
        i = randint(min,max)
        tableau.append(i)
    print("Voici un tableau",tableau)
tabl()

def tri_selection(tableau):
    for x in range(len(tableau)-1,0,-1):
        for y in range(x):
            if tableau[y]>tableau[x]:
                tableau[y],tableau[x]=tableau[x],tableau[y]
    return tableau

#Tri fusion fonction de division du tableau
def tri_fusion(tableau):
    if  len(tableau) <= 1:
        return tableau
    pivot = len(tableau)//2
    tableau1 = tableau[:pivot]
    tableau2 = tableau[pivot:]
    gauche = tri_fusion(tableau1)
    droite = tri_fusion(tableau2)
    fusionne = fusion(gauche,droite)
    return fusionne


#Tri fusion fonction de fusion de 2 listes
def fusion(tableau1,tableau2):
    indice_tableau1 = 0
    indice_tableau2 = 0
    taille_tableau1 = len(tableau1)
    taille_tableau2 = len(tableau2)
    tableau_fusionne = []
    while indice_tableau1<taille_tableau1 and indice_tableau2<taille_tableau2:
        if tableau1[indice_tableau1] < tableau2[indice_tableau2]:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1 += 1
        else:
            tableau_fusionne.append(tableau2[indice_tableau2])
            indice_tableau2 += 1
    while indice_tableau1<taille_tableau1:
        tableau_fusionne.append(tableau1[indice_tableau1])
        indice_tableau1+=1
    while indice_tableau2<taille_tableau2:
        tableau_fusionne.append(tableau2[indice_tableau2])
        indice_tableau2+=1
    return tableau_fusionne

def tri_bulle(tableau):
    for i in range(0, len(tableau)):
        for y in range(i):
            if tableau[y] > tableau[i]:
                tableau[i], tableau[y] = tableau[y], tableau[i]
    return tableau
running = True
while running:
    choix=int(input("Choisir le tri :\n" "1-Le Tri par Sélection\n" "2-Le Tri à Bulles\n" "3-Le Tri Fusion\n" "4-Comparaison des tris\n"))
    if choix==1:
        print("le tri par sélection donne:\n",)
        t1=time.perf_counter()
        tableau_trie=tri_selection(tableau)
        t2 = time.perf_counter()
        delta_selection= t2 - t1
        print(tableau_trie)
        print("Voici le temps écoulé en seconde {}".format(t2-t1))
        running = False
    elif choix==2:
        print("le tri à bulle donne:\n")
        t3 = time.perf_counter()
        tableau_trie=tri_bulle(tableau)
        t4 = time.perf_counter()
        delta_bulle= t4 -t3
        print(tableau_trie)
        print("Voici le temps écoulé en seconde {}".format(t4-t3))
        running = False
    elif choix==3:
        print("le tri fusion donne:\n")
        t5 = time.perf_counter()
        tableau_trie = tri_fusion(tableau)
        t6 = time.perf_counter()
        delta_fusion= t6 - t5
        print(tableau_trie)
        print("Voici le temps écoulé en seconde {}".format(t6 - t5))
        running = False
    elif choix == 4:
        t1 = time.perf_counter()
        tableau_trie=tri_selection(tableau)
        t2 = time.perf_counter()
        delta_selection = t2 - t1

        t3 = time.perf_counter()
        tableau_trie=tri_bulle(tableau)
        t4 = time.perf_counter()
        delta_bulle = t4 - t3

        t5 = time.perf_counter()
        tableau_trie = tri_fusion(tableau)
        t6 = time.perf_counter()
        delta_fusion = t6 - t5

        print("Les différentes temps d'exécution :\n")
        print("Tri séléction --->", delta_selection)
        print("Tri à bulle   --->", delta_bulle)
        print("Tri fusion    --->",delta_fusion)
        running= False
    else :
        print("Erreur!, veiller choisir entre 1 et 4")
