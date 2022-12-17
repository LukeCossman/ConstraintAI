# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 18:52:47 2022

@author: majes
"""



import pandas as pd
import random as r
import os
import time


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
    
    for x in range(len(data)):
        row = data.iloc[x]
        
        name = row["Course"]
        professor = row["Professors"]
        day = row["Day"]
        room = row["Room"]
        conflicts = row["Conflicts"].split("|")
        
        ALL.append(course(name, professor, day, room, conflicts))
        
    a = data["Room"].value_counts()[223]
    print(a)    
    
    MWF = 0
    TTH = 1
    
    solution = False
    schedule = [[], []]
    
    i = 0
    timeMWF = ["8:00", "9:00", "10:00", "11:00", "12:00", "1:00", "2:00", "3:00"]
    timeTTH = ["8:00", "9:30", "11:00", "12:30", "2:00", "3:30"]
    professors = {"Ryan" : 0, "Gupta" : 0, "Houck" : 0, "Hammarsten" : 0, "Ruggles" : 0,
                  "Walsh" : 0}
    
    tries = 0
    while not solution:
        
        bad = True
        current = ALL[i]
        
        while bad:
            time_error = False
            professor_error = False
            
            #initial assign
            if current.day == "MWF":
                
                current.time = timeMWF[r.randint(0, 7)]
            
                for course in schedule[MWF]:
                    if course != current:
                        if course.time == current.time and course.room == current.time:
                            time_error = True
                        if course.time == current.time and course.name in current.conflicts:
                            time_error = True
                        if course.time == current.time and course.professor == current.professor:
                            professor_error = True
                    
            
            
            else:
                current.time = timeTTH[r.randint(0, 5)]
                
                for course in schedule[TTH]:
                    if course != current:
                        if course.time == current.time and course.room == current.room:
                            time_error = True
                        if course.time == current.time and course.name in current.conflicts:
                            time_error = True
                        if course.time == current.time and course.professor == current.professor:
                            professor_error = True
                    
            
            #If errors
            if professor_error or time_error:
                
                tries += 1
                if tries == 10:
                    tries = 0
                    i -= 1
                    if current.day == "MWF":
                        schedule[MWF].pop(-1)
                    else:
                        schedule[TTH].pop(-1)
                
            #If no error
            else:
                bad = False
                i += 1
                tries = 0
                if current.day == "MWF":
                    schedule[MWF].append(current)
                else:
                    schedule[TTH].append(current)
                
            
            
        #if done
        if i == len(ALL):
            solution = True
            
    d = {}
    d["Course"] = []
    d["Day"] = []
    d["Time"] = []
    d["Professor"] = []
    d["Room"] = []
    output = pd.DataFrame(d)
    
            
    for day in schedule:
        for course in day:
            
            output.loc[len(output.index)] = [course.name, course.day,
                                             course.time, course.professor,
                                             course.room]
            
    
    print(output)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    