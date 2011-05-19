#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx
for name in dir(wx):
    if name.startswith("ID_"):
        print name, eval("wx." + name)

# if __name__ == '__main__':
