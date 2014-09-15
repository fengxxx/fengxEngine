import math
from vector3 import*
from vector2 import*
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

class Vector3x(object):
    '''
    def __new__(self):
        self._x=0.0
        self._y=0.0
        self._z=0.0
    '''

    def __init__(self,x,y,z):
        if x!=None: self._x=x 
        if y!=None: self._y=y
        if z!=None: self._z=z
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

class Vectorx(object):
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
    def growx(self,l):
        nx=l/math.sqrt(self.x**2(self.y**2-1)-self.y**2+1)
        ny=nx*self.x/self.y
        nv=Vector2(nx,ny)
    @classmethod
    def test(self):
        return self.x
    def grow(self,l):
        print math.sqrt(self.x**2*(self.y**2-1)-self.y**2+1) 
        nx=l/math.sqrt(self.x**2*(self.y**2-1)-self.y**2+1)
        ny=nx*self.x/self.y
        return Vectorx(nx,ny)
        '''
    len
        def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)
     def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)
'''

class Vector2c(object):
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    

    def __str__(self):
        return ("(" + str(self.x)+ "," + str(self.y) +")")



    @classmethod
    def pointToVector(self,p1,p2):
        return self(p1[0]-p2[0],p1[1]-p2[1])
    def getLength(self):
        return math.sqrt(self.x**2+self.y**2) 
    def normalize(self):
        l=self.get_Length
        self.x/=l
        self.y/=l

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
    def growx(self,l):
        nx=l/math.sqrt(self.x**2(self.y**2-1)-self.y**2+1)
        ny=nx*self.x/self.y
        nv=Vector2(nx,ny)
    @classmethod
    def test(self):
        print str(self.x)
        #print self._x
    def grow(self,length):
        print length/math.sqrt(self.x**2*(self.y**2-1)-self.y**2+1)
        #ny=nx*self.x/self.y
        #return Vector2(nx,ny)
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

class Mesh(object):
    def __init__(self, arg):
        super( Mesh, self).__init__()
        self.arg = arg
    renderEnable=True
    name=" " 
    vertexs=[]
    egdes=[]
    colors=[]
    normals=[]
    uvs=[]
    faces=[]
    smoothGroup=[]
    groupName=[]
    materials=[]
class Line(object):
    def __init__(self, arg):
        super( Line, self).__init__()
        self.arg = arg
    name="line"
    renderEnable=True
    vertexs=[]
    colors=[]
    index=[]
    
class Material(object):
    name="material"
    def __init__(self,n):
        if n!=None: self.name=n

    shader="shader"
    #just test 
    diffuseMap=""
    

class Transform(object):
    name="transform"
    active=True

    position=Vector3(0,0,0)
    rotation=Vector3(0,0,0)
    scale=Vector3(1,1,1)
    
    def __init__(self,n):
        if n!=None: self.name=n


    def move():
        print "move"
    def rotate():
        print "rotate"
    def scale():
        print "scale"

class GameObject(object):
    tag=0
    id=1
    name="GameObject"
    Parent=[]
    childs=[]
    transform=Transform("xx")
    mesh=Mesh("xx")

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



class ModelObject(object):
    #i=0
    #def __init__(self):
    #    self.i+=1
    name="mdoelObject"
    renderEnable=True
    transform=Transform("transform")
    #transform.position.x=i
    mesh=Mesh("mesh")
    line=Line("line")
    material=Material("material")



#f=[(1,2,3,4,5,6,7,8,9),(3,6,5,4),(9,8,6,4)]
def getEgdeFromFace(faces):
    egdes=[]
    for s in faces:
        for i in range(0,len(s)):
            if i==len(s)-1:
                tempE=(s[i][0],s[0][0])
                if tempE not in egdes:
                    egdes.append(tempE)               
            else:
                tempE=(s[i][0],s[(i+1)][0])
                if tempE not in egdes:
                    egdes.append(tempE)
    return egdes

            

#test

#a=Vectorx(31.0,9.0)


#print a.grow(4)
#print a.getLength()



