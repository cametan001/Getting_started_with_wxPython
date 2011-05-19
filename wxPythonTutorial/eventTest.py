#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

for x in dir(wx):
    if x.startswith('EVT_'):
        print x

# if __name__ == '__main__':
