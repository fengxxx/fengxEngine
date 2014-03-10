#coding:utf-8 
import wx
#import sys
import  wx.lib.mvctree  as  tree
import os

import math

#from key import  *
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

    
import  wx.lib.customtreectrl, wx.gizmos
try:
    import treemixin 
except ImportError:
    from wx.lib.mixins import treemixin

overview = treemixin.__doc__




ROOT_DIR=os.getcwd()
MAIN_WINDOW_SIZE=(600,600)
ICON_PATH=ROOT_DIR+"\\App.ico"

MAIN_BG_COLOR=(37,37,37)

EYE_POS=[1,1,1]
TARGET_POS=[0,0,0]
ANGLE = -90
ANGLE_UP=-90
PI=3.14159
SPEED=0.5
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


class MyTreeCtrl(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
        #self.log = log
        #print self.SetWindowStyleFlag
        self.SetForegroundColour((168,168,168))
        #self.SetItemBackgroundColour(MAIN_BG_COLOR)
        self.SetBackgroundColour(MAIN_BG_COLOR)
    def OnCompareItems(self, item1, item2):
        t1 = self.GetItemText(item1)
        t2 = self.GetItemText(item2)
        print ('compare: ' + t1 + ' <> ' + t2 + '\n')
        
        if t1 < t2: return -1
        if t1 == t2: return 0
        return 1


'''
(TR_EXTENDED 'TR_DEFAULT_STYLE', 'TR_EDIT_LABELS', 'TR_EXTENDED', 'TR_FULL_ROW_HIGHLIGHT',
'TR_HAS_BUTTONS', 'TR_HAS_VARIABLE_ROW_HEIGHT', 'TR_HIDE_ROOT', 'TR_LINES_AT_ROOT', 'TR_MAC_BUTTONS',
'TR_MULTIPLE', 'TR_NO_BUTTONS', 'TR_NO_LINES', 'TR_ROW_LINES', 'TR_SINGLE', 'TR_TWIST_BUTTONS')



'''                           

class TestTreeCtrlPanel(wx.Panel):
    def __init__(self, parent):
        # Use the WANTS_CHARS style so the panel doesn't eat the Return key.
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        #self.log = log
        tID = wx.NewId()

        self.tree = MyTreeCtrl(self, tID, (0,0) , (100,100),
                               wx.TR_HAS_BUTTONS
                                |wx.TR_TWIST_BUTTONS
                                #| wx.TR_SINGLE
                                | wx.TR_MULTIPLE
                                |wx.TR_NO_LINES
                                |wx.TR_FULL_ROW_HIGHLIGHT
                                |wx.TR_EDIT_LABELS
                                #|wx.TR_EXTENDED
                               #|wx.TR_NO_BUTTONS
                               #|wx.TR_HAS_VARIABLE_ROW_HEIGHT
                               )

        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])

        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NEW_DIR,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        icon=wx.Icon("App.ico", wx.BITMAP_TYPE_ICO)
        
        smileidx    = il.Add(wx.ArtProvider_GetBitmap(wx.ART_TICK_MARK, wx.ART_OTHER, isz))#il.Add(wx.BitmapFromIcon(icon))

        self.tree.SetImageList(il)
        self.il = il

        # NOTE:  For some reason tree items have to have a data object in
        #        order to be sorted.  Since our compare just uses the labels
        #        we don't need any real data, so we'll just use None below for
        #        the item data.

        self.root = self.tree.AddRoot("project")
        self.tree.SetPyData(self.root, None)
        self.tree.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)


        for x in range(2):
            child = self.tree.AppendItem(self.root, "Item %d" % x)
            self.tree.SetPyData(child, None)
            self.tree.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
            self.tree.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)

            for y in range(2):
                last = self.tree.AppendItem(child, "item %d-%s" % (x, chr(ord("a")+y)))
                self.tree.SetPyData(last, None)
                self.tree.SetItemImage(last, fldridx, wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(last, fldropenidx, wx.TreeItemIcon_Expanded)

                for z in range(2):
                    item = self.tree.AppendItem(last,  "item %d-%s-%d" % (x, chr(ord("a")+y), z))
                    self.tree.SetPyData(item, None)
                    self.tree.SetItemImage(item, fileidx, wx.TreeItemIcon_Normal)
                    self.tree.SetItemImage(item, smileidx, wx.TreeItemIcon_Selected)

        self.tree.Expand(self.root)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self.tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginEdit, self.tree)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.OnEndEdit, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivate, self.tree)

        self.tree.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDClick)
        self.tree.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.tree.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)


    def OnRightDown(self, event):
        pt = event.GetPosition();
        item, flags = self.tree.HitTest(pt)
        if item:
            print ("OnRightClick: %s, %s, %s\n" %
                               (self.tree.GetItemText(item), type(item), item.__class__))
            self.tree.SelectItem(item)


    def OnRightUp(self, event):
        pt = event.GetPosition();
        item, flags = self.tree.HitTest(pt)
        if item:        
            print ("OnRightUp: %s (manually starting label edit)\n"
                               % self.tree.GetItemText(item))
            self.tree.EditLabel(item)



    def OnBeginEdit(self, event):
        print ("OnBeginEdit\n")
        # show how to prevent edit...
        item = event.GetItem()
        if item and self.tree.GetItemText(item) == "The Root Item":
            wx.Bell()
            print ("You can't edit this one...\n")

            # Lets just see what's visible of its children
            cookie = 0
            root = event.GetItem()
            (child, cookie) = self.tree.GetFirstChild(root)

            while child.IsOk():
                print ("Child [%s] visible = %d" %
                                   (self.tree.GetItemText(child),
                                    self.tree.IsVisible(child)))
                (child, cookie) = self.tree.GetNextChild(root, cookie)

            event.Veto()


    def OnEndEdit(self, event):
        print ("OnEndEdit: %s %s\n" %
                           (event.IsEditCancelled(), event.GetLabel()) )
        # show how to reject edit, we'll not allow any digits
        for x in event.GetLabel():
            if x in string.digits:
                print ("You can't enter digits...\n")
                event.Veto()
                return


    def OnLeftDClick(self, event):
        pt = event.GetPosition();
        item, flags = self.tree.HitTest(pt)
        if item:
            print ("OnLeftDClick: %s\n" % self.tree.GetItemText(item))
            parent = self.tree.GetItemParent(item)
            if parent.IsOk():
                self.tree.SortChildren(parent)
        event.Skip()


    def OnSize(self, event):
        w,h = self.GetClientSizeTuple()
        self.tree.SetDimensions(0, 0, w, h)


    def OnItemExpanded(self, event):
        item = event.GetItem()
        if item:
            print ("OnItemExpanded: %s\n" % self.tree.GetItemText(item))

    def OnItemCollapsed(self, event):
        item = event.GetItem()
        if item:
            print ("OnItemCollapsed: %s\n" % self.tree.GetItemText(item))

    def OnSelChanged(self, event):
        self.item = event.GetItem()
        if self.item:
            print ("OnSelChanged: %s\n" % self.tree.GetItemText(self.item))
            if wx.Platform == '__WXMSW__':
                print ("BoundingRect: %s\n" %
                                   self.tree.GetBoundingRect(self.item, True))
            #items = self.tree.GetSelections()
            #print map(self.tree.GetItemText, items)
        event.Skip()


    def OnActivate(self, event):
        if self.item:
            print ("OnActivate: %s\n" % self.tree.GetItemText(self.item))


#---------------------------------------------------------------------------


class mainFrame(wx.Frame):
    global MAIN_WINDOW_SIZE
    global ICON_PATH
    global MAIN_BG_COLOR

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'fengx', size=MAIN_WINDOW_SIZE,style=wx.DEFAULT_FRAME_STYLE)
        
        #---------------main Window settings----->>>>
        self.SetBackgroundColour(MAIN_BG_COLOR)
        self.icon = wx.Icon(ICON_PATH, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        

        #--------------main MenuBar--------------->>>>
        self.menuBar = wx.MenuBar()
        self.SetMenuBar(self.CreateMenuBar())
        #--------------main MenuBar--------------<<<<<
        self.CreateStatusBar()
        self.SetStatusText("fengxEngine")
        '''
        self._leftWindow1 = wx.SashLayoutWindow(self, 101, wx.DefaultPosition,
                                                wx.Size(200, 1000), wx.NO_BORDER |
                                                wx.SW_3D | wx.CLIP_CHILDREN)
        
        self.ID_WINDOW_TOP = 100
        self.ID_WINDOW_LEFT1 = 101
        self.ID_WINDOW_RIGHT1 = 102
        self.ID_WINDOW_BOTTOM = 103

        self._leftWindow1.Bind(wx.EVT_SASH_DRAGGED_RANGE, self.OnFoldPanelBarDrag,
                               id=100, id2=103)
        self._leftWindow1.SetOrientation(wx.LAYOUT_VERTICAL)
        self._leftWindow1.SetAlignment(wx.LAYOUT_LEFT)
        self._leftWindow1.SetSashVisible(wx.SASH_RIGHT, True)
        self._leftWindow1.SetExtraBorderSize(3)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        '''
        #--------------main Part of window------->>>>
        self.P_main=wx.Panel(self)
 
        #---scene window
        self.sceneWindow=mainGlCanvas(self.P_main)
        #---resource manager
        self.resManager=TestTreeCtrlPanel(self.P_main)
        #---scene manager
        #self.sceneManager=TestTreeCtrlPanel(self.P_main)
        #---inspect panel
        #self.inspectorPnale=TestTreeCtrlPanel(self.P_main)
        #---toolBar
        #self.mainToolBar=wx.Panel(self)

        self.dir3 = wx.GenericDirCtrl(self.P_main, -1, size=(200,225), style=wx.DIRCTRL_SHOW_FILTERS,
                                filter="All files (*.*)|*.*|Python files (*.py)|*.py")

        #self.dir3.SetPath(ROOT_DIR)
        #self.dir3.SetDefaultPath(ROOT_DIR)
        self.box = wx.BoxSizer(wx.HORIZONTAL)
        self.box.Add(self.sceneWindow, 3, wx.EXPAND|wx.ALL ,border=2)
        self.box.Add(self.resManager, 1, wx.EXPAND|wx.ALL ,border=1)
        self.box.Add(self.dir3, 1, wx.EXPAND|wx.ALL ,border=1)

        self.b = wx.Button(self.P_main, -1, label=u'打开')  
        self.mainBox=wx.BoxSizer(wx.VERTICAL)
        self.mainBox.Add(self.b, 0, border=1)
        self.mainBox.Add(self.box,1,wx.EXPAND|wx.ALL ,border=1)
        


        self.P_main.SetSizer(self.mainBox)
        self.mainBox.Fit(self.P_main)
        self.Fit()


    def OnSize(self, event):

        wx.LayoutAlgorithm().LayoutWindow(self, self.remainingSpace)
        event.Skip()
    def OnFoldPanelBarDrag(self, event):

        if event.GetDragStatus() == wx.SASH_STATUS_OUT_OF_RANGE:
            return

        if event.GetId() == self.ID_WINDOW_LEFT1:
            self._leftWindow1.SetDefaultSize(wx.Size(event.GetDragRect().width, 1000))


        # Leaves bits of itself behind sometimes
        wx.LayoutAlgorithm().LayoutWindow(self, self.remainingSpace)
        self.remainingSpace.Refresh()

        event.Skip()
        
    def CreateMenuBar(self):

        # Make a menubar
        file_menu = wx.Menu()
        help_menu = wx.Menu()
        t1_menu = wx.Menu()
        t2_menu = wx.Menu()


        TEST_QUIT = wx.NewId()
        TEST_ABOUT = wx.NewId()
        TEST_JIKANG = wx.NewId()
        TEST_RUANJI = wx.NewId()
        TEST_LIULING = wx.NewId()


        file_menu.Append(TEST_QUIT, "&Exit")
        help_menu.Append(TEST_ABOUT, "&About")
        #file_menu.Append(TEST_RUANJI,"&阮籍", "时无英雄，使竖子成名")
        
        menu_bar = wx.MenuBar()

        menu_bar.Append(file_menu, "&ThreeKindom")
        menu_bar.Append(help_menu, "&Help")
        '''
        menu_bar.Append(t2_menu,)
        menu_bar.Append(t1_menu, "&魏晋")
        t1_menu.Append(TEST_JIKANG, "&嵇康", "广陵散")
        t1_menu.Append(TEST_RUANJI, "&阮籍", "时无英雄，使竖子成名")
        t1_menu.Append(TEST_LIULING, "&刘伶", "常乘鹿车，携一壶酒，使人荷锸而随之，谓曰：“死便埋我。")
        self.m_2= wx.Menu()
        self.m_2.Append(m_2_1, "&楚南宫", "This the text in the Statusbar")
        self.m_2.Append(m_2_2, "&重耳", "")
        self.m_2.Append(m_2_3, "&商臣", "You may select Earth too")
        #self.menuBar.Append(self.m_2, "&战国")
        self.menuBar.Append(self.menu1, "&魏晋")
        '''


        #self.Bind(wx.EVT_MENU, self.OnAbout, id=TEST_ABOUT)
        self.Bind(wx.EVT_MENU, self.close, id=TEST_QUIT)
        #self.Bind(wx.EVT_CLOSE, self.OnQuit)

        return menu_bar
    def close(self,event):
        self.Close()


    def OnButton(self, evt):
        dlg = wx.ColourDialog(self)

        # Ensure the full colour dialog is displayed, 
        # not the abbreviated version.
        dlg.GetColourData().SetChooseFull(True)

        if dlg.ShowModal() == wx.ID_OK:

            # If the user selected OK, then the dialog's wx.ColourData will
            # contain valid information. Fetch the data ...
            data = dlg.GetColourData()

            # ... then do something with it. The actual colour data will be
            # returned as a three-tuple (r, g, b) in this particular case.
            print ('You selected: %s\n' % str(data.GetColour().Get()))

        # Once the dialog is destroyed, Mr. wx.ColourData is no longer your
        # friend. Don't use it again!
        dlg.Destroy()
mainApp = wx.PySimpleApp()
newFrame = mainFrame(parent=None, id=-1)
newFrame.Show()
newFrame.SetBackgroundColour(MAIN_BG_COLOR)
#print dir(newFrame)
mainApp.MainLoop()


class Vector3():

class gameObject():


    class transform():
        position=(0,0,0)
        rotation=(0,0,0)
        scale=(0,0,0)


        
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




