from Circle import Circle

def main():
    circle1 = Circle()
    #print("The area of the circle of radius ",\
    #    circle1.radius, " is ", circle1.getArea())
    circle2 = Circle(100)
    #circle2.radius = 100
    print("Circle 2 radius is: ", circle2.getRadius())
    print("The Area of Radius: ",circle2.getRadius(), " is :",round(circle2.getArea(),3))

if __name__ == '__main__':
    main()