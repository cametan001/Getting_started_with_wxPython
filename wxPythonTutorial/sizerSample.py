#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title = title, size = (200, -1))

        # ボタンを作成
        self.button_cupnudle = wx.Button(self, wx.ID_ANY, "カップヌードル")
        self.button_bigmac = wx.Button(self, wx.ID_ANY, "ビッグマック")
        self.button_gyudon = wx.Button(self, wx.ID_ANY, "牛丼")

        # 水平方向に並べる BoxSizer を作成
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # ボタンを BoxSizer に追加
        self.sizer.Add(self.button_cupnudle, 1, wx.SHAPED | wx.ALIGN_TOP)
        self.sizer.Add(self.button_bigmac, 0, wx.FIXED_MINSIZE | wx.ALIGN_CENTER_VERTICAL)
        self.sizer.Add(self.button_gyudon, 0, wx.FIXED_MINSIZE | wx.ALIGN_BOTTOM)

        # レイアウトを行う
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.sizer.Fit(self)

        # Frame を表示する。
        self.Show()

app = wx.App(False)
frame = MainWindow(None, "Sizer サンプル")
app.MainLoop()
# if __name__ == '__main__':
