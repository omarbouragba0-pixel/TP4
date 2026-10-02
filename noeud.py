# noeud.py

# une modification (urin)

class Noeud:
    def __init__(self, valeur):
        """
        Initialise un noeud.
        
        :param valeur: str, int ou float représentant la valeur du noeud.

        """
        if not isinstance(valeur, (str, int, float)):
            raise TypeError("La valeur doit être de type str, int ou float.")
        
        self.valeur = valeur
        self.enfants = []

    def ajouter_enfant(self, enfant):
        """
        Ajoute un noeud enfant à la liste des enfants.
        
        :param enfant: Objet de type Noeud à ajouter.

        """
        if not isinstance(enfant, Noeud):
            raise TypeError("L'enfant doit être une instance de la classe Noeud.")
        
        self.enfants.append(enfant)
 # noeud.py

    def __init__(self, valeur):
        """
        Initialise un noeud.
        
        :param valeur: str, int ou float représentant la valeur du noeud.

        """
        if not isinstance(valeur, (str, int, float)):
            raise TypeError("La valeur doit être de type str, int ou float.")
        
        self.valeur = valeur
        self.enfants = []

    def ajouter_enfant(self, enfant):
        """
        Ajoute un noeud enfant à la liste des enfants.
        
        :param enfant: Objet de type Noeud à ajouter.
        """
        if not isinstance(enfant, Noeud):
            raise TypeError("L'enfant doit être une instance de la classe Noeud.")
        
        self.enfants.append(enfant)

    def afficher_polonais(self):
        """
        Retourne la représentation de l'expression sous forme de chaîne 
        de caractères en notation polonaise (préfixée).
        """
        # Récupère la valeur du noeud courant
        elements = [str(self.valeur)]
        
        # Ajoute récursivement la représentation polonaise de chaque enfant
        for enfant in self.enfants:
            elements.append(enfant.afficher_polonais())
            
        # Joint tous les éléments avec des espaces
        return " ".join(elements)       


      