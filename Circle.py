import math
#from pickletools import read_unicodestring1

class Circle:
    def __init__(self, radius=1):
        self.__radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi
    
    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getRadius(self):
        return self.__radius

    '''def setRadius(self, radius):
        self.radius = radius'''

