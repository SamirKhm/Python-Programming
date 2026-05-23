class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def sum(self,p):
        return Point(self.x+p.x,self.y+p.y)
    
    def print_point(self):
        print(f"({self.x},{self.y})")

    def __add__(self,p):
        return Point(self.x+p.x,self.y+p.y)

p1=Point(2,3)
p2=Point(4,5)

p3=p1.sum(p2)
p3.print_point()
print(p3.x) # Output: 6
print(p3.y) # Output: 8

p4=p1+p2
p4.print_point() # Output: (6,8)
# __add__ - is a special method in Python that is used to define the behavior of the addition operator (+) for a class. By implementing the __add__ method, we can specify how two objects of the class should be added together when the + operator is used. In this example, we have defined the __add__ method to return a new Point object that represents the sum of the x and y coordinates of the two Point objects being added.