# saisie de 2 matrices et calcul + affichage de la matrice produit
# date : 05-01-2023
# auteur : Manuel TARBY

# pour accéder à la commande qui efface l'écran
import os

# déclaration de la matrice A
# boucle sur la saisie du nombre de colonnes des matrices
nbColonnesA = 5
while nbColonnesA > 4:
    nbColonnesA = int(input("Entrez le nombre de colonnes des matrices (maximum 4) = "))
# boucle sur la saisie du nombre de lignes des matrices
nbLignesA = 6
while nbLignesA > 4:
    nbLignesA = int(input("Entrez le nombre de lignes des matrices (maximum 4) = "))

# déclaration de la matrice B
# boucle sur la saisie du nombre de colonnes des matrices
nbColonnesB = 5
while nbColonnesB > 4:
    nbColonnesB = int(input("Entrez le nombre de colonnes des matrices (maximum 4) = "))
# boucle sur la saisie du nombre de lignes des matrices
nbLignesB = 6
while nbLignesB > 4:
    nbLignesB = int(input("Entrez le nombre de lignes des matrices (maximum 4) = "))

# test de compatibilité pour le produit
if nbColonnesA == nbLignesB:
    # efface l'écran
    os.system('cls')

    # déclaration et initialisation des matrices
    A = [[0] * nbLignesA for _ in range(nbColonnesA)]
    B = [[0] * nbLignesB for _ in range(nbColonnesB)]
    C = [[0] * nbColonnesB for _ in range(nbLignesA)]

    # constantes de positionnement
    # largeur de case
    L = 6
    # hauteur de case
    H = 2

    # affichage de la structure des matrices à saisir
    # affichage de la matrice A
    for x in range(0, nbColonnesA):
        for y in range(0, nbLignesA):
            print(f"\033[{y * H + 1};{x * L + 1}H.")
    # affichage de la matrice B
    for x in range(0, nbColonnesB):
        for y in range(0, nbLignesB):
            print(f"\033[{y*H+1};{(x+nbColonnesA+1)*L}H.")
    print(f"\033[{(nbLignesB*H)//2};{nbColonnesA*L}Hx")
    print(f"\033[{(nbLignesB*H)//2};{(nbColonnesA + nbColonnesB +1)*L}H=")

    # saisie de la 1ère matrice : A
    for x in range(0, nbColonnesA):
        for y in range(0, nbLignesA):
            A[x][y] = float(input(f"\033[{y*H+1};{x*L+1}H"))

    # saisie de la 2ème matrice : B
    for x in range(0, nbColonnesB):
        for y in range(0, nbLignesB):
            B[x][y] = float(input(f"\033[{y*H+1};{(x+nbColonnesA+1)*L}H"))

    # remplissage de C avec le produit de A et B
    for x in range(0, nbColonnesB):
        for y in range(0, nbLignesA):
            for z in range(0, nbColonnesA):
                C[x][y] += A[z][y] * B[x][z]

    # affichage de la matrice C
    for x in range(0, nbColonnesB):
        for y in range(0, nbLignesA):
            print(f"\033[{y * H + 1};{(x + nbColonnesA + nbColonnesB + 2) * L}H{int(C[x][y])}")
else:
    print("Les deux matrices ne sont pas multipliables.")
