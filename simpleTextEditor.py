#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class MyFrame(wx.Frame):
    """We simply defive a new class of Frame."""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (200, 100))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()

# if __name__ == '__main__':
