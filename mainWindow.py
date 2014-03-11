#coding:utf-8 
import wx
#import sys
import math
from _hierarchy import *
from _globalData import *
from _scene import *

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
        dlg.GetColourData().SetChooseFull(True)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            print ('You selected: %s\n' % str(data.GetColour().Get()))
        dlg.Destroy()


mainApp = wx.PySimpleApp()
newFrame = mainFrame(parent=None, id=-1)
newFrame.Show()
newFrame.SetBackgroundColour(MAIN_BG_COLOR)
#print dir(newFrame)
mainApp.MainLoop()
