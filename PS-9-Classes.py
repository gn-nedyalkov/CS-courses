# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *
list_of_shapes='25995745d6fc211df42f9485592ff037_shapes.txt'
class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle():
    def __init__(self,base,height):
        self.base=float(base)
        self.height=float(height)
    def area(self):
        return self.base*self.height/2
    def __str__(self):
        return 'Triangle with base %s and height %s' %(self.base,self.height)
    def __eq__(self,other):
        return type(other)==Triangle and self.height==other.height and self.base==other.base

#
# Problem 2: Create the ShapeSet class

# TO DO: Fill in the following code skeleton according to the
#    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.set=[]
        self.place=None
        ## TO DO
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        for shape in self.set:
            if shape==sh:
                print('A ne be')
                return "Shape already in set"
            
        self.set.append(sh)
        ## TO DO
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place=0
        return self
    def next(self):
         if self.place >= len(self.set):
           raise StopIteration
         self.place += 1
         return self.set[self.place-1] 
        ## TO DO
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        res=[]
        for shape in self.set:
            res.append(str(shape))
        return '\n'.join(res)
        ## TO DO
tr1=Triangle(3,4)
cr1=Circle(5)   
sq1=Square(5)
set1=ShapeSet()
set1.addShape(tr1) 
set1.addShape(sq1)  
set1.addShape(cr1)
set1.addShape(tr1)

#
# Problem 3: Find the largest shapes in a ShapeSet

def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
        largest area.
    shapes: ShapeSet
    """
    max1=0
    max_list=[]
    for shape in shapes.set:
        if shape.area()>max1: max_list=[shape]
        if shape.area()==max1: max_list.append(shape)
    
    return tuple(max_list)
    ## TO DO
largest=findLargest(set1) 
for i in largest:
    print(i)
largest[0] is cr1
#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    shape_set=ShapeSet()
    input_file=open(filename)
    for line in input_file:
        info=line.split(',')
        if str(info[0])=='circle': 
            sh=Circle(info[1])
            shape_set.set.append(sh)
        elif str(info[0])=='square': 
            sh=Square(info[1])
            shape_set.set.append(sh)
        elif str(info[0])=='triangle': 
            sh=Triangle(info[1],info[2])
            shape_set.set.append(sh)
    return shape_set
    ## TO DO
shape_set= readShapesFromFile(list_of_shapes)