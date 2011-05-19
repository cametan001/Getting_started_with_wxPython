#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

app = wx.App()                          # False を削除
# frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame = wx.Frame(None, title = "Hello World")
frame.Show(True)
print "Hello, wxPython"                 # この行を追加
app.MainLoop()
