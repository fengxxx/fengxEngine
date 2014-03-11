from  _globalData import *
import math
import wx
from _core import *


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

class openGL_BasicCanvas(glcanvas.GLCanvas):
    global ANGLE
    global EYE_POS
    global TARGET_POS
    global PI

    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1,size=(100,100))
        self.init = False
        self.context = glcanvas.GLContext(self)
        
        # initial mouse position
        self.lastx = self.x = 0
        self.lasty = self.y = 0
        self.size = None
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)

    def OnEraseBackground(self, event):
        pass # Do nothing, to avoid flashing on MSW.


    def OnSize(self, event):
        size=self.GetClientSize()
        b=size.width/(size.height+0.0)
        #print b
        #gluPerspective(0,b,1,60)
        wx.CallAfter(self.DoSetViewport)
        event.Skip()

    def DoSetViewport(self):
        size = self.size =self.GetClientSize()
        a=min( size.width, size.height)
        b=size.width/(size.height+0.0)
        glViewport(0, 0, a, a)
        #glViewport(0,0,1000,1000)


    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
       


    def OnMouseDown(self, evt):
        #self.CaptureMouse()
        self.x, self.y = self.lastx, self.lasty = evt.GetPosition()
        self.lastx, self.lasty = evt.GetPosition()

    def OnMouseUp(self, evt):
        #self.ReleaseMouse()
        print ""

    def OnMouseMotion(self, evt):
        global ANGLE
        global ANGLE_UP
        global SPEED
        if evt.Dragging() and evt.RightIsDown():
            
            self.x, self.y = evt.GetPosition()

            ex=self.x-self.lastx
            ey=self.y-self.lasty

            ANGLE +=ex*0.2
            ANGLE_UP +=ey*0.2
            rad =PI*ANGLE/180.0
            rad_UP =PI*ANGLE_UP/180.0
            print ex
            print TARGET_POS
            TARGET_POS[1] = EYE_POS[1] + 100*(-math.cos(rad_UP))
            TARGET_POS[0] = EYE_POS[0] + 100*math.cos(rad)    
            TARGET_POS[2] = EYE_POS[2] + 100*math.sin(rad)   
            print TARGET_POS

            self.move()



            self.lastx, self.lasty = evt.GetPosition()
            self.Refresh(False)



    def OnKeyDown(self, evt):
        key=chr(evt.GetKeyCode())
        global ANGLE
        global TARGET_POS 
        global EYE_POS
        
        if key=="D":
            ANGLE +=1.1
            rad =PI*ANGLE/180.0
            #TARGET_POS[0] = EYE_POS[0] + 100*math.cos(rad)    
            #TARGET_POS[2] = EYE_POS[2] + 100*math.sin(rad)
            #TARGET_POS[1] = EYE_POS[1];
            EYE_POS[2] -= math.cos(rad) * SPEED 
            EYE_POS[0] -= -math.sin(rad) * SPEED
            self.move()

        if key=="A":
            ANGLE -=1.1
            rad =PI*ANGLE/180.0
            #TARGET_POS[0] = EYE_POS[0] + 100*math.cos(rad)    
            #TARGET_POS[2] = EYE_POS[2] + 100*math.sin(rad)
            #TARGET_POS[1] = EYE_POS[1];
            EYE_POS[0] += math.sin(rad) * SPEED
            #EYE_POS[2] += math.sin(rad) * SPEED


            self.move()
        if key=="W":

            rad =PI*ANGLE/180.0
            EYE_POS[2] += math.sin(rad) * SPEED
            EYE_POS[0] += math.cos(rad) * SPEED
            #TARGET_POS[0] = EYE_POS[0] + 100*math.cos(rad)    
            #TARGET_POS[2] = EYE_POS[2] + 100*math.sin(rad)
            #TARGET_POS[1] = EYE_POS[1];
            self.move()
        if key=="S":
 
            rad =PI*ANGLE/180.0
            EYE_POS[2] -= math.sin(rad) * SPEED
            EYE_POS[0] -= math.cos(rad) * SPEED
            #TARGET_POS[0] = EYE_POS[0] + 100*math.cos(rad)    
            #TARGET_POS[2] = EYE_POS[2] + 100*math.sin(rad)
            #TARGET_POS[1] = EYE_POS[1];
            self.move()
        if key=="E":
            
            EYE_POS[1] +=SPEED
            TARGET_POS[1] +=SPEED
            self.move()
        if key=="Q":
            EYE_POS[1] -=SPEED
            TARGET_POS[1] -= SPEED
            self.move()
        if key=="F":
            EYE_POS=[1,1,1]
            TARGET_POS=[0,0,0]
            self.move()

        if key=="-":
            global SPEED
            SPEED-=0.1

        if key=="=":
            global SPEED
            SPEED+=0.1
    def OnKeyUp(self, evt):
        key=evt.GetKeyCode()
        print chr(key)


    def  move(self):
        glLoadIdentity()
        gluLookAt(EYE_POS[0],EYE_POS[1], EYE_POS[2],  TARGET_POS[0],TARGET_POS[1] ,TARGET_POS[2], 0,1,0)
        self.Refresh(False)



class mainGlCanvas(openGL_BasicCanvas):
    def InitGL(self):
        # set viewing projection
        glMatrixMode(GL_PROJECTION)
        size = self.size =self.GetClientSize()
        #a=min( size.width, size.height)/max( size.width, size.height)
        glFrustum(-1, 1, -1, 1, 1.0, 1000)
        # position viewer
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -2.0)

        # position object
        #glRotatef(self.y, 1.0, 0.0, 0.0)
        #glRotatef(self.x, 0.0, 1.0, 0.0)


        a = 0.217
        b = 0.342
        c = 0.537
        d = 0.24

        glClearColor (a,a,a,1)

        glEnable(GL_DEPTH_TEST)
        #glEnable(GL_LIGHTING)
        #glEnable(GL_LIGHT1)


   

        glShadeModel(GL_FLAT)
        glShadeModel(GL_SMOOTH)


        lightIntensity=1

        #-----------------------light
        LightAmbient= (0.1, 0.15, 0.2, 1.0 )
        LightDiffuse=     (lightIntensity,lightIntensity, lightIntensity, 1.0 )
        LightPosition=    ( 2, 2, 2, 1.0 )
        Light_Model_Ambient = (0, 0, 0, 1.0)
        LightSpecular=    (1.0, 1.0, 1.0, 1.0)
        MaterialSpecular = ( 1.0,1.0,1.0,1.0 )

        glLightfv(GL_LIGHT1,GL_SPECULAR, LightSpecular)

        glMaterialfv(GL_FRONT,GL_SPECULAR,MaterialSpecular)

        glMaterialf(GL_FRONT,GL_SHININESS,128)

        glLightfv(GL_LIGHT1, GL_AMBIENT, LightAmbient)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, LightDiffuse)
        glLightfv(GL_LIGHT1, GL_POSITION,LightPosition)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, Light_Model_Ambient)


        glEnable(GL_LIGHT1)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        #-----------------------light


    def OnDraw(self):
        # clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # draw six faces of a cube

        self.box()
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glScale(0.1,0.1,0.2)
        glTranslatef(1,0.2,0)
        
        glPopMatrix()
        if self.size is None:
            self.size = self.GetClientSize()
 
        w, h = self.size
        w = max(w, 1.0)
        h = max(h, 1.0)
        xScale = 180.0 / w
        yScale = 180.0 / h
        glTranslatef(5,0,0)
        #glRotatef((self.y - self.lasty) * yScale, 1.0, 0.0, 0.0);
        #glRotatef((self.x - self.lastx) * xScale, 0.0, 1.0, 0.0);
   
        xl=10
        yl=10
        zl=10


        glBegin(GL_LINES)
        self.xyz()
        self.grid()
        glEnd()
 

        tpos=[0,0,0]
        sc=1.2
        big=1
        glScale(big,big,big)
        glTranslatef(-xl*sc/2,-yl*sc/2,-zl*sc/2)
        for ix in range(0,xl):
            for iy in range(0,yl):
                for iz in range(0,zl):
                    glColor3f(ix*0.1,iy*0.1,iz*0.1)
                    glTranslatef((ix-tpos[0])*sc,(iy-tpos[1])*sc,(iz-tpos[2])*sc)
                    
                    tpos=[ix,iy,iz]
                    self.box()
                    


        #glMatrixMode(GL_MODELVIEW)


       

  
        #self.OnDraw()

        self.SwapBuffers()

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



def loadOBJ(filename): 
    numVerts = 0 
    verts = [] 
    norms = [] 
    vertsOut = [] 
    normsOut = [] 
    for line in open(filename, "r"): 
        #vals = line.split(" ") 
        l=line.split("\n")
        #print l
        vals=l[0].split(" ")
        if vals[0] == "v": 
            v = map(float, vals[2:5]) 
            verts.append(v) 
        if vals[0] == "vn": 
            n = map(float, vals[2:5]) 
            norms.append(n) 
        if vals[0] == "f": 
            for f in vals[1:]: 
                w = f.split("/") 
                # OBJ Files are 1-indexed so we must subtract 1 below 
                vertsOut.append(list(verts[int(w[0])-1])) 
                normsOut.append(list(norms[int(w[2])-1])) 
                numVerts += 1
        
    return vertsOut, normsOut


print loadOBJ("C:\\Users\\fengx\Desktop\\temp.obj")[0]