from . import Matrice as mat

class Coloration :

    # Constructeur
    def __init__ (self, G) : 
        assert type(G) == mat.Matrice, "G n'est pas une matrice"
        self.G = G
        self.colo_dico = {}
        self.color_list = []

    # Requêtes 
    def matrice (self) : 
        """
        Renvoie la matrice d'adjacence du graphe 
        """
        return self.G

    def color_of(self, i) :
        """
        Prend en entrée un entier i et renvoie la couleur du noeud i s'il 
        est coloré, None sinon
        """
        assert (i >= 0 and i < self.G.get_nb_nodes()), "i n'est pas un noeud valide"
        if self.is_colored(i) : 
            return self.colo_dico[i]
        else : 
            return None

    def is_colored(self, i) : 
        """
        Prend en entrée un entier i et renvoie Vrai si le sommet i est
        coloré, Faux sinon  
        """
        assert (i >= 0 and i < self.G.get_nb_nodes()), "i n'est pas un noeud valide"
        return i in self.colo_dico

    def nb_color(self) : 
        """
        Renvoie le nombre de couleurs différentes utilisées pour la 
        coloration
        """
        return len(self.color_list) 
    
    def color_list(self) : 
        """
        Renvoie la liste de couleurs utilisées pour la coloration 
        """
        return self.color_list 
    
    def color_index(self, color) : 
        """
        Prend en entrée un entier color et renvoie l'indice de color dans
        la liste des couleurs utilisées pour la coloration
        """
        assert (color in self.color_list), "color n'est pas une couleur valide"
        for c in self.color_list :
            if c == color : 
                return self.color_list.index(c)

    def pick(self, i) :
        """
        Prend en entrée un entier i et renvoie la couleur d'indice i dans
        la liste des couleurs utilisées pour la coloration 
        """
        assert i < len(self.color_list), "i n'est pas une couleur valide"
        return self.color_list[i]
    
    # Commandes

    def add_color(self, color) :
        """
        Prend en entrée un entier color et ajoute color à la liste des
        couleurs utilisées pour la coloration 
        """
        assert (type(color) == int and color >= 0), "color n'est pas un entier positif"
        self.color_list.append(color)

    def generate_color(self) : 
        """
        Génère une nouvelle couleur qui n'est pas dans la liste des couleurs
        utilisées pour la coloration et l'ajoute à la liste des couleurs.
        La couleur choisie est le plus petit entier qui n'est pas dans la 
        liste de couleurs
        """ 
        col = 0
        while True : 
            if col not in self.color_list :
                self.add_color(col)
                return col 
            col += 1

    def define_color(self, i, color):
        """
        Prend en entrée deux entier, i et color, et définit la couleur du
        sommet i à color 
        """
        assert (i >= 0 and i < self.G.get_nb_nodes()), "i n'est pas un noeud valide"
        assert(color in self.color_list), "color n'est pas une couleur valide"
        self.colo_dico[i] = color

    def remove_color_of(self, i) : 
        """
        Prend en entrée un entier i et retire la couleur du sommet i  
        """
        assert (i >= 0 and i < self.G.get_nb_nodes()), "i n'est pas un noeud valide"
        del self.colo_dico[i]
    
    def reset_color_node(self) :
        """
        Retire la couleurs de tous les sommets du graphe 
        """
        self.colo_dico = {}    
    
    # Outils
    def __str__(self) : 
        return str(self.G) + "\n" + str(self.color_list) + "\n" +  str(self.colo_dico)
    

