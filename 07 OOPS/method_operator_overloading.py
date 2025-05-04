class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self,p):
        return Point(self.x+p.x,self.y+p.y)
    
    def print_point(self):
        print(f"x is {self.x} and y is {self.y}")

    def __add__(self,p):
        return Point(self.x+p.x,self.y+p.y)


p1 = Point(3,2)
p2 = Point(6,3)

p3 = p1.sum(p2)
p3.print_point()

p4 = p1+p2  ## We overloaded the + operator with __add__ function
p4.print_point()