# dodecahedron dice, 9 groups, each one goes once
# on average how many rolls will it take to get all 9 groups at least once
# simulation
# expected: 25.5, 9!*((9/12)*(8/12)*(7/12)*...*(1/12))
# updated expected after seeing numbers: 33.95, 12/9+12/8+...+12/1

import math
import random

l = []


def allgroupspicked(l):
    for x in range(1, 10):
        if l.count(x) == 0:
            return 0
            break
    return 1


def simulation(n):  # simlulate rolls until all 9 are rolled, n times
    sims = 0
    simlist = []
    while sims < n:
        rolls = 0
        l = []
        while allgroupspicked(l) == 0:
            l.append(random.randint(1, 12))
            rolls += 1
        simlist.append(rolls)
        sims += 1
    mean = sum(simlist) / len(simlist)
    print(mean)
    s = 0
    for x in simlist:
        s = s + (x - mean) ** 2
    t = (mean - 33.9476190476) * math.sqrt(len(simlist)) / s
    print("t-score=%s" % (t))


n = int(input("number of simulations?"))
simulation(n)
