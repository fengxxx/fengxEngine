from  _globalData import *
import math
import wx
from _core import *
from _data import *
import array
import Image
import random
import _import_obj as objFile
import primitives2obj_tool as po 
import os
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
        self.size=self.GetClientSize()
        b=self.size.width/(self.size.height+0.0)
        #print b
        gluPerspective(120,b,1,1000)
        #glFrustum(-0.1*b, 0.1*b, -0.1, 0.1, 0.1, 1000)
        wx.CallAfter(self.DoSetViewport)
        event.Skip()

    def DoSetViewport(self):
        
        self.size=self.GetClientSize()

        glViewport(0, 0, self.size.width, self.size.height)

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
        ()

    def OnMouseMotion(self, evt):
        global SPEED
        global rSPEED
        global EYE_POS
        global TARGET_POS
        if evt.Dragging() and evt.RightIsDown():
            self.x, self.y = evt.GetPosition()
            ex=self.x-self.lastx
            ey=self.y-self.lasty
            uDir=Vector2(TARGET_POS[1]-EYE_POS[1],TARGET_POS[0]-EYE_POS[0])

            lDir=Vector2(TARGET_POS[1]-EYE_POS[1],TARGET_POS[2]-EYE_POS[2])

            rDir=Vector2(TARGET_POS[0]-EYE_POS[0],TARGET_POS[2]-EYE_POS[2])

            uDir=uDir.rotate(-rSPEED*ey)
            rDir=rDir.rotate(rSPEED*ex)
            lDir=lDir.rotate(rSPEED*ey)
            TARGET_POS[1]=uDir.x+EYE_POS[1]
            TARGET_POS[0]=uDir.y+EYE_POS[0]

            TARGET_POS[1]=uDir.x+EYE_POS[1]
            TARGET_POS[2]=uDir.y+EYE_POS[2]
            

            TARGET_POS[0]=rDir.x+EYE_POS[0]
            TARGET_POS[2]=rDir.y+EYE_POS[2]

            self.move()
            self.lastx, self.lasty = evt.GetPosition()
            self.Refresh(False)
        
        if  evt.LeftIsDown():
            TARGET_POS=[0,0,0]
            #EYE_POS=[5,5,5]
            
            a=Vector2(EYE_POS[0],EYE_POS[2])
            a=a.rotate(SPEED)

            EYE_POS[0]=a.x
            EYE_POS[2]=a.y

            self.move()
            self.Refresh(False)



    def OnKeyDown(self, evt):
        key=chr(evt.GetKeyCode())
        global ANGLE
        global TARGET_POS 
        global EYE_POS
        global SPEED
        global rSPEED
        if key=="A":  
            by=TARGET_POS[2]-EYE_POS[2]
            bx=TARGET_POS[0]-EYE_POS[0]
            
            if bx==0 and by==0:
                bx=0.001

            dirVector=Vector2(bx,by)
            dirVector.normalise()
            dirVector=dirVector.rotate(-90.0)
            dirVector=dirVector.grow((SPEED-1))

            
            EYE_POS=[(EYE_POS[0]+dirVector.x),EYE_POS[1],(EYE_POS[2]+dirVector.y)]
            TARGET_POS=[(TARGET_POS[0]+dirVector.x),EYE_POS[1],(TARGET_POS[2]-dirVector.y)]
         
            self.move()
            #print ("fengxEngine: tartPos: "+str(TARGET_POS)+"eyePos: "+str(EYE_POS) )
        if key=="D":
            by=TARGET_POS[2]-EYE_POS[2]
            bx=TARGET_POS[0]-EYE_POS[0]
            
            if bx==0 and by==0:
                bx=0.001

            dirVector=Vector2(bx,by)
            dirVector.normalise()
            dirVector=dirVector.rotate(90.0)
            dirVector=dirVector.grow((SPEED-1))


            EYE_POS=[(EYE_POS[0]+dirVector.x),EYE_POS[1],(EYE_POS[2]+dirVector.y)]
            TARGET_POS=[(TARGET_POS[0]+dirVector.x),EYE_POS[1],(TARGET_POS[2]-dirVector.y)]

            self.move()
            #print ("fengxEngine: tartPos: "+str(TARGET_POS)+"eyePos: "+str(EYE_POS) )
        if key=="W":
            by=TARGET_POS[2]-EYE_POS[2]
            bx=TARGET_POS[0]-EYE_POS[0]
            if bx==0 and by==0:
                bx=0.001
            dirVector=Vector2(bx,by)
            dirVector.normalise()
            dirVector=dirVector.grow((SPEED-1))
            EYE_POS=[(EYE_POS[0]+dirVector.x),EYE_POS[1],(EYE_POS[2]+dirVector.y)]
            TARGET_POS=[(TARGET_POS[0]+dirVector.x),EYE_POS[1],(TARGET_POS[2]-dirVector.y)]
            self.move()
        if key=="S":
            by=TARGET_POS[2]-EYE_POS[2]
            bx=TARGET_POS[0]-EYE_POS[0]
            if bx==0 and by==0:
                bx=0.001
            dirVector=Vector2(bx,by)
            dirVector.normalise()
            dirVector=dirVector.grow((-SPEED-1))
            EYE_POS=[(EYE_POS[0]+dirVector.x),EYE_POS[1],(EYE_POS[2]+dirVector.y)]
            TARGET_POS=[(TARGET_POS[0]+dirVector.x),EYE_POS[1],(TARGET_POS[2]-dirVector.y)]
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
            EYE_POS=[5,5,5]
            TARGET_POS=[0,0,0]
            self.move()

        if key=="P":
            TARGET_POS=[0,0,0]
            #EYE_POS=[5,5,5]
            
            a=Vector2(EYE_POS[0],EYE_POS[2])
            a=a.rotate(SPEED)

            EYE_POS[0]=a.x
            EYE_POS[2]=a.y

            self.move()

        if key=="-":
            #global SPEED
            SPEED-=0.5
            rSPEED-=0.1
        if key=="=":
            #global SPEED
            SPEED+=0.5
            rSPEED+=0.1


    def OnKeyUp(self, evt):
        key=evt.GetKeyCode()
        #print chr(key)


    def  move(self):
        glLoadIdentity()
        gluLookAt(EYE_POS[0],EYE_POS[1], EYE_POS[2],  TARGET_POS[0],TARGET_POS[1] ,TARGET_POS[2], 0,1,0)
        self.Refresh(False)


class Texture( object ):
	"""Texture either loaded from a file or initialised with random colors."""
	def __init__( self ):
		self.xSize, self.ySize = 0, 0
		self.rawRefence = None

class RandomTexture( Texture ):
	"""Image with random RGB values."""
	def __init__( self, xSizeP, ySizeP ):
		self.xSize, self.ySize = xSizeP, ySizeP
		tmpList = [ random.randint(0, 255) \
			for i in range( 3 * self.xSize * self.ySize ) ]
		self.textureArray = array.array( 'B', tmpList )
		self.rawReference = self.textureArray.tostring( )

class FileTexture( Texture ):
	"""Texture loaded from a file."""
	def __init__( self, fileName ):
		im = Image.open( fileName )
		self.xSize = im.size[0]
		self.ySize = im.size[1]
		self.rawReference = im.tostring("raw", "RGB", 0, -1)

class mainGlCanvas(openGL_BasicCanvas):
    def InitGL(self):
        # set viewing projection
        glMatrixMode(GL_PROJECTION)
        self.size =self.GetClientSize()
        #a=min( size.width, size.height)/max( size.width, size.height)
        b=self.size.width/(self.size.height+0.0)
        glFrustum(-0.1, 0.1, -0.1, 0.1*b, 0.1*b, 1000)

        # position viewer
        glMatrixMode(GL_MODELVIEW)

        a = 0.217
        b = 0.342
        c = 0.537
        d = 0.47
        glClearColor (d,d,d,1)
        #glClearColor(0.5333,0.53333,0,1)
        glEnable(GL_DEPTH_TEST)

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
        glEnable(GL_COLOR_MATERIAL)
        #-----------------------light
        
        #-----------------------texture
        # fileName="jz_jzsj_yw0020_d_wb.png"
        # try:
            # texture = FileTexture( fileName )
        # except:
            # print 'could not open ', fileName, '; using random texture'
            # texture = RandomTexture( 256, 256 )
        # glShadeModel( GL_SMOOTH )
        # glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
        # glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
        # glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
        # glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
        # glTexImage2D( GL_TEXTURE_2D, 0, 3, texture.xSize, texture.ySize, 0,
                     # GL_RGB, GL_UNSIGNED_BYTE, texture.rawReference )
        # glEnable( GL_TEXTURE_2D )
        #-----------------------texture    
    def OnDraw(self):
        # clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glPopMatrix()
        # glEnable(GL_LIGHT1)
        # glEnable(GL_LIGHTING)
   
        if len(Helpers)>0:
            for s in Helpers:
                # glDisable(GL_LIGHT1)
                # glDisable(GL_LIGHTING)
                drawModelObject(s)
                

                
        glEnable(GL_LIGHT1)
        glEnable(GL_LIGHTING)
        if len(ModelObjects)>0:
            for s in ModelObjects:
                drawModelObject(s)
                
            glLineWidth(2)   
            # glDisable(GL_LIGHT1)
            # glDisable(GL_LIGHTING)
            for s in ModelObjects:
                drawMeshLine(s.mesh)
        glLineWidth(1)   
        '''
        if len(BigworldModels)>0:
            i=0
            glEnable(GL_LIGHT1)
            glEnable(GL_LIGHTING)
            for s in BigworldModels:
                i+=3
                #glTranslatef(i,0,0)
                drawObjectFromBigworld(s)
        '''

        
        self.SwapBuffers()

def TexFromPNG(self, filename):
        img = Image.open(filename)
        img_data = numpy.array(list(img.getdata()), numpy.uint8)

        texture = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        return texture

def drawLine(obj):
    if type(obj)==Line:
        #glLineWidth(2)
        i=0
        glBegin(GL_LINES)
        for s in obj.index:
            glColor3f(obj.colors[obj.index[i]][0],obj.colors[obj.index[i]][1],obj.colors[obj.index[i]][2])
            glVertex3f(obj.vertexs[obj.index[i]][0],obj.vertexs[obj.index[i]][1],obj.vertexs[obj.index[i]][2])
            i+=1    
        glEnd()
        glLineWidth(1) 
   
def drawMeshLine(obj):
    if type(obj)==Mesh:
        glBegin(GL_LINES)
        glColor3f(1,0,0)
        for s in obj.egdes:
            glVertex3f(obj.vertexs[(s[0]-1)][0],obj.vertexs[(s[0]-1)][1],obj.vertexs[(s[0]-1)][2])
            glVertex3f(obj.vertexs[(s[1]-1)][0],obj.vertexs[(s[1]-1)][1],obj.vertexs[(s[1]-1)][2])
        glEnd()
        
        
def drawMesh(obj):
    if type(obj)==Mesh:
        glColor3f(0.5,0.5,0.5)
        #i=0
        #---draw the mesh face
        glBegin(GL_QUADS)
        for s in obj.faces:
            if len(s)==4:
                for i in s:
                    v_num=i[0]-1
                    vt_num=i[1]-1
                    n_num=i[2]-1
                    if  i[2]!=0:
                        glNormal3f(obj.normals[n_num][0],obj.normals[n_num][1],obj.normals[n_num][2])
                    if  i[1]!=0:
                        glTexCoord2f(obj.uvs[vt_num][0],obj.uvs[vt_num][1])
                    glVertex3f(obj.vertexs[v_num][0],obj.vertexs[v_num][1],obj.vertexs[v_num][2])
        glEnd()
        glBegin(GL_TRIANGLES)
        
        for s in obj.faces:
            if len(s)==3:
                for i in s:
                    v_num=i[0]-1
                    vt_num=i[1]-1
                    n_num=i[2]-1
                    if  i[2]!=0:
                        glNormal3f(obj.normals[n_num][0],obj.normals[n_num][1],obj.normals[n_num][2])
                    if  i[1]!=0:
                        glTexCoord2f(obj.uvs[vt_num][0],obj.uvs[vt_num][1])
                    glVertex3f(obj.vertexs[v_num][0],obj.vertexs[v_num][1],obj.vertexs[v_num][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for s in obj.faces:
            if len(s)>4:
                #print len(s)
                for i in s:
                    v_num=i[0]-1
                    vt_num=i[1]-1
                    n_num=i[2]-1
                    if  i[2]!=0:
                        glNormal3f(obj.normals[n_num][0],obj.normals[n_num][1],obj.normals[n_num][2])
                    if  i[1]!=0:
                        glTexCoord2f(obj.uvs[vt_num][0],obj.uvs[vt_num][1])
                    glVertex3f(obj.vertexs[v_num][0],obj.vertexs[v_num][1],obj.vertexs[v_num][2])
        glEnd()
        

        
        
        
        #--draw the line
        '''
        glLineWidth(2)
        glBegin(GL_LINE_LOOP)#GL_QUADS)
        glColor3f(0.1,0.5,0.8)
        lon=1
        i=0
        for s in obj.faces:
            glVertex3f(obj.vertexs[i][0],obj.vertexs[i][1],obj.vertexs[i][2])
            #glVertex3f(obj.vertexs[i+lon][0],obj.vertexs[i+lon][1],obj.vertexs[i+lon][2])
            lon=-lon
            i+=1    
        glEnd()
        glLineWidth(1)
        '''       
def drawModelObject(obj):
    if obj.renderEnable==True:
        #glMatrixMode(GL_objVIEW)
        glTranslatef(obj.transform.position.x, obj.transform.position.y, obj.transform.position.z)
        #glRotatef(self.x, 0.0, 1.0, 0.0)
        drawMesh(obj.mesh)
        drawLine(obj.line)         

def importObjFile(filePath):
    obj=ModelObject()
    meshData=objFile.getVals_from_objFile(filePath)
    #vs,vt,vn,fs,objectName,groupName,smoothGroup,materials
    obj.mesh.vertexs=meshData[0]
    obj.mesh.uvs=meshData[1]
    obj.mesh.normals=meshData[2]
    obj.mesh.faces=meshData[3]
    obj.mesh.egdes=getEgdeFromFace(obj.mesh.faces)
    obj.mesh.groupName=meshData[5]
    obj.mesh.smoothGroup=meshData[6]
    obj.mesh.materials=meshData[7]
    #print meshData[4]
    if len(meshData[4])>1 :
        if type(meshData[4][0])==type(" "):
            obj.mesh.name=meshData[4][0]
            obj.name=meshData[4][0]
    #print mesh.normals
    import _data as da
    da.ModelObjects.append(obj)
def importFile():
    file_wildcard = "OBJ files(*.obj)|*.obj|All files(*.*)|*.*"   
    #os.getcwd()
    dlg = wx.FileDialog(self, "Open Wavefront obj file...",  
                        "E:\\Desktop\\",   
                        style = wx.OPEN,  
                        wildcard = file_wildcard)  
    if dlg.ShowModal() == wx.ID_OK:  
        self.filename = dlg.GetPath()  
    dlg.Destroy()  
    importObjFile(self.filename) 



def importBigworldModel(modelInfo):
    obj=ModelObject()
    #vs,vt,vn,fs,objectName,groupName,smoothGroup,materials
    
    for s in modelInfo[2]:
        obj.mesh.vertexs.append(modelInfo[1][s][0])
        obj.mesh.uvs.append(modelInfo[1][s][1])
        obj.mesh.normals.append(modelInfo[1][s][2])
        
    for i in range(0,(len(modelInfo[2])/3)):
        #print "xxxx",i
        f_1=[(i*3+1),(i*3+1),(i*3+1)]#(modelInfo[2][i*3]+1),(modelInfo[2][i*3]+1)]
        f_2=[(i*3+2),(i*3+2),(i*3+2)]#(modelInfo[2][(i*3+1)]+1),(modelInfo[2][(i*3+1)]+1)]
        f_3=[(i*3+3),(i*3+3),(i*3+3)]#(modelInfo[2][(i*3+2)]+1),(modelInfo[2][(i*3+2)]+1)]
        obj.mesh.faces.append([f_1,f_2,f_3])
    obj.mesh.egdes=getEgdeFromFace(obj.mesh.faces)
    #obj.mesh.groupName=meshData[5]
    #obj.mesh.smoothGroup=meshData[6]
    #obj.mesh.materials=meshData[7]
    import _data as da
    da.ModelObjects.append(obj)   
    
    

def createGridModel():
    grid=ModelObject()
    num=21
    j=num*0.1#l/10
    l=j*(num-1)/2
    for i in range(num):
        if i == ((num-1)/2):
            grid.line.colors.append((1.0,0.0,0.0))
            grid.line.vertexs.append((-l, 0, i * j - l))
            grid.line.colors.append((1.0,0.0,0.0))
            grid.line.vertexs.append((l, 0,i * j - l))
            grid.line.colors.append((0.0,0.0,1.0))
            grid.line.vertexs.append((i * j - l, 0,l))
            grid.line.colors.append((0.0,0.0,1.0))
            grid.line.vertexs.append((i * j - l, 0,-l))
        else:
            grid.line.colors.append((0.6,0.6,0.6))
            grid.line.vertexs.append((-l, 0, i * j - l))
            grid.line.colors.append((0.6,0.6,0.6))
            grid.line.vertexs.append((l, 0,i * j - l))
            grid.line.colors.append((0.6,0.6,0.6))
            grid.line.vertexs.append((i * j - l, 0,l))
            grid.line.colors.append((0.6,0.6,0.6))
            grid.line.vertexs.append((i * j - l, 0,-l))
    grid.name="grid"
    grid.line.colors.append((0.0,1.0,0.0))
    grid.line.vertexs.append((0.0, l,0.0))
    grid.line.colors.append((0.0,1.0,0.0))
    grid.line.vertexs.append((0.0, -l,0.0))


    a=Vector2(0.0,21)
    for s in range(1,360):
        b=a.rotate(s)    
        t=3*math.sin(s*10/180.0*math.pi)
        grid.line.colors.append((b.x,1.0,b.y))
        grid.line.vertexs.append((b.x,t,b.y))



    for s in range(0,(len(grid.line.vertexs))):
        grid.line.index.append(s)


    Helpers.append(grid)
createGridModel()


def drawObjectFromBigworld(modelInfo):
    #a=po.getModelInfo(filePath,"H:\\testPrimitives\\bghm_jztj_yw0040_2545")
    vertexs=modelInfo[1]
    indexs=modelInfo[2]
    #glPointSize(5)
    #glLineWidth(2)
    glColor3f(0.5,0.5,0.5)    
    glBegin(GL_TRIANGLES)#_STRIP)
    for i in range(0,(len(indexs)-1)):
        #print vertexs[indexs[i]]
        glNormal3f(vertexs[indexs[i]][2][0],vertexs[indexs[i]][2][1],vertexs[indexs[i]][2][2])
        glVertex3f(vertexs[indexs[i]][0][0],vertexs[indexs[i]][0][1],vertexs[indexs[i]][0][2])
    glEnd()
    #print modelInfo