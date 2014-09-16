#coding:utf-8 
import wx
import math
import sys

#from customTree import CustomTreeCtrl
import wx.lib.agw.customtreectrl as CT
from _hierarchy import *
from _globalData import *
from _scene import *
from _data import *
from PyConsole import PyConsoleFrame,PyConsolePanel


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window, log):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.log = log

    def OnDropFiles(self, x, y, filenames):
        for f in filenames:
            fileE=os.path.splitext(f)[1]
            if fileE==".obj" or  fileE==".OBJ":
                print "import obj file:" ,f
                importObjFile(f) 
            elif  fileE==".primitives":   
                importBigworldModel(po.getModelInfo(f,"temp\\"))  
                print "import Primitives file:" ,f
            else:
                print "can't import file :",f
class mainFrame(wx.Frame):
    global MAIN_WINDOW_SIZE
    global ICON_PATH
    global MAIN_BG_COLOR
    log=""
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'fengxEngine', size=MAIN_WINDOW_SIZE,style=wx.DEFAULT_FRAME_STYLE)
        #---------------main Window settings----->>>>
        self.SetBackgroundColour((225,225,225))#MAIN_BG_COLOR)
        self.icon = wx.Icon(ICON_PATH, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        #self.CreateStatusBar()
        #self.SetStatusText("fengxEngine: tartPos: "+str(TARGET_POS)+"eyePos: "+str(EYE_POS) )

        #--------------main Part of window------->>>>
        self.P_main=wx.Panel(self)
        
        #---scene window 
        self.sceneWindow=mainGlCanvas(self.P_main)
        self.sceneWindow2=mainGlCanvas(self.P_main)
        #---resource manager 
              #self.log = log
 
        self.resManager=sceneTreePanel(self.P_main, wx.NewId(), (0,0) , (100,100),
                               wx.TR_HAS_BUTTONS
                                |wx.TR_TWIST_BUTTONS
                                |wx.TR_SINGLE
                                |wx.TR_MULTIPLE
                                |wx.TR_NO_LINES
                                |wx.TR_FULL_ROW_HIGHLIGHT
                                |wx.TR_EDIT_LABELS
                                #|wx.TR_HIDE_ROOT
                                |wx.TR_EXTENDED
                               #|wx.TR_NO_BUTTONS
                               #|wx.TR_HAS_VARIABLE_ROW_HEIGHT
                               )
        
        self.resManager.SetBackgroundColour((120,120,120))
        

        dt = MyFileDropTarget(self.P_main, log)
        self.SetDropTarget( dt ) 
        
        #---scene manager
        #self.sceneManager=TestTreeCtrlPanel(self.P_main)
        #---inspect panel
        #self.inspectorPnale=TestTreeCtrlPanel(self.P_main)
        #---toolBar
    
        #--------------main MenuBar--------------->>>>
        #self.menuBar = wx.MenuBar()
        #self.SetMenuBar(self.CreateMenuBar())
        #--------------main MenuBar--------------<<<<<


    
        #self.dir3 = wx.GenericDirCtrl(self.P_main, -1, size=(200,225), style=wx.DIRCTRL_SHOW_FILTERS,
        #                        filter="All files (*.*)|*.*|Python files (*.py)|*.py")

        #self.dir3.SetPath(ROOT_DIR)
        #self.dir3.SetDefaultPath(ROOT_DIR)
        
        '''
        self.tc = wx.TextCtrl(self.P_main, -1, "self.t()", size=(25, 20), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        #self.Bind(wx.EVT_TEXT, self.EvtText, t2)
        self.tc.SetBackgroundColour((100,100,100))#(48.825,48.825,48.825))
        #self.tc.SetOwnBackgroundColour(MAIN_BG_COLOR)
        self.tc.SetForegroundColour(MAIN_BG_COLOR)#(120,120,120))
        self.tc.SetTransparent(2)
        self.bce=wx.Button(self.P_main, -1, label=u'Enter') 
        self.bce.SetBackgroundColour((100,100,100))
        #self.bce.SetForegroundColour(MAIN_BG_COLOR)
        
        self.Bind(wx.EVT_BUTTON, self.execComd, self.bce)
        #self.tc.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        '''
        self.box = wx.BoxSizer(wx.HORIZONTAL)
        self.box.Add(self.sceneWindow, 3, wx.EXPAND|wx.ALL ,border=0)
        self.box.Add(self.sceneWindow2, 3, wx.EXPAND|wx.ALL ,border=0)
        
        self.box.Add(self.resManager, 1, wx.EXPAND|wx.ALL ,border=0)
        #self.box.Add(self.dir3, 1, wx.EXPAND|wx.ALL ,border=1)


        #----------------------main toolbar 
        self.main_toolbar = wx.ToolBar(self.P_main, -1, wx.DefaultPosition, wx.DefaultSize,wx.TB_FLAT | wx.TB_NODIVIDER| wx.TB_TEXT)
        #self.main_toolbar.SetToolBitmapSize(wx.Size(10,10))
        iconSize=25
        
        self.Icon_fileOpen = wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, wx.Size(iconSize, iconSize))
        self.Icon_fileNew = wx.ArtProvider_GetBitmap(wx.ART_NEW, wx.ART_OTHER, wx.Size(iconSize, iconSize))
        self.Icon_close = wx.ArtProvider_GetBitmap(wx.ART_CLOSE, wx.ART_OTHER, wx.Size(iconSize, iconSize))
        #self.Icon_play = wx.ArtProvider_GetBitmap(wx.ART_TOOLBAR, wx.ART_OTHER, wx.Size(iconSize, iconSize))
        self.main_toolbar.AddLabelTool(10, "new file", self.Icon_fileNew)
        self.main_toolbar.AddLabelTool(11, "open file", self.Icon_fileOpen)
        
        self.main_toolbar.AddStretchableSpace()
        self.main_toolbar.AddLabelTool(13, "pyconsole", self.Icon_fileOpen)
        #self.main_toolbar.AddLabelTool(14, "open file", self.Icon_fileOpen)
        
        #self.main_toolbar.AddSeparator()
        #self.main_toolbar.AddStretchableSpace()
        #----------------------------------------------------------------------
        '''
        intro = 'Welcome To PyCrust %s - The Flakiest Python Shell' % py.version.VERSION
        self.win = py.shell.Shell(self.P_main, -1, introText="fengxEngine")
        '''           
           
        #self.cbID = wx.NewId()
        #self.main_toolbar.AddControl(wx.ComboBox(self.main_toolbar, self.cbID, "", choices=["54", "1", "2", "fengx"],size=(150,-1), style=wx.CB_DROPDOWN))
        self.main_toolbar.AddStretchableSpace()
        self.main_toolbar.AddLabelTool(12, "close", self.Icon_close)
        
        self.main_toolbar.Realize()
        self.main_toolbar.SetBackgroundColour((120,120,120))

        #self.Bind(wx.EVT_COMBOBOX, self.OnCombo, id=self.cbID)
        self.Bind(wx.EVT_TOOL, self.importFile, id=11)
        self.Bind(wx.EVT_TOOL, self.restAll, id=10)
        #self.Bind(wx.EVT_TOOL_RCLICKED, self.importFile, id=11)
        self.Bind(wx.EVT_TOOL, self.close, id=12)
        self.Bind(wx.EVT_TOOL,self.createPyConsole,id=13)
        #self.Bind(wx.EVT_TOOL_RCLICKED, self.close, id=12)
        #----------------------main toolbar 
        
        
        #---------------------layout-------
        #self.conmmadBox=wx.BoxSizer(wx.HORIZONTAL)
        #self.conmmadBox.Add(self.tc, 9, wx.EXPAND|wx.ALL,border=0)
        #self.conmmadBox.Add(self.bce, 1, wx.EXPAND|wx.ALL,border=0)
        self.mainBox=wx.BoxSizer(wx.VERTICAL)
        self.mainBox.Add(self.main_toolbar,1,wx.EXPAND|wx.ALL ,border=0)
        self.mainBox.Add(self.box,20,wx.EXPAND|wx.ALL ,border=0)
 
        self.P_main.SetSizer(self.mainBox)
        self.mainBox.Fit(self.P_main)
        #self.Fit()
    def createPyConsole(self,event):
        #mainApp = wx.PySimpleApp()
        pyFrame = PyConsoleFrame(parent=None, id=-1)
        pyFrame.Show()
        pyFrame.SetBackgroundColour((120,120,120))
        #mainApp.MainLoop()
    def OnCombo(self, event):
        print ("combobox item selected: %s\n" % event.GetString())

 
    def OnKeyDown(self,event):
        #print "test"
        #print event.GetKeyCode()

        if event.GetKeyCode()==370 :
            print self.tc.getvalue()
            #sc=self.tc.GetValue()
            #if sc!="":

            print "xxxx"
            #exec(sc)
            #print "out:  ",sys.stdout.getvalue()
            #self.tc.Clear()
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
        RestAll=wx.NewId()
        TEST_IMPORT = wx.NewId()
        file_menu.Append(TEST_QUIT, "&Exit")
        file_menu.Append(TEST_IMPORT,"&Import")
        file_menu.Append(RestAll,"&RestAll")
        help_menu.Append(TEST_ABOUT, "&About")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")

        #self.Bind(wx.EVT_MENU, self.resManager.updateTree, id=TEST_ABOUT)
        self.Bind(wx.EVT_MENU, self.importFile, id=TEST_IMPORT)
        self.Bind(wx.EVT_MENU, self.restAll, id=RestAll)
        self.Bind(wx.EVT_MENU, self.close, id=TEST_QUIT)
        #self.Bind(wx.EVT_CLOSE, self.OnQuit)
        #menu_bar.SetBackgroundColour(MAIN_BG_COLOR)
        return menu_bar
    def restAll(self,event):
        print "wip"
        self.resManager.updateTree()
        for s in ModelObjects:
            ModelObjects.remove(s)

    def close(self,event):
        self.Close()

    def importFile(self,event):
        file_wildcard = "OBJ files(*.obj)|*.obj|BigWorld model files(*.primitives)|*.primitives|All files(*.*)|*.*"   
        dlg = wx.FileDialog(self, "Open paint file...",  
                            "E:\\Desktop\\",   
                            style = wx.OPEN,  
                            wildcard = file_wildcard)  
        if dlg.ShowModal() == wx.ID_OK:  
            self.filename = dlg.GetPath()  
        dlg.Destroy()  
        fileE=os.path.splitext(self.filename)[1]
        if fileE==".obj" or  fileE==".OBJ":
            importObjFile(self.filename) 
        elif  fileE==".primitives":   
            importBigworldModel(po.getModelInfo(self.filename,"H:\\testPrimitives\\temp\\"))   

    def OnButton(self, evt):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            print ('You selected: %s\n' % str(data.GetColour().Get()))
        dlg.Destroy()

mainApp = wx.PySimpleApp()
newFrame = mainFrame(parent=None, id=-1)
newFrame.Show()
newFrame.SetBackgroundColour((120,120,120))
mainApp.MainLoop()
