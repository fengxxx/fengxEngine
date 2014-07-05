"""
from  _globalData import *
import math
import wx
from _core import *




try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
    haveOpenGL = True
except ImportError:
    haveOpenGL = False

def box(self):

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
def xyz(self):
    a=15
    glColor3f(0,0,1)
    glVertex3d(0, 0, -a)
    glVertex3d(0, 0, a)
    glColor3f(0,1,0)
    glVertex3d(a, 0, 0)
    glVertex3d(-a, 0, 0)
    glColor3f(1,0,0)
    glVertex3d(0, -a, 0)
    glVertex3d(0, a, 0)

def grid(self):
    num=200
    j=num*0.001#0.08#l/10
    l=j*(num-1)/2
    for i in range(num):
        if i == ((num-1)/2):
            glColor3f(0.1,0.1,0.1)
        else:
            glColor3f(0.6,0.6,0.6)
            glVertex3d(-l, 0, i * j - l)
            glVertex3d(l, 0,i * j - l)
            glVertex3d(i * j - l, 0,l)
            glVertex3d(i * j - l, 0,-l)

"""

def loadOBJ(filename): 
    numVerts = 0 
    vertexs = []
    faces=[] 
    norms = [] 
    vertsOut = [] 
    normsOut = [] 
    f=open(filename)
    #line=f.readline()

    for line in f: 
        #print line
        vals=line.replace("\n","").split(" ")
        #print vals
        if vals[0] == "v":
            #print vals 
            v = map(float, vals[2:6]) 
            vertexs.append(v) 
            #print v
        elif vals[0] == "vn": 
            n = map(float, vals[2:6]) 
            norms.append(n) 
        elif vals[0] == "f": 
            for f in vals[1:]: 
                w = f.split("/")
                faces.append(int(w[0])-1)
                #print w
                #print w[0] 
                # OBJ Files are 1-indexed so we must subtract 1 below 
                #vertsOut.append(list(verts[int(w[0])-1])) 
                #normsOut.append(list(norms[int(w[0])-1])) 
                numVerts += 1
    return vertexs, faces  
    f.close()

#print loadOBJ("D:/desktop/testObj.obj")[1]