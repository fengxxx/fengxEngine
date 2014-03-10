import math
try:
    from wx import glcanvas
    haveGLCanvas = True
except ImportError:
    haveGLCanvas = False

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
    haveOpenGL = True
except ImportError:
    haveOpenGL = False

class Vector4(object):
	def __init__(self,x,y,z,w):
		if x!=None: self._x=x
		if x!=None: self._y=y
		if x!=None: self._z=z
		if x!=None: self._w=w
		
	def __str__(self):       
		return ("(" + str(self.x)+ "," + str(self.y) + "," + str(self.z)+ "," + str(self.w)+")")
	@property
	def x(self):
	    return self._x
	@x.setter
	def x(self, value):
	    self._x = value
		
	@property
	def y(self):
	    return self._y
	@y.setter
	def y(self, value):
	    self._y = value
	@property
	def z(self):
	    return self._z
	@x.setter
	def z(self, value):
	    self._z = value

	@property
	def w(self):
	    return self._w
	@x.setter
	def w(self, value):
	    self._w = value



class Vector3(object):
	def __init__(self,x,y,z):
		if x!=None: self._x=x
		if x!=None: self._y=y
		if x!=None: self._z=z
	def __str__(self):       
		return ("(" + str(self.x)+ "," + str(self.y) + "," + str(self.z)+")")
	@property
	def x(self):
	    return self._x
	@x.setter
	def x(self, value):
	    self._x = value
		
	@property
	def y(self):
	    return self._y
	@y.setter
	def y(self, value):
	    self._y = value
	@property
	def z(self):
	    return self._z
	@x.setter
	def z(self, value):
	    self._z = value


	def distance(a,b):
		return math.sqrt((b.x-a.x)^2+(b.y-a.y)^2+(b.z-a.z)^2)

class Vector2(object):
	def __init__(self,x,y):
		if x!=None: self._x=x
		if x!=None: self._y=y
	def __str__(self):       
		return ("(" + str(self.x)+ "," + str(self.y) +")")
	@property
	def x(self):
	    return self._x
	@x.setter
	def x(self, value):
	    self._x = value
		
	@property
	def y(self):
	    return self._y
	@y.setter
	def y(self, value):
	    self._y = value


	def distance(a,b):
		return math.sqrt((b.x-a.x)^2+(b.y-a.y)^2)



class Size(object):
	def __init__(self,x,y):
		if x!=None: self._x=x
		if x!=None: self._y=y
	def __str__(self):       
		return ("(" + str(self.x)+ "," + str(self.y) +")")
	@property
	def x(self):
	    return self._x
	@x.setter
	def x(self, value):
	    self._x = value
		
	@property
	def y(self):
	    return self._y
	@y.setter
	def y(self, value):
	    self._y = value

	@property
	def width(self):
	    return self._x
	@width.setter
	def width(self, value):
	    self._x = value
		
	@property
	def heith(self):
	    return self._y
	@heith.setter
	def heith(self, value):
	    self._y = value






class gameObject():


    class transform():
        position=Vector3(0,0,0)
        rotation=Vector3(0,0,0)
        scale=Vector3(1,1,1)
        
        def move():
            print "move"
        def rotate():
            print "rotate"
        def scale():
            print "scale"

    class mesh():
        print "mesh"

    class meshRender():
        print "meshRender"




    def createPrimitives(objectType):
        if objectType=="box":
            print "box"
            glBegin(GL_QUADS)
            #glColor3f(0.78,0.78,0.78)
            glNormal3f( 0.0, 0.0, 1.0)
            glVertex3f( 0.5, 0.5, 0.5)
            glVertex3f(-0.5, 0.5, 0.5)
            glVertex3f(-0.5,-0.5, 0.5)
            glVertex3f( 0.5,-0.5, 0.5)
            #glColor3f(0,0.6,0)
            glNormal3f( 0.0, 0.0,-1.0)
            glVertex3f(-0.5,-0.5,-0.5)
            glVertex3f(-0.5, 0.5,-0.5)
            glVertex3f( 0.5, 0.5,-0.5)
            glVertex3f( 0.5,-0.5,-0.5)
            #glColor3f(0.4,0,0)
            glNormal3f( 0.0, 1.0, 0.0)
            glVertex3f( 0.5, 0.5, 0.5)
            glVertex3f( 0.5, 0.5,-0.5)
            glVertex3f(-0.5, 0.5,-0.5)
            glVertex3f(-0.5, 0.5, 0.5)
            #glColor3f(0,0.5,0.5)
            glNormal3f( 0.0,-1.0, 0.0)
            glVertex3f(-0.5,-0.5,-0.5)
            glVertex3f( 0.5,-0.5,-0.5)
            glVertex3f( 0.5,-0.5, 0.5)
            glVertex3f(-0.5,-0.5, 0.5)

            glNormal3f( 1.0, 0.0, 0.0)
            glVertex3f( 0.5, 0.5, 0.5)
            glVertex3f( 0.5,-0.5, 0.5)
            glVertex3f( 0.5,-0.5,-0.5)
            glVertex3f( 0.5, 0.5,-0.5)
            #glColor3f(0.5,0.5,0.5)
            
            glNormal3f(-1.0, 0.0, 0.0)
            glVertex3f(-0.5,-0.5,-0.5)
            glVertex3f(-0.5,-0.5, 0.5)
            glVertex3f(-0.5, 0.5, 0.5)
            glVertex3f(-0.5, 0.5,-0.5)
            glEnd()










print str(Vector2(0,1))

print str(Vector3(0,1,0))

print str(Vector4(0,1,0,5))

print str(Size(0,1))













class Singleton(object):
	_singletons = {}
	def __new__(cls, *args, **kwds):
		if not cls._singletons.has_key(cls):           
		 cls._singletons[cls] = object.__new__(cls)  
		return cls._singletons[cls]    


c=Singleton