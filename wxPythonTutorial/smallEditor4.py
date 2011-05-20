#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class MyFrame(wx.Frame):
    """ メニューから終了する """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (400, 300))

        file_menu = wx.Menu()

        # Exitメニューアイテムのオブジェクト(バインドするときのソース)
        menuExit = file_menu.Append(wx.ID_EXIT, "終了 (&X)", "簡易エディタの終了をします")

        # メニューバーオブジェクトを作って、そこにファイルメニューオブジェクトを追加
        menuBar = wx.MenuBar()

        self.SetMenuBar(menuBar)

        self.SetMenuBar(menuBar)
        menuBar.Append(file_menu, "ファイル (&F)")

        # イベントに対して、ハンドラとソースをバインドする
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # 表示
        self.Show(True)

    # 終了のためのメソッド
    def OnExit(self, event):
        self.Close(True)

app = wx.App(False)
frame = MyFrame(None, '簡易エディタ')
app.MainLoop()

# if __name__ == '__main__':
