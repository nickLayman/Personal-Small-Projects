import math
import random


class Destination:
    name: str
    x: float
    y: float

    def __init__(self, pname, xcoord=0, ycoord=0):
        self.name = pname
        self.x = xcoord
        self.y = ycoord


def d(first: Destination, second: Destination):
    x1 = first.x
    x2 = second.x
    y1 = first.y
    y2 = second.y
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def E(path: list):
    length = 0
    for i in range(len(path)-1):
        length += d(path[i], path[i+1])
    length += d(path[-1], path[0])
    return length


def P(curr_path, prop_path, curr_temp):
    es = E(curr_path)
    esp = E(prop_path)
    t = curr_temp
    if esp <= es:
        return 1
    else:
        return 0  # math.exp(-(esp - es) / t)


def temp(time):
    return max_d*(1-time)


def swap(path: list, i1, i2):
    temp = path.copy()
    temp[i1], temp[i2] = temp[i2], temp[i1]
    return temp


def neighbor(path, time):
    i1 = random.randrange(len(path))
    i2 = random.randrange(len(path))
    while i1 == i2:
        i2 = random.randrange(len(path))
    for i in range(50):
        if d(path[i1], path[i2]) > temp(time):
            i1 = random.randrange(len(path))
            i2 = random.randrange(len(path))
            while i1 == i2:
                i2 = random.randrange(len(path))
    return swap(path, i1, i2)


trip = []
for y in range(10):
    trip.append(Destination(f"0{y}", 0, y))
    trip.append(Destination(f"9{y}", 9, y))
for x in range(1, 9):
    trip.append(Destination(f"{x}0", x, 0))
    trip.append(Destination(f"{x}9", x, 9))
# for i in range(100):
#     trip.append(Destination(f"{i}", random.randint(0, 10),
#                             random.randint(0, 10)))

random.shuffle(trip)
print(E(trip))

max_d = math.sqrt(200)
for k in range(500):
    t = temp(k/500)
    trip_new = neighbor(trip, k/500)
    if P(trip, trip_new, t) >= random.random():
        trip = trip_new
        print(E(trip))

print(E(trip))
