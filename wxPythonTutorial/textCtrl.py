#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class MyFrame(wx.Frame):
    """ Frame をベースに新しいクラスを作る """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (400, 300))
        self.control = wx.TextCtrl(self,
                                   style = wx.TE_MULTILINE | wx.TE_RIGTH | TE_AUTO_URL | wx.TE_RICH)
        self.Show(True)
        print self.control.GetDegaultStyle()

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)
app.MainLoop()

# if __name__ == '__main__':
