#coding:utf-8 
import wx
#import sys
import  wx.lib.mvctree  as  tree
import os
import images
import  string

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



class openGL_BasicCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)
        
        # initial mouse position
        self.lastx = self.x = 30
        self.lasty = self.y = 30
        self.size = None
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)


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
        #self.SetCurrent(self.context)
        #print self.context
        #print size 
        a=min( size.width, size.height)
  
        b=size.width/(size.height+0.0)
        #glFrustum(-1, 1, -1, 1, 1.0, 150)
        #gluPerspective(0,b,1,100)
    
        #glFrustum(-b, b, -1, 1, 1.0, 150)
        #gluPerspective(0,b,1,100)
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
        self.CaptureMouse()
        self.x, self.y = self.lastx, self.lasty = evt.GetPosition()


    def OnMouseUp(self, evt):
        self.ReleaseMouse()


    def OnMouseMotion(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            self.lastx, self.lasty = self.x, self.y
            self.x, self.y = evt.GetPosition()
            self.Refresh(False)



class mainGlCanvas(openGL_BasicCanvas):
    def InitGL(self):
        # set viewing projection
        glMatrixMode(GL_PROJECTION)
        size = self.size =self.GetClientSize()
        #a=min( size.width, size.height)/max( size.width, size.height)
        glFrustum(-1, 1, -1, 1, 1.0, 150)
        # position viewer
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -2.0)

        # position object
        glRotatef(self.y, 1.0, 0.0, 0.0)
        glRotatef(self.x, 0.0, 1.0, 0.0)


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
       
        glBegin(GL_QUADS)
        glColor3f(0.78,0.78,0.78)
        glNormal3f( 0.0, 0.0, 1.0)
        glVertex3f( 0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5,-0.5, 0.5)
        glVertex3f( 0.5,-0.5, 0.5)
        glColor3f(0,0.6,0)
        glNormal3f( 0.0, 0.0,-1.0)
        glVertex3f(-0.5,-0.5,-0.5)
        glVertex3f(-0.5, 0.5,-0.5)
        glVertex3f( 0.5, 0.5,-0.5)
        glVertex3f( 0.5,-0.5,-0.5)
        glColor3f(0.4,0,0)
        glNormal3f( 0.0, 1.0, 0.0)
        glVertex3f( 0.5, 0.5, 0.5)
        glVertex3f( 0.5, 0.5,-0.5)
        glVertex3f(-0.5, 0.5,-0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glColor3f(0,0.5,0.5)
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
        glColor3f(0.5,0.5,0.5)
        
        glNormal3f(-1.0, 0.0, 0.0)
        glVertex3f(-0.5,-0.5,-0.5)
        glVertex3f(-0.5,-0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5,-0.5)
        glEnd()

        #glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        #glLoadIdentity()
        glScale(0.9,0.9,0.2)
        glPopMatrix()
        if self.size is None:
            self.size = self.GetClientSize()
 
        w, h = self.size
        w = max(w, 1.0)
        h = max(h, 1.0)
        xScale = 180.0 / w
        yScale = 180.0 / h
        glRotatef((self.y - self.lasty) * yScale, 1.0, 0.0, 0.0);
        glRotatef((self.x - self.lastx) * xScale, 0.0, 1.0, 0.0);
        glBegin(GL_LINES)
        self.xyz()
        self.grid()
        glEnd()

        self.SwapBuffers()


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
        num=41
        j=0.08#l/10
        l=j*(num-1)/2
        for i in range(num):
            if i == ((num-1)/2):
                glColor3f(0.1,0.1,0.1)
            else:
                glColor3f(0.6,0.6,0.6)
                glVertex3d(-l, i * j - l, 0)
                glVertex3d(l, i * j - l, 0)
                glVertex3d(i * j - l, l, 0)
                glVertex3d(i * j - l, -l, 0)


class MyTreeCtrl(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
        #self.log = log
        print self.SetWindowStyleFlag
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

        self.tree = MyTreeCtrl(self, tID, (400,0) , wx.DefaultSize,
                               wx.TR_HAS_BUTTONS
                                |wx.TR_TWIST_BUTTONS
                                | wx.TR_SINGLE
                                | wx.TR_MULTIPLE
                                |wx.TR_NO_LINES
                                |wx.TR_FULL_ROW_HIGHLIGHT
                                |wx.TR_EDIT_LABELS
                                |wx.TR_EXTENDED
                               #|wx.TR_NO_BUTTONS
                               #|wx.TR_HAS_VARIABLE_ROW_HEIGHT
                               )

        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        icon=wx.Icon("App.ico", wx.BITMAP_TYPE_ICO)
        smileidx    = il.Add(wx.BitmapFromIcon(icon))

        self.tree.SetImageList(il)
        self.il = il

        # NOTE:  For some reason tree items have to have a data object in
        #        order to be sorted.  Since our compare just uses the labels
        #        we don't need any real data, so we'll just use None below for
        #        the item data.

        self.root = self.tree.AddRoot("The Root Item")
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
        #--------------main Part of window------->>>>
        #self.P_main=wx.Panel(self,-1)
        #self.P_tooBar=wx.Panel(self)
        #self.P_mainWindow=wx.Panel(self)
        self.P_main=wx.Panel(self,  id=-1, pos=(0,0), size=(500,500), style=wx.TAB_TRAVERSAL|wx.NO_BORDER, name="zzz") 

        '''
        '''
        self.P_sceneWindow=wx.Panel(self)
        self.P_fileManager=wx.Panel(self)
        self.P_sceneManager=wx.Panel(self)

        '''
        '''
        #---scene window
        self.sceneWindow=mainGlCanvas(self)
        #---resource manager
        self.resManager=TestTreeCtrlPanel(self)
        #---scene manager
        self.sceneManager=TestTreeCtrlPanel(self)
        self.log="sss"
        self.b2=wx.Button(self,label="xxxaaxxxxxxx")
        

        #self.log = log
        tID = wx.NewId()
        self.tr = MyTreeCtrl(self,tID, (400,0) , wx.DefaultSize,
                               wx.TR_HAS_BUTTONS
                                |wx.TR_TWIST_BUTTONS
                                | wx.TR_SINGLE
                                | wx.TR_MULTIPLE
                                |wx.TR_NO_LINES
                                |wx.TR_FULL_ROW_HIGHLIGHT
                                |wx.TR_EDIT_LABELS
                                |wx.TR_EXTENDED
                               #|wx.TR_NO_BUTTONS
                               #|wx.TR_HAS_VARIABLE_ROW_HEIGHT
                               )

        
        #---layout
        #---BoxSizer
        self.mainBox=wx.BoxSizer(wx.HORIZONTAL)

        self.mainBox.Add(self.b2,1, wx.EXPAND)

        self.mainBox.Add(self.sceneWindow )#,1, wx.EXPAND
        self.mainBox.Add(self.tr)
        #self.mainBox.Add(self.sceneManager )
 
  


        self.P_main.SetSizer(self.mainBox)
        #self.tbox=wx.BoxSizer(wx.VERTICAL)
        #self.tbox.add()
        #self.
        #P_tooBar.add()

        
    '''



        #---file project
        #self.tre = TestTreeCtrlPanel(self)
        #---openGl 3D window
        self.gl=mainGlCanvas(self)
        self.gl.Bind(wx.EVT_MIDDLE_UP,  self.close)

        
        #---ect
        #self.b = wx.Button(self, -1, "test", (50,50))
        #self.b.Bind(wx.EVT_BUTTON, self.OnButton, self.b)


        '''
        self.SetAutoLayout(True)

        lgl = wx.LayoutConstraints()


        lgl.top.PercentOf(self, wx.Top,1) 
        lgl.left.PercentOf(self, wx.Left, 1) 
        lgl.right.PercentOf(self,wx.Right,60) 
        lgl.bottom.PercentOf(self,wx.Bottom,100)

        lc = wx.LayoutConstraints()
        lc.top.PercentOf(self, wx.Top, 90)
        lc.left.PercentOf(self, wx.Left, 50)
        lc.bottom.PercentOf(self,wx.Bottom,50)
        #lc.bottom.SameAs(self, wx.Bottom, 100)
        lc.right.PercentOf(self, wx.Right, 50)
       
        '''

        
        #self.tre.SetConstraints(lc)             
        #self.gl.SetConstraints(lgl )

        
    def makeSimpleBox3(win):
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(SampleWindow(win, "one"), 0, wx.EXPAND)
        box.Add(SampleWindow(win, "two"), 0, wx.EXPAND)
        box.Add(SampleWindow(win, "three"), 0, wx.EXPAND)
        box.Add(SampleWindow(win, "four"), 0, wx.EXPAND)
        box.Add(SampleWindow(win, "five"), 1, wx.EXPAND)
        return box

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

