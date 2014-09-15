import wx.lib.mvctree  as  tree
import wx
from  _globalData import *
from  _data import *
import os
import  _scene 
               
class sceneTreePanel(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
        # Use the WANTS_CHARS style so the panel doesn't eat the Return key.
        #wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)
        #self.Bind(wx.EVT_SIZE, self.OnSize)

  

        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])

        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NEW_DIR,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        icon=wx.Icon("App.ico", wx.BITMAP_TYPE_ICO)
        
        smileidx    = il.Add(wx.ArtProvider_GetBitmap(wx.ART_TICK_MARK, wx.ART_OTHER, isz))#il.Add(wx.BitmapFromIcon(icon))

        self.SetImageList(il)
        self.il = il

        # NOTE:  For some reason tree items have to have a data object in
        #        order to be sorted.  Since our compare just uses the labels
        #        we don't need any real data, so we'll just use None below for
        #        the item data.

        self.root = self.AddRoot("scene")
        self.SetPyData(self.root, None)
        #self.tree.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        #self.tree.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        #for s in Objects:
        child = self.AppendItem(self.root, "mainCamera")
        c_light = self.AppendItem(self.root, "mainLight")
         

        self.SetPyData(child, None)
        self.SetPyData(c_light, None)

        self.Expand(self.root)
  
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self)
        self.Bind(wx.EVT_TREE_SEL_CHANGED,self.OnSelChanged, self)# self.updateTree,self.tree)#
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginEdit, self)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.OnEndEdit, self)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivate, self)

 
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnRightUp)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        #self.getTheObj()
    def updateTree(self):
       
        if len(ModelObjects)>0:
            for s in ModelObjects:
                print "xxxxxxxxxxx"
                if s.mesh.name=="" or s.mesh.name==" ": 
                    child = self.AppendItem(self.root, s.name)
                else:
                    child = self.AppendItem(self.root, s.mesh.name)
                self.SetPyData(child, None)
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
                self.SetPyData(child1, None)
                #self.importObjFile()

    
    def OnRightDown(self, event):
        pt = event.GetPosition();
        item, flags = self.HitTest(pt)
        if item:
            print ("OnRightClick: %s, %s, %s\n" %
                               (self.GetItemText(item), type(item), item.__class__))
            self.SelectItem(item)

    def OnRightUp(self, event):
        pt = event.GetPosition();
        item, flags = self.HitTest(pt)
        print item
        if not item:
            event.Skip()
            return

        #if not self.IsItemEnabled(item):
        #    event.Skip()
        #    return

        
        menu = wx.Menu()

        item1 = menu.Append(wx.ID_ANY, "Change item background colour")
        item2 = menu.Append(wx.ID_ANY, "Modify item text colour")
        menu.AppendSeparator()

        item4 = menu.Append(wx.ID_ANY, "Change item font")
        menu.AppendSeparator()

        #if ishtml:
        #    strs = "Set item as non-hyperlink"
        #else:
        #    strs = "Set item as hyperlink"
            
        menu.AppendSeparator()

        item13 = menu.Append(wx.ID_ANY, "Insert separator")
        menu.AppendSeparator()
        
        item7 = menu.Append(wx.ID_ANY, "Disable item")
        
        menu.AppendSeparator()
        item8 = menu.Append(wx.ID_ANY, "Change item icons")
        menu.AppendSeparator()
        item9 = menu.Append(wx.ID_ANY, "Get other information for this item")
        menu.AppendSeparator()
    
        self.PopupMenu(menu)
        menu.Destroy()

    def OnBeginEdit(self, event):
        print ("OnBeginEdit\n")
        # show how to prevent edit...
        item = event.GetItem()
        if item and self.GetItemText(item) == "The Root Item":
            wx.Bell()
            print ("You can't edit this one...\n")

            # Lets just see what's visible of its children
            cookie = 0
            root = event.GetItem()
            (child, cookie) = self.GetFirstChild(root)

            while child.IsOk():
                print ("Child [%s] visible = %d" %
                                   (self.GetItemText(child),
                                    self.IsVisible(child)))
                (child, cookie) = self.GetNextChild(root, cookie)

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
        item, flags = self.HitTest(pt)
        
        if item:
            print ("OnLeftDClick: %s\n" % self.GetItemText(item))
            p=self.GetItemText(item)+".obj"
            parent = self.GetItemParent(item)
            if parent.IsOk():
                self.SortChildren(parent)
        event.Skip()

    def OnSize(self, event):
        w,h = self.GetClientSizeTuple()
        self.SetDimensions(0, 0, w, h)


    def OnItemExpanded(self, event):
        item = event.GetItem()
        if item:
            print ("OnItemExpanded: %s\n" % self.GetItemText(item))

    def OnItemCollapsed(self, event):
        item = event.GetItem()
        if item:
            print ("OnItemCollapsed: %s\n" % self.GetItemText(item))

    def OnSelChanged(self, event):
        self.item = event.GetItem()
        if self.item:
            print ("OnSelChanged: %s\n" % self.GetItemText(self.item))
            if wx.Platform == '__WXMSW__':
                print ("BoundingRect: %s\n" %
                                   self.GetBoundingRect(self.item, True))
            #items = self.GetSelections()
            #print map(self.GetItemText, items)
        event.Skip()


    def OnActivate(self, event):
        print "OnActive"
        if self.item:
            print ("OnActivatexxxx: %s\n" % self.GetItemText(self.item))


#---------------------------------------------------------------------------
'''
(TR_EXTENDED 'TR_DEFAULT_STYLE', 'TR_EDIT_LABELS', 'TR_EXTENDED', 'TR_FULL_ROW_HIGHLIGHT',
'TR_HAS_BUTTONS', 'TR_HAS_VARIABLE_ROW_HEIGHT', 'TR_HIDE_ROOT', 'TR_LINES_AT_ROOT', 'TR_MAC_BUTTONS',
'TR_MULTIPLE', 'TR_NO_BUTTONS', 'TR_NO_LINES', 'TR_ROW_LINES', 'TR_SINGLE', 'TR_TWIST_BUTTONS')

'''      