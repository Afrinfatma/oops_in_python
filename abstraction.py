from abc import ABCMeta ,abstractmethod



class Shape(metaclass=ABCMeta):
    pass
    def __init__(self):
       print("Welcome to the world of Shapes")

    @abstractmethod
    def area(self):
         pass
    @abstractmethod
    def perimeter(self):
         pass

class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("Hi! this is Rectangle:")



    def area(self):
        length = int(input("enter the length:"))
        breadth = int(input("enter the breadth:"))

        print("Area of rectangle:", length * breadth)


    def perimeter(self):
        length = int(input("enter the length:"))
        breadth = int(input("enter the breadth:"))
        print("Perimeter of circle:" ,2*(length+breadth))


class Circle(Shape):
    pi = 3.14
    def __init__(self):
        Shape.__init__(self)
        print("This is Circle:")


    def area(self):
       radius = int(input("Enter the radius:"))
       print("Area of circle:", round(Circle.pi * (radius ** 2),2))


    def perimeter(self):
        radius = int(input("Enter the radius:"))
        print("Perimeter of circle:", round(2* Circle.pi *radius,2))


if __name__ == '__main__':

    rect=Rectangle()
    rect.area()
    rect.perimeter()

    circle=Circle()
    circle.area()
    circle.perimeter()
