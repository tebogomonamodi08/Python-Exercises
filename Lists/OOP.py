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


    