#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class MyFrame(wx.Frame):
    """ メニューを作る """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (400, 300))

        # 個々のメニューオブジェクトを作成する
        # ファイルメニュー、編集メニュー、書式メニュー、表示メニュー、ヘルプメニューの各メニューオブジェクトを作成
        file_menu = wx.Menu()
        edit_menu = wx.Menu()
        format_menu = wx.Menu()
        view_menu = wx.Menu()
        help_menu = wx.Menu()

        # 各メニュー毎にメニューアイテムを作っていく
        # ファイルメニュー
        file_menu.Append(wx.ID_NEW, "新規作成 (&N)", "ファイルを新しく作ります")
        file_menu.Append(wx.ID_OPEN, "ファイル (&F)", "ファイルを開きます")
        file_menu.Append(wx.ID_SAVE, "上書き保存 (&S)", "編集中のファイルに上書きで保存します")
        file_menu.Append(wx.ID_SAVEAS, "名前を付けて保存 (&A)", "新しく名前をつけて保存します")

        file_menu.AppendSeparator()     # メニューセパレータ
        file_menu.Append(wx.ID_EXIT, "修了 (&X)", "簡易エディタを終了します")

        # 編集メニュー
        edit_menu.Append(wx.ID_UNDO, "元に戻す (&U)", "編集を元に戻します")
        edit_menu.Append(wx.ID_CUT, "切り取り (&T)", "選択箇所を切り取ります")
        edit_menu.Append(wx.ID_COPY, "コピー (&V)", "選択箇所をコピーします")
        edit_menu.Append(wx.ID_PASTE, "貼り付け (&P)", "切り取られた箇所を貼り付けます")

        # ヘルプメニュー
        help_menu.Append(wx.ID_HELP, "ヘルプの表示 (&H)", "プログラムのヘルプを表示します")

        # メニューバーを作成する
        menuBar = wx.MenuBar()
        # 個々のメニューをメニューバーに追加していく
        menuBar.Append(file_menu, "ファイル (&F)")
        menuBar.Append(edit_menu, "編集 (&E)")
        menuBar.Append(format_menu, "書式 (&O)")
        menuBar.Append(view_menu, "表示 (&V)")
        menuBar.Append(help_menu, "ヘルプ (&H)")

        # メニューバーを Frame にセットする
        self.SetMenuBar(menuBar)
        # ステータスバーを作成する
        self.CreateStatusBar()
        # 表示
        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, '簡易エディタ')
app.MainLoop()

# if __name__ == '__main__':
