#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class MyFrame(wx.Frame):
    """ 文字色と背景色とフォントを変える """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (400, 300))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)

        # 文字色の指定
        self.control.SetForegroundColour("#ff0000")
        # 背景色の指定
        self.control.SetBackgroundColour("#30ffff")
        # フォントの指定
        font = wx.Font(24,
                       wx.NORMAL,        # wx.FONTFAMILY_DEDAULT
                       wx.ITALIC,        # wx.FONTSTYLE_ITALIC
                       wx.BOLD)          # wx.FONTWEIGHT_BOLD
        self.control.SetFont(font)
        # 表示
        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, '簡易エディタ')
app.MainLoop()

# if __name__ == '__main__':
