#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici
    resultat = []
    compteur = 1
    caractere_en_cours = s[0]
    for k in range(1, len(s)): 
        if s[k] == caractere_en_cours :
            compteur += 1
        else :
            resultat.append((caractere_en_cours, compteur))
            caractere_en_cours = s[k]
            compteur = 1
    resultat.append((caractere_en_cours, compteur))
    return resultat


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    if len(s)==0:
        return[]
    compteur = 1
    while compteur < len(s) and s[compteur]==s[0]:
        compteur += 1
    premier_tuple = (s[0], compteur)
    return [premier_tuple] + artcode_r(s[compteur:])
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()