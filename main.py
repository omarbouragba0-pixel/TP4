# main.py
from noeud import Noeud

# Instanciation de l'expression exp(2 + y)

# 1. Création des feuilles (constante et variable)
noeud_2 = Noeud(2)
noeud_y = Noeud("y")

# 2. Création du noeud d'addition '+' et ajout des feuilles
noeud_plus = Noeud("+")
noeud_plus.ajouter_enfant(noeud_2)
noeud_plus.ajouter_enfant(noeud_y)

# 3. Création de la racine 'exp' et ajout du sous-arbre '+'
racine = Noeud("exp")
racine.ajouter_enfant(noeud_plus)

# Vérification de l'affichage en notation polonaise
expression_polonaise = racine.notation_polonaise()

print("Résultat de l'affichage polonais :")
print(expression_polonaise)

# Assertion pour vérifier le résultat attendu
assert expression_polonaise == "exp + 2 y", f"Attendu 'exp + 2 y', obtenu '{expression_polonaise}'"
print("\nValidation réussie ! L'affichage correspond exactement à 'exp + 2 y'.")