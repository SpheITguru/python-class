from Circle import Circle

def main():
    circle1 = Circle()
    #print("The area of the circle of radius ",\
    #    circle1.radius, " is ", circle1.getArea())
    circle2 = Circle(25)
    #circle2.radius = 100
    print("Circle 2 radius is: ", circle2.radius)

if __name__ == '__main__':
    main()