#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class ExamplePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap = 5, vgap = 5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.quote = wx.StaticText(self, label = "Your quote: ")
        grid.Add(self.quote, pos = (0, 0))

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger = wx.TextCtrl(self, size = (200, 300), style = wx.TE_MULTILINE | wx.TE_READONLY)

        # A button
        self.button = wx.Button(self, label = "Save")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label = "Your name :")
        grid.Add(self.lblname, pos = (1, 0))
        self.editname = wx.TextCtrl(self, value = "Enter here your name", size = (140, -1))
        grid.Add(self.editname, pos = (1, 1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # the combobox Control
        self.sampleList = ['friends', 'advertising', 'web search', 'Yellow Pages']
        self.lblhear = wx.StaticText(self, label = "How did you hear from us?")
        grid.Add(self.lblhear, pos = (3, 0))
        self.edithear = wx.ComboBox(self, size = (95, -1), choices = self.sampleList, style = wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.edithear)

        # add a spacer to the sizer
        grid.Add((10, 40), pos = (2, 0))

        # Checkbox
        self.insure = wx.CheckBox(self, label = "Do you want Insured Shipment?")
        grid.Add(self.insure, pos = (4, 0), span = (1, 2), flag = wx.BOTTOM, border = 5)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # Radio Boxes
        radioList = ['blue', 'red', 'yewllow', 'orange', 'green', 'purple', 'navy blue', 'black', 'gray']
        rb = wx.RadioBox(self, label = "What color would you like?", pos = (20, 210), choices = radioList, majorDimension = 3, style = wx.RA_SPECIFY_COLS)
        grid.Add(rb, pos = (5, 0), span = (1, 2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(self.logger)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(self.button, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)

    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self, event):
        self.logger.AppendText(" Click on object with Id %d\n" % event.GetId())
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())


app = wx.App(False)
frame = wx.Frame(None, title = "Demo with Notebook")
nb = wx.Notebook(frame)

panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()



# if __name__ == '__main__':
