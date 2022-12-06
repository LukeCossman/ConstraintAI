# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 18:52:47 2022

@author: majes
"""


class course():
    def __init__(self, name="", professor="", days="", room=0, conflicts=[], time=0):
        self.name = name
        self.professor = professor
        self.major = name.split("-")[0]
        self.days = days
        self.room = room
        self.conflicts = conflicts
        self.time = time
        
    def __str__(self):
        return self.name
        
    def has_conflict(self, other):
        if other.name in self.conflicts:
            return True
        else:
            return False
        
class stack():
    def __init__(self):
        self.size = 0
        self.list = []
        self.top = None
        
    def __str__(self):
        s = ""
        for i in self.list:
            s = s + str(i) + " "
        return s
        
    def add(self, new):
        self.list.append(new)
        self.size += 1
        self.top = new
        
    def pop(self):
        self.list.pop(-1)
        self.size -= 1
        self.top = self.list[-1]

    def clear(self):
        self.list.clear()
        self.size = 0
        self.top = None
        
        
        
if __name__ == "__main__":
    
    MWF = stack()
    TTH = stack()
    
    #Course name, professor, preferable days, classroom
    #"CS-115|Dr. Ryan|MWF|223"
    c = input()
    ALL = []
    while c != "quit":
        c = c.split("|")
        name = c[0]
        professor = c[1]
        days = c[2]
        room = c[3]
        new = course(name, professor, days, room)
        ALL.append(new)
        c = input()
    
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    
    solution = False
    [[], [], [], [], []]
    
        
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    