#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

for name in dir(wx):
    if name.startswith("TE_"):
        print name

# if __name__ == '__main__':
