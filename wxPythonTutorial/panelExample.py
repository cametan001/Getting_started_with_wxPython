#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class ExamplePanel(wx.Panel):

    def __init__(self, parent):

        wx.Panel.__init__(self, parent)

        self.SetBackgroundColour("silver")

        wx.StaticText(self, label = "ラベル1 :", pos = (10, 10))
        wx.StaticText(self, label = "ラベル2 :", pos = (100, 10))
        wx.StaticText(self, label = "ラベル3 :", pos = (200, 10))

        wx.StaticText(self, label = "ラベル4 :", pos = (10, 30))

        wx.StaticText(self, label = "ラベル5 :", pos = (100, 30), size = (20, -1))
        wx.StaticText(self, label = "ラベル6 :", pos = (200, 30), size = (-1, 10))

        wx.StaticText(self, label = "ラベル7 :", pos = (10, 60), size = (200, -1))
        wx.StaticText(self, label = "ラベル8 :", pos = (30, 60))
        wx.StaticText(self, label = "ラベル9 :", pos = (200, 60))

app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
        

# if __name__ == '__main__':
