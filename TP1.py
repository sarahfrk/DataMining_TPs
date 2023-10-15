''' 
    Exo1: Analyse_des_Données **Dta_mining   10/10/2023
    FERKOUS Sarah 191931043867
'''
import matplotlib.pyplot as plt
import numpy as np


#QST 1
print("\nQuestion 1===============================\n\n")
def chargement_dataset(data):
    lines = []
    with open(data, 'r') as file:
        for line in file:
            lines.append(line)
    return lines

result = chargement_dataset('Dataset-Exos.txt') 


#print(result)
'''
for line in result:
    print(line)
'''

#QST 2
print("\nQuestion 2===============================\n\n")
def informations_dataset(dataset):
    if dataset is None:
        print("Le dataset est vide ou n'a pas été chargé correctement.")
        return

    nombre_de_lignes = len(dataset)
    if nombre_de_lignes == 0:
        print("Le dataset est vide.")
        return

    longueur_lignes = [len(ligne) for ligne in dataset]
    longueur_moyenne = sum(longueur_lignes) / nombre_de_lignes

    print(f"Nombre total de lignes dans le dataset : {nombre_de_lignes}")
    print(f"Longueur moyenne des lignes : {longueur_moyenne:.2f} caractères")

    print("\nPremières lignes du dataset :")
    for i in range(5):
        print(dataset[i])


informations_dataset(result)


#QST 3
print("\nQuestion 3===============================\n\n")

def moyenneM(tab):
    s = sum(tab)
    m = len(tab)
    return s/m


def medianeM(tab):
    liste_entiers_triee = sorted(tab)

    n = len(liste_entiers_triee)
    if n % 2 == 1:
        # Si la liste a une longueur impaire, la médiane est au milieu
        mediane = liste_entiers_triee[n // 2]
    else:
        # Si la liste a une longueur paire, la médiane est la moyenne des deux éléments du milieu
        mediane = (liste_entiers_triee[(n - 1) // 2] + liste_entiers_triee[n // 2]) / 2
    return mediane    


def modeM(tab):
    occurrences = {}
    for valeur in tab:
        if valeur in occurrences:
            occurrences[valeur] += 1
        else:
            occurrences[valeur] = 1

    mode = None
    max_occurrences = 0

    for valeur, count in occurrences.items():
        if count > max_occurrences:
            mode = valeur
            max_occurrences = count
    return mode        




def tendances_centrales(attribut):
    if len(attribut) == 0:
        return None

    moyenne = moyenneM(attribut)
    mediane = medianeM(attribut)
    mode_resultat = modeM(attribut)
 
    return {
        "Moyenne": moyenne,
        "Médiane": mediane,  #milieu
        "Mode": mode_resultat #plus freq
    }


for line in result:
    segments = line.split(',')
    chiffres = []
    for segment in segments:
        try:
            chiffre = float(segment)
            chiffres.append(chiffre)
        except ValueError:
            pass
    print(chiffres)    
    resultats = tendances_centrales(chiffres)        

    if resultats:
        print("Tendances centrales de l'attribut :")
        for stat, valeur in resultats.items():
            print(f"{stat}: {valeur}")
    else:
        print("Aucune donnée fournie.")



#QST 4
print("\nQuestion 4===============================\n\n")
def calculer_quartiles(attribut):
    # Trier l'attribut
    attribut_trie = sorted(attribut)

    # Calculer (Q0) qui est le min
    Q0 = attribut_trie[0]

    # Calculer le premier quartile (Q1)
    n = len(attribut_trie)
    q1_idx = n // 4
    Q1 = (attribut_trie[q1_idx - 1] + attribut_trie[q1_idx]) / 2

    # Calculer le deuxième quartile (Q2, la médiane)
    if n % 2 == 1:
        Q2 = attribut_trie[n // 2]
    else:
        mid_idx = n // 2
        Q2 = (attribut_trie[mid_idx - 1] + attribut_trie[mid_idx]) / 2

    # Calculer le troisième quartile (Q3)
    q3_idx = (3 * n) // 4
    Q3 = (attribut_trie[q3_idx - 1] + attribut_trie[q3_idx]) / 2

    # Calculer le quatrième quartile (Q4)
    q4_idx = n - q1_idx
    Q4 = (attribut_trie[q4_idx - 1] + attribut_trie[q4_idx]) / 2


    return Q0, Q1, Q2, Q3, Q4



for line in result:
    segments = line.split(',')
    chiffres = []
    for segment in segments:
        try:
            chiffre = float(segment)
            chiffres.append(chiffre)
        except ValueError:
            pass
    print(chiffres)    
    Q0, Q1, Q2, Q3, Q4 = calculer_quartiles(chiffres)       

    if (Q0 and Q1 and Q2 and Q3 and Q4):
        print("les quartiles  :")
        print("Q0 :", Q0)
        print("Q1 :", Q1)
        print("Q2 (médiane) :", Q2)
        print("Q3 :", Q3)
        print("Q4 :", Q4)
    else:
        print("Aucune donnée fournie.")



#QST 5
print("\nQuestion 4===============================\n\n")
def valeurs_manquantes(attribut):
    # Compter les valeurs manquantes
    valeurs_manquantes = 0
    total_valeurs = len(attribut)

    for valeur in attribut:
        if valeur is None or valeur == '':
            valeurs_manquantes += 1

    # Calculer le pourcentage de valeurs manquantes
    pourcentage_manquant = (valeurs_manquantes / total_valeurs) * 100

    print("Nombre de valeurs manquantes :", valeurs_manquantes)
    print("Pourcentage de valeurs manquantes : {:.2f}%".format(pourcentage_manquant))



for line in result:
    segments = line.split(',')
    chiffres = []
    for segment in segments:
        try:
            chiffre = float(segment)
            chiffres.append(chiffre)
        except ValueError:
            pass
    print(chiffres)
    valeurs_manquantes(chiffres)