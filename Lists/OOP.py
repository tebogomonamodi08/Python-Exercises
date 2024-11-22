#Object-Oriented-Programming
################################################################################################
#We are going to explore object oriented programming.
#The main idea is to create an explicit relationship between classes and object, modelling problems into physical objects
#Encapsulating object and classes.
#classes are blueprints of objects
#look at the example below, creating a point type, that will represent points on a 2-D space.

class Point:
    '''This class will represent a point on a 2-D space'''

#creating an object
point = Point() #instantation
#print(point)
point.x = 2.4
point.y = 1.3
x = point.x
#print(x) There is no conflict between variable x and attribute x

#You can pass an object as an argument to a function so that you access its attributes
def print_point(point):
    '''This function will print the point of object: point'''
    print(point.x,point.y, end=' ')

#Exercise create a function named distance_between_point that takes in a object as argument and returns the distance between the points.
def distance_between(ob):
    '''this function takes an object as a parameter, and returns the distance between attribute x and y'''
    return ob.y - ob.x

#print(distance_between(point))

#Making decisions on the kind of attribute to use for a problem, the Rectangle problem.
class Rectangle:
    '''
    This is a class to represent a rectangle.
    attributes: width, height, point(we already created a point class)
    '''

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.point = Point() #create an object named box.point
box.point.x = 4 
box.point.y = 1

#return an instance
def find_center(rect):
    p = Point()
    p.x = rect.point.x - rect.width/2
    p.y = rect.point.y - rect.height/2
    return p

#Objects are mutable once you have created them you can change their attributes.
def increase_box(shape, shape_height, shape_width):
    shape.point.x += shape_width
    shape.point.y += shape_height

increase_box(box, 4, 3)
print(box.point.y)

book = Rectangle()
book.width = 23
book.height = 51
book.point = Point()
def move_rectangle(rect, dx, dy):
    rect.point.x += dx
    rect.point.y += dy
move_rectangle(book, 3,4)
