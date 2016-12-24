import random
import math
from itertools import permutations
class city(object):
    """Object for a city """

    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

def addCity(name,x,y):
    """Adds a city to the cities array

    :name: City Name
    :x: x position of the city
    :y: y position of the city
    :returns: returns the new City object

    """
    tmp = city(name,x,y)
    cities.append(tmp)

def calcDistance(city1,city2):
    """TODO: Docstring for distance.

    :city1: City 1 object
    :city2: City 2 object
    :returns: returns the distance value of a straight line between cities

    """
    deltaX = math.pow(abs(city1.x - city2.x),2)
    deltaY = math.pow(abs(city1.y - city2.y),2)

    tmp = math.sqrt(deltaX+deltaY)
    return tmp

cities = []
cityNum = 10 
worldSize = 100
# city generator
print "Generating 10 cities"
for i in range(cityNum):
    x = random.randint(0,worldSize)
    y = random.randint(0,worldSize)
    addCity("City " + str(i), x, y)

# start the permutations
min = worldSize*worldSize 
lazy = False
for p in permutations(cities):
    total = 0
    for i in range(1,len(p)):
        total = total + calcDistance(p[i-1],p[i])
        if total > min:
            lazy = True
            break

    if lazy:
        continue

    # add the way back
    total = total + calcDistance(p[0],p[len(p)-1])
    if total < min or min == 0:
        min = total
        print "New min distance:" + str(total)
        print "Route:"
        for city in p:
            print city.name
