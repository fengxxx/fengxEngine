# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc



###########################################################################
## Class mainFrame
###########################################################################
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
class mainFrame ( wx.Frame ):
    lastPos=[0,0]
    canMove=False
    canSize=False
    mousePos=[0,0]
    pos=[400,300]
    size=[0,0]
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FengxEngine 1.0", pos = wx.DefaultPosition, size = wx.Size( 876,685 ), style = wx.NO_BORDER|wx.TAB_TRAVERSAL ) #wx.RESIZE_BORDER|
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( UI_COLOR_MAIN_FG )
        self.SetBackgroundColour( UI_COLOR_MAIN_BG )
        # self.statusBar_main = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        # self.statusBar_main.SetBackgroundColour((66,66,66))# wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
        
        
        #--------------Menu
        # ID_NEW_SCENE = 1000
        # ID_IMPORT_FILE = 1001
        # ID_EXIT = 1002
        # self.m_menubar1 = wx.MenuBar( 0 )
        # self.m_menubar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        # self.m_menubar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        # self.file = wx.Menu()
        # self.newScene = wx.MenuItem( self.file, ID_NEW_SCENE, u"New Scene", wx.EmptyString, wx.ITEM_NORMAL )
        # self.file.AppendItem( self.newScene )
        
        # self.importFile = wx.MenuItem( self.file, ID_IMPORT_FILE, u"Import File", wx.EmptyString, wx.ITEM_NORMAL )
        # self.file.AppendItem( self.importFile )
        
        # self.exit = wx.MenuItem( self.file, ID_EXIT, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        # self.file.AppendItem( self.exit )
        
        # self.m_menubar1.Append( self.file, u"File" ) 
        
        #self.SetMenuBar( self.m_menubar1 )
        #--------------Menu
        
        Sizer_main_V = wx.BoxSizer( wx.VERTICAL )
        
        bSizer_mainScene = wx.BoxSizer( wx.HORIZONTAL )
        
        #self.p_scenes = wx.Panel( self)#, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        #self.p_scenes.SetMinSize( wx.Size( 100,100 ) )
        
        self.sceneWindow=mainGlCanvas(self)
        self.sceneWindow.SetMinSize( wx.Size( 300,100 ) )
        
        bSizer_mainScene.Add( self.sceneWindow, 4, wx.ALL|wx.EXPAND, 0 )
        
        self.tree_project=sceneTreePanel(self, wx.NewId(), (0,0) , (100,100),
                                wx.TR_HAS_BUTTONS
                                |wx.TR_HAS_VARIABLE_ROW_HEIGHT
                                |wx.TR_TWIST_BUTTONS
                                |wx.TR_SINGLE
                                |wx.TR_MULTIPLE
                                |wx.TR_NO_LINES
                                |wx.TR_FULL_ROW_HIGHLIGHT
                                |wx.TR_EDIT_LABELS
                                |wx.TR_EXTENDED

                                #wx.TR_HIDE_ROOT
                                #|wx.TR_NO_BUTTONS
                               )
        
        # self.tree_project = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        self.tree_project.SetForegroundColour(UI_COLOR_sceneTree_FG )
        self.tree_project.SetBackgroundColour(UI_COLOR_sceneTree_BG)
        self.tree_project.SetHelpText( u"fengx" )
        self.tree_project.SetMinSize( wx.Size( 200,300 ) )
        self.tree_project.SetMaxSize( wx.Size( 350,-1 ) )
        
          
        
        log=""
        dt = MyFileDropTarget(self.sceneWindow, log)
        self.SetDropTarget( dt ) 
        
        

        self.p_moveBar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.p_moveBar.SetBackgroundColour( UI_COLOR_movebar_BG )
        self.p_moveBar.SetMinSize( wx.Size( 100,25 ) )
        self.p_moveBar.SetMaxSize( wx.Size( -1,25 ) ) 
        #self.title=wx.StaticText(parent=self.p_moveBar,-1,"xx")
        self.title=wx.StaticText(self.p_moveBar, -1, "VisualFengx_1.0")
        self.title.SetBackgroundColour(UI_COLOR_movebar_BG )
        self.title.SetForegroundColour(UI_COLOR_movebar_FG )
        

        b_close_bmp=wx.Bitmap("b_max.bmp",wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(b_close_bmp, wx.BLUE)
        b_close_bmp.SetMask(mask)
        
        b_max_bmp=wx.Bitmap("b_max.bmp",wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(b_max_bmp, wx.BLUE)
        b_max_bmp.SetMask(mask)
        
        b_min_bmp=wx.Bitmap("b_max.bmp",wx.BITMAP_TYPE_BMP)
        mask = wx.Mask(b_min_bmp, wx.BLUE)
        b_min_bmp.SetMask(mask)
        

        
        self.b_close= wx.BitmapButton(self.p_moveBar, -1, b_close_bmp, style = wx.NO_BORDER)
        self.b_close.SetBackgroundColour(UI_COLOR_movebar_BG )
        self.b_close.Bind(wx.EVT_BUTTON, self.close)
        
        self.b_max= wx.BitmapButton(self.p_moveBar, -1, b_max_bmp, style = wx.NO_BORDER)
        self.b_max.SetBackgroundColour(UI_COLOR_movebar_BG )
        
        self.b_min= wx.BitmapButton(self.p_moveBar, -1, b_min_bmp, style = wx.NO_BORDER)
        self.b_min.SetBackgroundColour(UI_COLOR_movebar_BG )
        
        
        #self.b_close=wx.StaticBitmap(parent=self.p_moveBar,bitmap=wx.Bitmap("b_close.bmp"))
        #self.backgroundImage=wx.StaticBitmap(parent=self.p_moveBar,bitmap=bmp)
        
        self.sizebar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.sizebar.SetMinSize( wx.Size( 100,15 ) )
        self.sizebar.SetMaxSize( wx.Size( -1,15 ) ) 
        self.sizebar.SetBackgroundColour( UI_COLOR_sizebar_BG )


        self.p_mainTool = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.p_mainTool.SetMinSize( wx.Size( 100,5 ) )
        self.p_mainTool.SetMaxSize( wx.Size( -1,5 ) )
        self.p_mainTool.SetBackgroundColour(UI_COLOR_mainToolbar_BG)
     
     
        self.box_movebar = wx.BoxSizer( wx.HORIZONTAL )
        self.box_movebar.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
        self.box_movebar.Add( self.title, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
        self.box_movebar.AddSpacer( ( 0, 0), 1, wx.EXPAND, 0 )
        self.box_movebar.Add( self.b_min, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
        self.box_movebar.Add( self.b_max, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
        self.box_movebar.Add( self.b_close, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
        

        self.p_moveBar.SetSizer( self.box_movebar )
        self.p_moveBar.Layout()
        self.box_movebar.Fit( self.p_moveBar)
        


        Sizer_main_V.Add( self.p_moveBar, 1, wx.EXPAND |wx.ALL, 0 )
        Sizer_main_V.Add( self.p_mainTool, 1, wx.EXPAND |wx.ALL, 0 )

        
        bSizer_mainScene.Add( self.tree_project, 1, wx.ALL|wx.EXPAND, 0 )
        
        
        Sizer_main_V.Add( bSizer_mainScene, 7, wx.EXPAND, 0 )
        Sizer_main_V.Add( self.sizebar, 1, wx.EXPAND, 0 )
        
        
        
        self.SetSizer( Sizer_main_V )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        
        self.p_moveBar.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp) 
        self.p_moveBar.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown) 
        self.p_moveBar.Bind(wx.EVT_MOTION,  self.OnMove)
        self.p_moveBar.Bind(wx.EVT_RIGHT_UP,  self.popupmenu)
        
        #self.title.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp) 
        #self.title.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown) 
        #self.title.Bind(wx.EVT_MOTION,  self.OnMove)
        self.title.Bind(wx.EVT_RIGHT_UP,  self.popupmenu)
        
        # self.p_moveBar.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBackGroundm)
        #self.p_mainTool.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBackGround)
        #self.tree_project.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBackGround)
        #self.statusBar_main.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBackGround)
        #self.bg=wx.StaticBitmap(self.p_moveBar,-1,  bmp, (0,0))
        #self.bga=wx.Button(self.p_moveBar,-1)
        self.Bind(wx.EVT_UPDATE_UI,self.upDate)
        
        
        
        
        self.sizebar.Bind(wx.EVT_LEFT_UP, self.OnSizeMouseLeftUp) 
        self.sizebar.Bind(wx.EVT_LEFT_DOWN, self.OnSizeMouseLeftDown) 
        self.sizebar.Bind(wx.EVT_MOTION,  self.OnSizeMove)
        

    def popupmenu(self,event):
        self.ppmenu = wx.Menu()
        pyc=wx.NewId()
        self.newScene = wx.MenuItem( self.ppmenu, pyc, u"Console", wx.EmptyString, wx.ITEM_NORMAL )
        self.ppmenu.AppendItem( self.newScene )
        #self.ppmenu.AppendItem( self.newScene )
        self.Bind(wx.EVT_MENU, self.createPyConsole, id=pyc)
        self.PopupMenu(self.ppmenu)
        self.ppmenu.Destroy()
        

    def close(self,event):
            sys.exit()
    def upDate(self,event):        
        ()
        #self.SetStatusText(("FPS:  "+str(self.sceneWindow.FPS)))
    def __del__( self ):
        pass
       
    def OnMove(self, event):
        newPosX=event.GetPosition()[0]-self.lastPos[0]+self.pos[0]
        newPosY=event.GetPosition()[1]-self.lastPos[1]+self.pos[1]
        newPos=wx.Point=(newPosX,newPosY)
        self.mousePos[0]=event.GetPosition()[0]
        self.mousePos[1]=event.GetPosition()[1]
        if self.canMove:
            self.SetPosition(newPos)
            self.pos[0]=newPos[0]
            self.pos[1]=newPos[1]

    def OnMouseLeftDown(self, event):
        self.p_moveBar.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        self.p_moveBar.CaptureMouse()
        self.lastPos[0]=event.GetPosition()[0]
        self.lastPos[1]=event.GetPosition()[1]
        self.canMove=True
    
    def OnMouseLeftUp(self, event):
        self.p_moveBar.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        if self.p_moveBar.HasCapture():
            self.p_moveBar.ReleaseMouse()          
        self.canMove=False

    def OnEraseBackGround(self,event):
        dc=event.GetDC()
        if not dc:
            dc=wx.ClientDC(self)
            rect=self.GetUpdateRegion().Getbox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp=wx.Bitmap("MAIN_BG_IMAGE.bmp")
        bmp_movebar=wx.Bitmap("MAIN_MOVEBAR_IMAGE.bmp")
        #dc.DrawBitmap(bmp,0,0)
        self.TileBackground(dc,bmp)
    def OnEraseBackGroundm(self,event):
        dc=event.GetDC()
        if not dc:
            dc=wx.ClientDC(self)
            rect=self.GetUpdateRegion().Getbox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp=wx.Bitmap("MAIN_BG_IMAGE.bmp")
        bmp_movebar=wx.Bitmap("MAIN_MOVEBAR_IMAGE.bmp")
        #dc.DrawBitmap(bmp,0,0)
        self.TileBackground(dc,bmp_movebar)
        
        
        
    def TileBackground(self, dc,bmp):
            sz = self.GetClientSize()
            w = bmp.GetWidth()
            h = bmp.GetHeight()

            x = 0

            while x < sz.width:
                y = 0

                while y < sz.height:
                    dc.DrawBitmap(bmp, x, y)
                    y = y + h

                x = x + w       


    def OnSizeMove(self, event):
        self.sizebar.SetCursor(wx.StockCursor(wx.CURSOR_SIZENWSE))
        newSizeX=event.GetPosition()[0]-self.lastPos[0]+self.GetClientSize()[0]
        newSizeY=event.GetPosition()[1]-self.lastPos[1]+self.GetClientSize()[1]
        newSize=wx.Point=(newSizeX,newSizeY)
        if self.canSize:
            self.SetSize(newSize) 
        self.lastPos[0]=event.GetPosition()[0]
        self.lastPos[1]=event.GetPosition()[1]
        
    def OnSizeMouseLeftDown(self, event):
       
        self.sizebar.CaptureMouse()
        self.lastPos[0]=event.GetPosition()[0]
        self.lastPos[1]=event.GetPosition()[1]
        self.canSize=True


    def OnSizeMouseLeftUp(self, event):
        self.p_moveBar.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        if self.sizebar.HasCapture():
            self.sizebar.ReleaseMouse()          
        self.canSize=False
    def createPyConsole(self,event):
        console=PyConsoleFrame(parent=None,id=-1)
        console.Show()       


mainApp = wx.App()

mainWindow=mainFrame(parent=None)
mainWindow.Show()


mainApp.MainLoop()

