#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx, time

class MyFrame(wx.Frame):

    """ Frame をベースに新しいクラスを作る """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (400, 300))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        print "step 2+"
        time.sleep(2)
        self.Show(False)                # ここでは False に変更してみる。
        print "step 2++"
        time.sleep(2)

print "step 1"
app = wx.App(False)
print "step 2"
frame = MyFrame(None, '簡易エディタ')
print "step 3"
time.sleep(2)
frame.Show(True)                        # ここで True にした。
print "step 4"
time.sleep(2)
app.MainLoop()
# if __name__ == '__main__':
