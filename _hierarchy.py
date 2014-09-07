import wx.lib.mvctree  as  tree
import wx
from  _globalData import *
from  _data import *
import os
import  _scene 
class sceneTree(wx.TreeCtrl):
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
                     

class sceneTreePanel(wx.Panel):
    def __init__(self, parent):
        # Use the WANTS_CHARS style so the panel doesn't eat the Return key.
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        #self.log = log
        tID = wx.NewId()

        self.tree = sceneTree(self, tID, (0,0) , (100,100),
                               wx.TR_HAS_BUTTONS
                                |wx.TR_TWIST_BUTTONS
                                | wx.TR_SINGLE
                                | wx.TR_MULTIPLE
                                |wx.TR_NO_LINES
                                |wx.TR_FULL_ROW_HIGHLIGHT
                                |wx.TR_EDIT_LABELS
                                #|wx.TR_HIDE_ROOT
                                |wx.TR_EXTENDED
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

        self.root = self.tree.AddRoot("scene")
        self.tree.SetPyData(self.root, None)
        #self.tree.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        #self.tree.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        #for s in Objects:
        child = self.tree.AppendItem(self.root, "testObj")
        self.tree.SetPyData(child, None)


        self.tree.Expand(self.root)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self.tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED,self.OnSelChanged, self.tree)# self.updateTree,self.tree)#
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginEdit, self.tree)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.OnEndEdit, self.tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivate, self.tree)

        self.tree.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDClick)
        self.tree.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.tree.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        #self.getTheObj()
    def updateTree(self,event):
        if len(Objects)>0:
            for s in Objects:
                child = self.tree.AppendItem(self.root, s.name)
                self.tree.SetPyData(child, None)
                #self.tree.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                #self.tree.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
        '''
            for y in range(2):
                last = self.tree.AppendItem(child, "item %d-%s" % (x, chr(ord("a")+y)))
                self.tree.SetPyData(last, None)
                #self.tree.SetItemImage(last, fldridx, wx.TreeItemIcon_Normal)
                #self.tree.SetItemImage(last, fldropenidx, wx.TreeItemIcon_Expanded)

                for z in range(2):
                    item = self.tree.AppendItem(last,  "item %d-%s-%d" % (x, chr(ord("a")+y), z))
                    self.tree.SetPyData(item, None)
                    #self.tree.SetItemImage(item, fileidx, wx.TreeItemIcon_Normal)
                    #self.tree.SetItemImage(item, smileidx, wx.TreeItemIcon_Selected)
        '''
    def getTheObj(self,event):
        print os.curdir 
        objFiles=os.listdir(".")
        for  f in objFiles:
            print  os.path.splitext(f)
            if os.path.splitext(f)[1]==".obj":
                print "..................."
                print os.path.splitext(f)[0]
                child1 = self.tree.AppendItem(self.root, os.path.splitext(f)[0])
                self.tree.SetPyData(child1, None)
                #self.importObjFile()

    
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
            p=self.tree.GetItemText(item)+".obj"
            #_scene.importObjFile(p)
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
'''
(TR_EXTENDED 'TR_DEFAULT_STYLE', 'TR_EDIT_LABELS', 'TR_EXTENDED', 'TR_FULL_ROW_HIGHLIGHT',
'TR_HAS_BUTTONS', 'TR_HAS_VARIABLE_ROW_HEIGHT', 'TR_HIDE_ROOT', 'TR_LINES_AT_ROOT', 'TR_MAC_BUTTONS',
'TR_MULTIPLE', 'TR_NO_BUTTONS', 'TR_NO_LINES', 'TR_ROW_LINES', 'TR_SINGLE', 'TR_TWIST_BUTTONS')

'''      