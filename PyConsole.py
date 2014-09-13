#-----use wx GUI
import wx
import wx.py as py
from   _globalData import*
class PyConsolePanel(wx.Panel):
    def __init__(self, parent):
        intro = 'Welcome To PyCrust %s - The Flakiest Python Shell' % wx.py.version.VERSION
        self.pyConsole= wx.py.shell.Shell(self, -1, introText="fengxEngine")
        
        
        
        
class PyConsoleFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'fengxEngine', size=(585, 405),style=wx.DEFAULT_FRAME_STYLE)
        #---------------main Window settings----->>>>
        self.SetBackgroundColour((225,225,225))#MAIN_BG_COLOR)
        self.icon = wx.Icon(ICON_PATH, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        intro = 'Welcome To PyCrust %s - The Flakiest Python Shell' % py.version.VERSION
        self.pyConsole= py.shell.Shell(self, -1, introText="fengxEngine")

        
        
        
        

if __name__ == '__main__':
    mainApp = wx.PySimpleApp()
    newFrame = PyConsoleFrame(parent=None, id=-1)
    newFrame.Show()
    newFrame.SetBackgroundColour((120,120,120))
    mainApp.MainLoop()
