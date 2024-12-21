from . import AlgoColo as grid
from . import Coloration as colo
from . import Matrice as mat
import math as Math
import random

class SudokuModel : 

    def __init__ (self, dimension) :
        assert (type(dimension) == int and dimension > 0), "dimension n'est pas un entier positif"
        if(Math.sqrt(dimension)) % 1 != 0 :
            raise Exception("dimension n'est pas un carré parfait")
        self.dimension = dimension 
        self.mat = mat.Matrice(dim=dimension * dimension)
        self.region = self.__init_region()
        self.__init_matrice()
        self.colo = colo.Coloration(self.mat)
        for i in range(dimension) :
            self.colo.add_color(i)
        self.grid = grid.ColoAlgo(self.colo)

    # Requêtes

    def get_dimension(self) : 
        """
        Renvoie la dimension du sudoku
        """
        return self.dimension
    
    def get_matrice(self) :
        """
        Renvoie la matrice du sudoku
        """
        return self.mat
    
    def get_region(self) :
        """
        Renvoie les régions du sudoku
        """
        return self.region
    
    def get_coloration(self) :
        """
        Renvoie la coloration du sudoku
        """
        return self.colo
    
    # Commandes 

    def resolve_with_backtrack(self) :
        """
        Résout le sudoku avec l'algorithme de backtrack
        """
        self.grid.color_with_backtrack()

    def resolve_with_glouton(self) :
        """
        Résout le sudoku avec l'algorithme glouton
        """
        self.grid.color_with_glouton()

    def resolve_with_welsh_powell(self) :
        """
        Résout le sudoku avec l'algorithme welsh powell
        """
        self.grid.color_with_welsh_powell()
    
    def partial_resolve(self, d) :
        """
        Prend en entrée un entier d et révèle d cases du sudoku
        """
        assert d > 0, "d ne peut pas être négatif"
        color = {}
        self.colo.reset_color_node()
        random.shuffle(self.colo.color_list)
        self.grid.color_with_backtrack()
        for i in range(d) :
            rand = random.randint(0, self.dimension * self.dimension - 1)
            while(rand in color.keys()) :
                rand = random.randint(0, self.dimension * self.dimension - 1)
            color[rand] = self.colo.color_of(rand)
            self.colo.remove_color_of(rand)

        self.colo.reset_color_node()
        for i in color.keys() :
            self.colo.define_color(i, color[i])

        


    def change_dimension(self, dimension) :
        """
        Prend en entrée un entier dimension qui est la nouvelle dimension du
        sudoku
        """
        assert (type(dimension) == int and dimension > 0), "dimension n'est pas un entier positif"
        if(Math.sqrt(dimension)) % 1 != 0 :
            raise Exception("dimension n'est pas un carré parfait")
        self.dimension = dimension 
        self.mat = mat.Matrice(dim=dimension * dimension)
        self.region = self.__init_region()
        self.__init_matrice()
        self.colo = colo.Coloration(self.mat)
        for i in range(dimension) :
            self.colo.add_color(i)
        self.grid = grid.ColoAlgo(self.colo)

    # Outils

    
    def __init_region(self):
        """
        Initialise les régions du sudoku 
        """
        region = {}
        sqrt_dim = int(Math.sqrt(self.dimension))
        for i in range(self.dimension) : 
            region[i] = []
        for r in range(self.dimension) : 
            for i in range(self.dimension) :
                region_row = r // sqrt_dim
                region_col = r % sqrt_dim
                cell_row = i // sqrt_dim
                cell_col = i % sqrt_dim
                k = (region_row * sqrt_dim + cell_row) * self.dimension + region_col * sqrt_dim + cell_col
                if cell_row % sqrt_dim == 0 and cell_row != 0:
                    k += self.dimension
                region[r].append(int(k))

        return region 
    def __init_matrice(self) : 
        """
        Initialise les arcs de la matrice du sudoku, c'est à dire, tous
        les sommets de la même ligne, de la même colonne et de la même région
        sont reliés entre eux
        """
        for i in range(self.dimension) :
            for j in range(self.dimension) :
                for k in range(self.dimension) :
                    if(j != k) :
                        self.mat.add_arc(i * self.dimension + j, i * self.dimension + k)
                        self.mat.add_arc(j * self.dimension + i, k * self.dimension + i)
        for i in self.region.keys() : 
            for j in self.region[i] : 
                for k in self.region[i] : 
                    if(j != k) :
                        self.mat.add_arc(j, k)
                        self.mat.add_arc(k, j)

    def __str__(self) :
        r = ""
        for i in range(self.dimension) : 
            for j in range(self.dimension) :
                s = " "
                if(self.colo.is_colored(i * self.dimension + j)) :
                    s = str(self.colo.color_of(i * self.dimension + j))
                r += "[" + s + "]"
            r += "\n"
        r+= self.region.__str__()
        return r
            
