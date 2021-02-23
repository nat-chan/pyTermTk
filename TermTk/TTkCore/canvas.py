#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2021 Eugenio Parodi <ceccopierangiolieugenio AT googlemail DOT com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import TermTk.libbpytop as lbt
from TermTk.TTkCore.constant import TTkK
from TermTk.TTkCore.log import TTkLog
from TermTk.TTkCore.cfg import *
from TermTk.TTkCore.color import *
from TermTk.TTkCore.helper import *
from TermTk.TTkGui.theme import *

class TTkCanvas:
    '''
    TTkCanvas
    canvas window primitives
    ...
    Attributes
    ----------
    Methods
    -------
    __init__({})
      input obj{ width, height}

    resize(w, h)
      - resize the canvas keeping or cutting the current one
      in  w = the width of the new canvas
      in  h = the height of the new canvas
    '''
    __slots__ = ('_widget', '_width', '_height', '_newWidth', '_newHeight','_theme', '_data', '_colors', '_visible')
    def __init__(self, *args, **kwargs):
        self._widget = kwargs.get('widget', None)
        self._visible = True
        self._width = 0
        self._height = 0
        self._newWidth = kwargs.get('width', 0 )
        self._newHeight = kwargs.get('height', 0 )
        self.updateSize()
        # self.resize(self._width, self._height)
        self._theme = TTkTheme()
        # TTkLog.debug((self._width, self._height))

    def getWidget(self): return self._widget

    def updateSize(self):
        if not self._visible: return
        w,h = self._newWidth, self._newHeight
        if w  == self._width and h == self._height:
            return
        self._data = [[]]*h
        self._colors = [[]]*h
        for i in range(0,h):
            self._data[i] = [' ']*w
            self._colors[i] = [TTkColor.RST]*w
        self._width  = w
        self._height = h

    def resize(self, w, h):
        self._newWidth = w
        self._newHeight = h

    def clean(self, pos=(0, 0), size=None):
        if not self._visible: return
        x,y = pos
        w,h = size if size is not None else (self._width, self._height)
        for iy in range(y,y+h):
            for ix in range(x,x+w):
                self._data[iy][ix] = ' '
                self._colors[iy][ix] = TTkColor.RST

    def hide(self):
        self._visible = False

    def show(self):
        self._visible = True


    def zTop(self):
        # TODO: Figure out how to use this
        pass

    def _set(self, _y, _x, _ch, _col=TTkColor.RST):
        if _y < self._height  and \
           _x < self._width and \
           _x >= 0 and _y >=0 :
            self._data[_y][_x] = _ch
            self._colors[_y][_x] = _col

    def drawText(self, pos, text, color=TTkColor.RST):
        if not self._visible: return
        x,y = pos
        arr = list(text)
        for i in range(0, len(arr)):
            self._set(y, x+i, arr[i], color)


    def drawBox(self, pos, size, color=TTkColor.RST):
        self.drawGrid(pos=pos, size=size, color=color)

    def drawGrid(self, pos, size, hlines=[], vlines=[], color=TTkColor.RST, grid=0):
        if not self._visible: return
        x,y = pos
        w,h = size
        gg = self._theme.grid[grid]
        # 4 corners
        self._set(y,     x,     gg[2], color)
        self._set(y,     x+w-1, gg[3], color)
        self._set(y+h-1, x,     gg[4], color)
        self._set(y+h-1, x+w-1, gg[5], color)
        if w > 2:
            for i in range(x+1,x+w-1):
                self._set(y,   i, gg[0], color)
                self._set(y+h-1, i, gg[0], color)
        if h > 2:
            for i in range(y+1,y+h-1):
                self._set(i, x,   gg[1], color)
                self._set(i, x+w-1, gg[1], color)
        # Draw horizontal lines
        for iy in hlines:
            iy += y
            if not (0 < iy < h): continue
            self._set(iy, x,     gg[6], color)
            self._set(iy, x+w-1, gg[7], color)
            if w > 2:
                for ix in range(x+1,x+w-1):
                    self._set(iy, ix, gg[10], color)
        # Draw vertical lines
        for ix in vlines:
            ix+=x
            if not (0 < ix < w): continue
            self._set(y,     ix, gg[8], color)
            self._set(y+h-1, ix, gg[9], color)
            if h > 2:
                for iy in range(y+1,y+h-1):
                    self._set(iy, ix, gg[11], color)
        # Draw intersections
        for iy in hlines:
            for ix in vlines:
                self._set(y+iy, x+ix, gg[12], color)

    def drawScroll(self, pos, size, slider, orientation, color):
        if not self._visible: return
        x,y = pos
        f,t = slider # slider from-to position
        if orientation == TTkK.HORIZONTAL:
            for i in range(x+1,x+size-1):
                self._set(y,x+i, self._theme.hscroll[1], color)
            for i in range(f,t):
                self._set(y,x+i, self._theme.hscroll[2], color)
            self._set(y,x, self._theme.hscroll[0], color)
            self._set(y,x+size-1, self._theme.hscroll[3], color)
        else:
            for i in range(y+1,y+size-1):
                self._set(y+i,x, self._theme.vscroll[1], color)
            for i in range(f,t):
                self._set(y+i,x, self._theme.vscroll[2], color)
            self._set(y,x, self._theme.vscroll[0], color)
            self._set(y+size-1,x, self._theme.vscroll[3], color)

        pass

    def execPaint(self, winw, winh):
        pass

    '''
    geom  = (x,y,w,h)
    bound = (x,y,w,h)
    '''
    def paintCanvas(self, canvas, geom, slice, bound):
        # TTkLog.debug(f"PaintCanvas:{(x,y,w,h)}")
        x, y, w, h  = geom
        bx,by,bw,bh = bound
        # out of bound
        if not self._visible: return
        if not canvas._visible: return
        if x+w < bx or y+h<by or bx+bw<x or by+bh<y:
            return
        if x>=self._width:    x=self._width-1
        if y>=self._height:   y=self._height-1
        if w>=self._width-x:  w=self._width-x
        if h>=self._height-y: h=self._height-y

        xoffset = 0 if x>=bx else bx-x
        yoffset = 0 if y>=by else by-y
        wslice = w if x+w < bx+bw else bx+bw-x
        hslice = h if y+h < by+bh else by+bh-y

        for iy in range(yoffset,hslice):
            for ix in range(xoffset,wslice):
                #TTkLog.debug(f"PaintCanvas:{(ix,iy)}")
                self._data[y+iy][x+ix]   = canvas._data[iy][ix]
                self._colors[y+iy][x+ix] = canvas._colors[iy][ix]

    def pushToTerminal(self, x, y, w, h):
        # TTkLog.debug("pushToTerminal")
        lastcolor = None
        for y in range(0, self._height):
            ansi = lbt.Mv.t(y+1,1)
            for x in range(0, self._width):
                ch = self._data[y][x]
                color = self._colors[y][x]
                if color != lastcolor:
                    ansi += color
                    lastcolor = color
                ansi+=ch
            lbt.Term.push(ansi)