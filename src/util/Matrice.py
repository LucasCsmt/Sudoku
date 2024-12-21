import numpy as np

class Matrice : 
    # Constructeur 

    def __init__ (self, G=None, dim=1) : 
        if(G is None): 
            self.G = np.zeros((dim,dim))
        elif (not self.__is_correct_matrix(G)):
            raise Exception("G n'est pas une matrice d'adjacence valide")
        else :
            self.G = G

    # Requêtes
    def get_nb_nodes(self) :
        """
        Renvoie le nombre de noeuds du graphe
        """
        return self.G.shape[0]
    
    def successors(self, i) :
        """
        Prend en entrée un entier i et renvoie un générateur des successeurs de
        i 
        """
        assert (i >= 0 and i < self.get_nb_nodes()), "i n'est pas un noeud valide"
        for j in range(self.G.shape[0]):
            if self.G[i, j] == 1:
                yield j
    def nb_successors(self, i) :
        """
        Prend en entrée un entier i et renvoie le nombre de successeurs du
        sommet i 
        """
        assert (i >= 0 and i < self.get_nb_nodes()), "i n'est pas un noeud valide"
        return sum(1 for _ in self.successors(i))

    def predecessors(self, i) :
        """
        Prend en entrée un entier i et renvoie un générateur des 
        prédécesseurs du sommet i
        """
        assert (i >= 0 and i < self.get_nb_nodes()), "i n'est pas un noeud valide"
        for j in range(self.G.shape[0]):
            if self.G[j, i] == 1:
                yield j

    def nb_predecessors(self, i) :
        """
        Prend en entrée un entier i et renvoie le nombre de prédécesseurs
        du sommet i 
        """
        assert (i >= 0 and i < self.get_nb_nodes()), "i n'est pas un noeud valide"
        return sum(1 for _ in self.predecessors(i))    

    def other_nodes(self, i) : 
        """
        Prend en entrée un entier i et renvoie un générateur des sommets
        qui ne sont ni successeurs ni prédecesseurs de i 
        """
        assert (i >= 0 and i < self.get_nb_nodes()), "i n'est pas un noeud valide"
        for j in range(self.G.shape[0]):
            if self.G[i, j] == 0 and self.G[j, i] == 0 and i != j:
                yield j



    # Commandes 

    
    def add_arc(self, i, j):
        """
        Prend en entrée i et j, deux entiers, et ajoute un arc de i vers j
        au graphe
        """
        assert (i >= 0 and i < self.get_nb_nodes()), "i n'est pas un noeud valide"
        assert (j >= 0 and j < self.get_nb_nodes()), "j n'est pas un noeud valide"
        self.G[i,j] = 1
    
    def remove_arc(self, i, j):
        """
        Prend en entrée i et j, deux entiers, et supprime l'arc de i vers j
        au graphe 
        """
        assert (i >= 0 and i < self.get_nb_nodes()), "i n'est pas un noeud valide"
        assert (j >= 0 and j < self.get_nb_nodes()), "j n'est pas un noeud valide"
        self.G[i,j] = 0
    
    # Outils

    def __is_correct_matrix(self, G) : 
        """
        Renvoie Vrai si G est une matrice d'adjacence valide, Faux sinon 
        """
        if(type(G) != np.ndarray):
            return False
        if len(G.shape) != 2 or G.shape[0] != G.shape[1]:
            return False
        for i in range(G.shape[0]):
            for j in range(G.shape[1]):
                if G[i,j] >= G.shape[0] or G[i,j] < 0:
                    return False
        return True
    
    def __str__ (self) : 
        return str(self.G)

