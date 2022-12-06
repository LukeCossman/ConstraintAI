# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 18:52:47 2022

@author: majes
"""

#What's so funny about sussus amogus

import pandas as pd
import random as r
import os

class course():
    def __init__(self, name="", professor="", day="", room=0, conflicts=[], time=0):
        self.name = name
        self.professor = professor
        self.major = name.split("-")[0]
        self.day = day
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
                
        
if __name__ == "__main__":
     
    ALL = []
    data = pd.read_csv("input.csv")
    
    for i in range(len(data)):
        row = data.iloc[0]
        
        name = row["Course"]
        professor = row["Professors"]
        day = row["Day"]
        room = row["Room"]
        conflicts = row["Conflicts"].split("|")
        
        ALL.append(course(name, professor, day, room, conflicts))
        
        
    MWF = 0
    TTH = 1
    
    solution = False
    schedule = [[], []]
    
    i = 0
    timeMWF = [800, 900, 1000, 1100, 1200, 100, 200, 300]
    timeTTH = [800, 930, 1100, 1230, 200, 330]
    professors = {"Ryan" : 0, "Gupta" : 0, "Houck" : 0, "Hammarsten" : 0, "Ruggles" : 0,
                  "Walsh" : 0}
    
    while not solution:
        
        bad = True
        current = ALL[i]
        while bad:
            time_error = False
            professor_error = False
            
            #initial assign
            if current.day == "MWF":
                
                current.time = timeMWF[r.randint(0, 7)]
                professors[current.professor] += 1
            
                for course in schedule[MWF]:
                    if course.time == current.time and course.room == current.time:
                        time_error = True
                    if course.time == current.time and course.name in current.conflicts:
                        time_error = True
                    if course.time == current.time and course.professor == current.professor:
                        professor_error = True
            
            
            else:
                current.time = timeMWF[r.randint(0, 5)]
                professors[current.professor] += 1
                
                for course in schedule[TTH]:
                    if course.time == current.time and course.room == current.time:
                        time_error = True
                    if course.time == current.time and course.name in current.conflicts:
                        time_error = True
                    if course.time == current.time and course.professor == current.professor:
                        professor_error = True
                
            
            for day in schedule:
                for p in professors:
                    if professors[p] > 5:
                        professor_error = True
            
            
            if not (professor_error or time_error):
                bad = False
                i += 1
                if current.day == "MWF":
                    schedule[MWF].append(current)
                else:
                    schedule[TTH].append(current)
            
        #if done
        if i == len(ALL):
            solution = True
            
            
    for day in schedule:
        for course in day:
            print(course)
    
        
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    