from . import Coloration as colo

class ColoAlgo :

    def __init__(self, C) : 
        assert type(C) == colo.Coloration, "C n'est pas une coloration"
        self.c = C
        self.mat = self.c.matrice()
        self.order = []

    # Requêtes
    def order(self) : 
        """
        Renvoie l'ordre de coloration des sommmets associé à la coloration
        (utilisé pour l'algorithme de Welsh Powell et Glouton)  
        """
        return self.order
    
    def coloration(self) :
        """
        Renvoie la coloration associée à la matrice d'adjacence 
        """ 
        return self.c

    # Commandes     

    def color_with_glouton (self) : 
        """
        Colorie le graphe en utilisant l'algorithme glouton de la coloration
        de graphe 
        """
        if(self.order == []) :
            self.__order()
        for i in self.order :
            linked_colo = [self.c.color_of(j) for j in self.mat.successors(i)] + [self.c.color_of(j) for j in self.mat.predecessors(i)]
            self.c.define_color(i, self.__first_not_in_list(linked_colo))

    def color_with_welsh_powell(self) :
        """
        Colorie le graphe en utilisant l'algorithme de Welsh Powell de la
        coloration de graphe (l'algorithme n'est pas compatible avec les
        couleurs déjà définies) 
        """
        self.c.reset_color_node()
        self.__order()
        color = 0 
        for i in self.order :
            if(not self.c.is_colored(i)) : 
                if(self.c.nb_color() <= color) : 
                    self.c.generate_color()
                self.c.define_color(i, self.c.pick(color))
            for k in self.mat.other_nodes(i) : 
                if(not self.c.is_colored(k)) :
                    self.c.define_color(k, self.c.pick(color))
            color += 1

    def color_with_backtrack(self) : 
        """
        Colorie le graphe en utilisant l'algorithme de backtrack de la
        coloration de graphe 
        """
        i = 0
        while(not self.__backtract() and i < self.mat.get_nb_nodes()) :
            i += 1
            self.c.generate_color()
            self.c.reset_color_node()

    # Outils

    def __backtract(self):
        """
        Fonction qui Colorie le graphe en utilisant l'algorithme de backtrack
        avec un nombre limité de couleurs. Renvoie Vrai si le graphe a pu être
        colorié avec le nombre de couleurs actuel, Faux sinon
        """
        stack = [(0, 0)] 
        while stack:
            actualColor, actualNode = stack.pop()
            if actualColor == self.c.nb_color():
                if actualNode == 0:
                    self.c.reset_color_node()
                    return False
                else:
                    indice_of_old_color = self.c.color_index(self.c.color_of(actualNode - 1))
                    self.c.remove_color_of(actualNode - 1)
                    stack.append((indice_of_old_color + 1, actualNode - 1))
            elif actualNode == self.mat.get_nb_nodes():
                return True
            elif self.c.is_colored(actualNode):
                actualNode += 1
                actualColor = 0
                stack.append((actualColor, actualNode))
            elif self.__is_coloriable(actualNode, actualColor):
                self.c.define_color(actualNode, self.c.pick(actualColor))
                actualNode += 1
                actualColor = 0
                stack.append((actualColor, actualNode))
            else:
                actualColor += 1
                stack.append((actualColor, actualNode))
        return False

    def __is_coloriable(self, i, color) :
        """
        Prend en entrée un entier i et un entier color et renvoie Vrai si le
        sommet i est coloriable avec la couleur color, Faux sinon 
        """
        assert (i >= 0 and i < self.mat.get_nb_nodes()), "i n'est pas un noeud valide"
        assert (color >= 0), "color n'est pas un entier positif"
        assert (color < self.c.nb_color()), "color n'est pas une couleur valide"
        for j in self.mat.successors(i) :
            if(self.c.color_of(j) == self.c.pick(color)) :
                return False
        for j in self.mat.predecessors(i) :
            if(self.c.color_of(j) == self.c.pick(color)) :
                return False
        return True

    def __first_not_in_list(self, l):
        """
        Prend en entrée une liste d'entiers positifs et renvoie le plus petit
        entier positif qui n'est pas dans la liste 
        """
        assert (type(l) == list) , "l n'est pas une liste d'entiers positifs"
        for e in self.c.color_list :
            if e not in l : 
                return e 
        return self.c.generate_color()


    def __order(self) :
        """
        Affecte à order l'ordre de coloration des sommmets associé à la 
        coloration en les triant par nombre de voisins décroissant 
        """
        order = {}
        for i in range(self.mat.get_nb_nodes()) :
            if(not self.c.is_colored(i)) : 
                order[i] = self.mat.nb_successors(i) + self.mat.nb_predecessors(i)
        self.order = sorted(order, key=order.get, reverse=True)

    def __str__(self) : 
        return str(self.c) + "\n" + str(self.order)