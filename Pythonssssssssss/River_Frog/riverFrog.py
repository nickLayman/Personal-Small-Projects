import numpy
import random

width = 10
pos = 0


def jump():
    global width
    global pos
    
    pos += random.randint(1, width - pos)
    

def trial():
    global width
    global pos
    
    pos = 0
    jumps = 0
    
    while pos < width:
        jump()
        jumps += 1
        
    return jumps


def manyTrials(num):
    trials = []
    
    for x in range(num):
        trials.append(trial())
    
    return trials
        

def avgTrials(num):
    trialSum = 0
    
    for x in range(num):
        trialSum += trial()
        
    return trialSum / num


print(avgTrials(500000))
