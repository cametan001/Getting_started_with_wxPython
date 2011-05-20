#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class MyFrame(wx.Frame):
    """ メニューを作る """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (400, 300))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)

        # 個々のメニューオブジェクトを作成する
        # ファイルメニュー、編集メニュー、書式メニュー、表示メニュー、ヘルプメニューの各オブジェクトを作成

        file_menu = wx.Menu()
        edit_menu = wx.Menu()
        help_menu = wx.Menu()

        # 各メニュー毎にメニューアイテムを作っていく

        # ファイルメニュー

        menuNew = file_menu.Append(wx.ID_NEW, "新規作成 (&N)", "ファイルを新しく作ります")
        menuOpen = file_menu.Append(wx.ID_OPEN, "ファイル (&F)", "ファイルを開きます")
        menuSave = file_menu.Append(wx.ID_SAVE, "上書き保存 (&S", "編集中のファイルに上書きで保存します")
        menuSaveas = file_menu.Append(wx.ID_SAVEAS, "名前を付けて保存 (&A)", "新しく名前をつけて保存します")

        file_menu.AppendSeparator()     # メニューセパレータ
        menuExit = file_menu.Append(wx.ID_EXIT, "終了 (&X)", "簡易エディタを終了します")

        # 編集メニュー
        menuUndo = edit_menu.Append(wx.ID_UNDO, "元に戻す (&U)", "編集を元に戻します")
        menuCut = edit_menu.Append(wx.ID_CUT, "切り取り (&T)", "選択箇所を切り取ります")

        menuCopy = edit_menu.Append(wx.ID_COPY, "コピー (&V(", "選択箇所をコピーします")
        menuPaste = edit_menu.Append(wx.ID_PASTE, "貼り付け (&P)", "切り取られた箇所を貼り付けます")

        # ヘルプメニュー
        menuHelp = help_menu.Append(wx.ID_HELP, "ヘルプの表示 (&H)", "プログラムのヘルプを表示します")
        menuAbout = help_menu.Append(wx.ID_ABOUT, "バージョン情報 (&A)", "プログラムのヘルプを表示します")

        # メニューバーを作成し、個々のメニューをメニューバーに追加していく
        menuBar = wx.MenuBar()
        menuBar.Append(file_menu, "ファイル (&F)")
        menuBar.Append(edit_menu, "編集 (&E)")
        menuBar.Append(help_menu, "ヘルプ (&H)")

        # 個々のメニューアイテムを、イベントハンドラにバインドする
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnSaveas, menuSaveas)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        
        self.Bind(wx.EVT_MENU, self.OnUndo, menuUndo)
        self.Bind(wx.EVT_MENU, self.OnCut, menuCut)
        self.Bind(wx.EVT_MENU, self.OnCopy, menuCopy)
        self.Bind(wx.EVT_MENU, self.OnPaste, menuPaste)
        self.Bind(wx.EVT_MENU, self.OnHelp, menuHelp)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        # メニューバーを Frame にセットする
        self.SetMenuBar(menuBar)

        # ステータスバーを作成する
        self.CreateStatusBar()

        # 表示
        self.Show(True)
        
    # メニューが選択されたら、選択されたことを標準出力に表示する
    def OnNew(self, event):
        print "Select New"

    def OnOpen(self, event):
        print "Select Open"

    def OnSave(self, event):
        print "Select Save"

    def OnSaveas(self, event):
        print "Select SaveAs"

    def OnUndo(self, event):
        print "Select Undo"

    def OnCut(self, event):
        print "Select Cut"

    def OnCopy(self, event):
        print "Select Copy"

    def OnPaste(self, event):
        print "Select Paste"

    def OnHelp(self, event):
        print "Select Help"

    def OnAbout(self, event):
        print "Select About"

    def OnExit(self, event):
        print "Select Exit"

app = wx.App(False)
frame = MyFrame(None, '簡易エディタ')
app.MainLoop()

# if __name__ == '__main__':
