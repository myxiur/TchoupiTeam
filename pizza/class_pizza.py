# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:48:20 2018

@author: César
"""
import time
import os
import math

class Part:
    
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

class Pizza:
    
    def __init__(self, w, h, mini, area, pizza):
        self.listPart = []
        self.w = w
        self.h = h
        self.mini = mini
        self.area = area
        self.pizza = pizza

    def slicep(self, pizza,x,y,x1,y1):
        if x >= len(pizza[0]) or y >= len(pizza):
            return False
        if x < 0 or y < 0:
            return False
        if x1 >= len(pizza[0]) or y1 >= len(pizza):
            return False
        
        newPart = Part(x,y,x1,y1)
        nbt, nbm = self.partOfPizza(newPart)
        if nbt < self.mini or nbm < self.mini:
            return False
        
        if not self.checkTaken(newPart):
            self.listPart.append(newPart)
        return True
    
    def checkTaken(self,partofPizza):
        for i in self.listPart:
            if partofPizza.x0 >= i.x0 and partofPizza.x0 <= i.x1 and partofPizza.y0 >=i.y0 and partofPizza.y0 <= i.y1:
                return True
            if partofPizza.x1 >= i.x0 and partofPizza.x1 <= i.x1 and partofPizza.y1 >=i.y0 and partofPizza.y1 <= i.y1:
                return True
        return False
    
    def compute_score(self):
        score = 0
        for i in self.listPart:
            score += (abs(i.x1 - i.x0) + 1) * (abs(i.y1 - i.y0) + 1)
        return score

    def Save(self):
        returnString = ""
        returnString += str(len(self.listPart)) +"\n"
        for i in self.listPart:
            returnString += str(i.x0) + " " + str(i.x1) + " " + str(i.y0) + " " + str(i.y1) + "\n"

        if not os.path.exists("results"):
            os.makedirs("results")
        fichier = open("results/result_"+ str(time.time())+ "_"+str(0)+".txt","w")
        fichier.write(returnString)
        fichier.close()
        return None

    def partOfPizza(self, partofPizza):
        nbT = 0
        nbM = 0
        for i in range(partofPizza.x0, partofPizza.x1 + 1):
            for j in range(partofPizza.y0, partofPizza.y1 + 1):
                if self.pizza[j][i] == 'T':
                    nbT += 1
                else:
                    nbM += 1
        return nbT, nbM
            
                    
                    
    
    
    
