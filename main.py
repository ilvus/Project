from copy import deepcopy
from secrets import choice
import tkinter as tk
import random 

class Matrix:
    def __init__(self,canvas, n, m, monster, width, height):
        self.canvas = canvas
        self.n = n
        self.m = m
        self.number_monster = monster
        self.width = width
        self.height = height
        self.h = height/n
        self.w = width/m
        self.a = []
        self.monsters = []
        
        self.a.append([2 for i in range(m+2)])
    
        for i in range(n):
            row = [2] 
            for j in range(m):
                row.append(random.choice([0,1]))
        
            row.append(2)
      
            self.a.append(row)
      
        self.a.append([2 for i in range(m+2)])
        self.create_monster()
        self.draw()
    
    
    
    def draw(self):
        y=0
        self.canvas.delete('all')
        for i in range(1, self.n + 1):
            x = 0  
            for j in range(1, self.m + 1):
                if self.a[i][j] == 1:
                    color = 'grey'
                elif self.a[i][j] == 3:
                    color = 'red'
                else:
                    color = 'white'
                self.canvas.create_rectangle(
                    x, y, x + self.w, y + self.h, fill=color
                )
                x += self.w
            y += self.h
        self.check()
        self.move_monster()
        self.canvas.after(500, self.draw)
        
        
        
    def create_monster(self):
       
        for i in range(self.number_monster):
            b = random.randint(0, self.n)
            c = random.randint(0, self.m)
            self.monsters.append((b,c))
            self.a[b][c] = 3
            
            
    def move_monster(self):
        for i in range(self.number_monster):
            
            self.a[self.monsters[i][0]][self.monsters[i][1]] = 0
            try:
                self.monsters[i] = (self.monsters[i][0]+choice([0,-1,1]),self.monsters[i][1]+choice([0,-1,1]))
            except:
                pass
            self.a[self.monsters[i][0]][self.monsters[i][1]] = 3
    
        
        
        
        
    def check(self):
        self.copy = deepcopy(self.a)
        
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                nn = 0
                if self.a[i][j] == 3:
                    continue
                
                a = self.copy[i+1][j] 
                if a == 1:
                    nn += 1
                elif a == 3:
                    self.a[i][j] = 0
                    continue
                
                a = self.copy[i+1][j+1]
                if a == 1:
                    nn += 1
                elif a == 3:
                    self.a[i][j] = 0
                    continue
                
                a = self.copy[i][j+1]
                if a == 1:
                    nn += 1
                elif a == 3:
                    self.a[i][j] = 0 
                    continue
                
                a = self.copy[i-1][j+1]
                if a == 1:
                    nn += 1
                elif a == 3:
                    self.a[i][j] = 0 
                    continue
                
                a = self.copy[i-1][j]
                if a == 1:
                    nn += 1
                elif a == 3:
                    self.a[i][j] = 0 
                    continue
                
                a = self.copy[i-1][j-1] 
                if a == 1:
                    nn += 1
                elif a == 3:
                    self.a[i][j] = 0 
                    continue
                
                a = self.copy[i][j-1] 
                if a == 1:
                    nn += 1
                elif a == 3:
                    self.a[i][j] = 0
                    continue
                
                a = self.copy[i+1][j-1]
                if a == 1:
                    nn += 1
                elif a == 3:
                    self.a[i][j] = 0
                    continue
                
                
                if nn not in (2,3):
                    self.a[i][j] = 0
                elif nn == 3:
                    self.a[i][j] = 1
                    
                    
    def get_matrix(self):
        for i in self.a:
            print(i)


root = tk.Tk()
root.geometry('900x900')
canvas = tk.Canvas(root, width=900, height=900)
canvas.pack()

mat = Matrix(canvas, 50, 50, 5, 900, 900)

root.mainloop()
