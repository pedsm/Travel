import random
import math
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

cities = [city('Mandala city',20,30)]
addCity("New city",40,50)

# city generator
print "Generating 10 cities"
for i in range(10):
    x = random.randint(0,100)
    y = random.randint(0,100)
    addCity("City " + str(i), x, y)


# print all city names
for city in cities:
    print (city.name,city.x,city.y)


