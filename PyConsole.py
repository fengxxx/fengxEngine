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
        self.pyConsole= py.crust.Crust(self)


        #self.bg=wx.Panel(self,size=(900,900))
        #self.bg.Bind(wx.EVT_PAINT, self.OnPaint)
        


        
        # #set icon
        # try:
            # self.tbicon = TB_Icon(self)
        # except:
            # self.tbicon = None
    def OnPaint(self, evt):
        pdc = wx.PaintDC(self)
        try:
            dc = wx.GCDC(pdc)
        except:
            dc = pdc
        # rect = wx.Rect(0,0, 100, 100)
        # for RGB, pos in [((178,  34,  34), ( 50,  90)),
                         # (( 35, 142,  35), (110, 150)),
                         # ((  0,   0, 139), (170,  90))
                         # ]:
            # r, g, b = RGB
            # penclr   = wx.Colour(r, g, b, wx.ALPHA_OPAQUE)
            # brushclr = wx.Colour(r, g, b, 128)   # half transparent
            # dc.SetPen(wx.Pen(penclr))
            # dc.SetBrush(wx.Brush(brushclr))
            # rect.SetPosition(pos)
            # dc.DrawRoundedRectangleRect(rect, 8)
            
        # some additional testing stuff
        dc.SetPen(wx.Pen(wx.Colour(0,0,255, 196)))
        dc.SetBrush(wx.Brush(wx.Colour(0,0,255, 64)))
        dc.DrawCircle(50, 275, 25)
        dc.DrawEllipse(100, 275, 75, 50)
        

if __name__ == '__main__':
    EN_Dic = {
        "grap"                    :    "&Grap",
        "save"                    :    "&Save",
        "show"                    :    "Show",
        "hide"                    :    "Hide",
        "show_all_windows"        :    "Show All &Window",
        "hide_all_windows"        :    "&Hide All Window",
        "close"                   :    "&Close",
        "delete"                  :    "&Delete",
        "exit"                    :    "&Exit",
        "delete_all_images"       :    "Delete All &Images",
        "show_in_explorer"        :    "Show In &Explorer",
        "reset_position"          :    "&Reset Position",
        "hide_others"             :    "Hide &Others"
    }

    mainApp = wx.PySimpleApp()
    newFrame = PyConsoleFrame(parent=None, id=-1)
    newFrame.Show()
    #newFrame.SetBackgroundColour((120,120,120))
    mainApp.MainLoop()
