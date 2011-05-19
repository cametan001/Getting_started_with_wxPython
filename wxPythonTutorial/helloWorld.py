#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

app = wx.App(False)                     # 1. アプリケーションの作成
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # 2. トップレベルウィンドウの作成
frame.Show(True)                                 # トップレベルウィンドウの表示
app.MainLoop()

# if __name__ == '__main__':
