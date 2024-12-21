import tkinter as tk
from util import SudokuModel as sm
from util import SudokuModel as sm
import math as Math


class Sudoku:
    def __init__(self):
        self.model = sm.SudokuModel(4)
        self.createView()
        self.placeComponents()
        self.createController()

    def createView(self) : 
        self.window = tk.Tk()
        self.window.title("Sudoku")

        self.sudoku_grid = tk.Frame(self.window)
        self.resolve_button = tk.Button(self.window, text="Résoudre le Sudoku")
        self.dimension = tk.Scale(self.window, from_=4, to=16, orient=tk.HORIZONTAL, label="Dimension du Sudoku")
        self.dimension.config(length=200) 
        self.difficulty = tk.Scale(self.window, from_=1, to=100, orient=tk.HORIZONTAL, label="Difficulté du Sudoku")
        self.difficulty.config(length=200)
        self.partial_resolve_button = tk.Button(self.window, text="Résoudre partiellement le Sudoku")
    
    def placeComponents(self) :
        self.build_grid()
        self.sudoku_grid.pack(anchor="center") 
        self.resolve_button.pack(side=tk.BOTTOM)        
        self.dimension.pack(side=tk.BOTTOM)
        self.partial_resolve_button.pack(side=tk.BOTTOM)
        self.difficulty.pack(side=tk.BOTTOM)
    
    def createController(self) :
        self.resolve_button.bind("<Button-1>", self.solve_sudoku)
        self.dimension.bind("<ButtonRelease-1>", self.change_dimension)
        self.partial_resolve_button.bind("<Button-1>", self.partial_solve_sudoku)
    
    def solve_sudoku(self, event) :
        self.model.resolve_with_backtrack()
        self.refresh()
    
    def partial_solve_sudoku(self, event) :
        d = int(self.difficulty.get() * self.model.get_dimension() * self.model.get_dimension() // 100)
        if(d == 0) :
            d = 1
        self.model.partial_resolve(d)
        self.refresh()
    
    def change_dimension(self, event) :
        if(Math.sqrt(self.dimension.get()) % 1 == 0) :
            self.model.change_dimension(int(self.dimension.get()))
            self.refresh()
    
    def refresh(self) :
        self.sudoku_grid.destroy()
        self.build_grid()
        self.sudoku_grid.pack(anchor="center") 
        self.window.update()

    def build_grid(self) :
        self.sudoku_grid = tk.Frame(self.window) 
        size = int(50 // self.model.get_dimension())
        colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "cyan", "magenta", "lime", "teal", "indigo", "maroon", "gold"]
        for i in range(self.model.get_dimension()) :
            for j in range(self.model.get_dimension()) :
                if self.model.get_coloration().is_colored(i * self.model.get_dimension() + j) :
                    color = colors[self.model.get_coloration().color_of(i * self.model.get_dimension() + j) % len(colors)]
                    label = tk.Label(self.sudoku_grid, text=self.model.get_coloration().color_of(i * self.model.get_dimension() + j), relief="solid", borderwidth=1, width=size, height=size // 2, bg=color)
                else:
                    label = tk.Label(self.sudoku_grid, text="", relief="solid", borderwidth=1, width=size, height=size//2, bg="white")
                label.grid(row=i, column=j, padx=2, pady=2)  

    def display(self) :
        self.window.mainloop()