import wx
import wx.aui
from _hierarchy import *
from _globalData import *
from _scene import *
class mainFrame(wx.Frame):
    global MAIN_WINDOW_SIZE
    global ICON_PATH
    global MAIN_BG_COLOR
    def __init__(self, parent, id=-1, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE |
                                            wx.SUNKEN_BORDER |
                                            wx.CLIP_CHILDREN):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        #---------------main Window settings----->>>>
        self.SetBackgroundColour(MAIN_BG_COLOR)
        self.icon = wx.Icon(ICON_PATH, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)

        self.statusbar =self.CreateStatusBar(2, wx.ST_SIZEGRIP)
        self.statusbar.SetStatusWidths([-2, -3])
        self.statusbar.SetStatusText("fengxEngine", 0)
        self.statusbar.SetStatusText("selcetion", 1)

        # min size for the frame itself isn't completely done.
        # see the end up FrameManager::Update() for the test
        # code. For now, just hard code a frame minimum size
        self.SetMinSize(wx.Size(400, 300))
        
        #--------------main MenuBar--------------->>>>
        self.menuBar = wx.MenuBar()
        self.SetMenuBar(self.CreateMenuBar())
        #--------------main MenuBar--------------<<<<<
        #self.SetStatusText("fengxEngine")



        self._mgr.AddPane(mainGlCanvas(self), wx.aui.AuiPaneInfo().
                          Name("test10").Caption("Text Pane").
                          Bottom().Layer(1).Position(1).CloseButton(True).MaximizeButton(True))
        self._mgr.GetPane("test10").Show().Bottom().Layer(0).Row(0).Position(0)

        self._mgr.AddPane(sceneTreePanel(self), wx.aui.AuiPaneInfo().
                  Name("test2").Caption("Pane Captionx").Left().
                  CloseButton(True).MaximizeButton(True))  
        self._mgr.GetPane("test2").Show().Bottom().Layer(0).Row(1).Position(0)
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

        TEST_IMPORT = wx.NewId()

        file_menu.Append(TEST_IMPORT,"&Import")
        file_menu.Append(TEST_QUIT, "&Exit")
        help_menu.Append(TEST_ABOUT, "&About")


        menu_bar = wx.MenuBar()

        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")


        #self.Bind(wx.EVT_MENU, self.OnAbout, id=TEST_ABOUT)
        self.Bind(wx.EVT_MENU, self.importFile, id=TEST_IMPORT)
        self.Bind(wx.EVT_MENU, self.close, id=TEST_QUIT)
        #self.Bind(wx.EVT_CLOSE, self.OnQuit)
        return menu_bar
    def close(self,event):
        self.Close()

    def importFile(self,event):
        
        #p=wx.openFileDialog()
        file_wildcard = "OBJ files(*.obj)|*.obj|All files(*.*)|*.*"   
        dlg = wx.FileDialog(self, "Open paint file...",  
                            os.getcwd(),   
                            style = wx.OPEN,  
                            wildcard = file_wildcard)  
        if dlg.ShowModal() == wx.ID_OK:  
            self.filename = dlg.GetPath()  
            
            
        dlg.Destroy()  
        #if dlg.GetPath() !="":
        importObjFile(self.filename)#"D://desktop//testObj.obj")


mainApp = wx.PySimpleApp()
frame =mainFrame(None, wx.ID_ANY, "fengxEngine", size=(750, 590))
frame.Show()
mainApp.MainLoop()
