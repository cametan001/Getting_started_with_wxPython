#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class MyFrame(wx.Frame):

    """ Frame をベースに新しいクラスを作る """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (400, 300))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, '簡易エディタ')
app.MainLoop()

# if __name__ == '__main__':
