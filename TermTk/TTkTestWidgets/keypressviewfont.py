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

from TermTk.TTkCore.TTkTerm.inputkey import TTkKeyEvent, mod2str, key2str
from TermTk.TTkCore.TTkTerm.inputmouse import TTkMouseEvent
from TermTk.TTkCore.helper import TTkHelper
from TermTk.TTkCore.signal import pyTTkSlot
from TermTk.TTkCore.constant import TTkK
from TermTk.TTkCore.timer import TTkTimer
from TermTk.TTkCore.color import TTkColor
from TermTk.TTkWidgets.widget import TTkWidget

class TTkKeyPressViewFont():
    bitmap = {
        ' ':[
          "   ",
          "   ",
          "   ",
            ],
        '!':[
          " ▖ ",
          " ▌ ",
          " ▖ ",
            ],
        '\'':[
          " ▖ ",
          " ▘ ",
          "   ",
            ],
        '"':[
          "▗▗ ",
          "▝▝ ",
          "   ",
            ],
        '#':[
          "▗▗ ",
          "▜▜▘",
          "▜▜▘",
            ],
        '$':[
          "▗▄▖",
          "▚▙ ",
          "▄▙▘",
            ],
        '%':[
          "▄ ▖",
          "▀▞ ",
          "▞▐▌",
            ],
        '&':[
          " ▄ ",
          "▝▖ ",
          "▐▞▖",
            ],
        '(':[
          " ▗ ",
          " ▌ ",
          " ▚ ",
            ],
        ')':[
          "▗  ",
          " ▌ ",
          "▗▘ ",
            ],
        '*':[
          "▗▗ ",
          "▗▚ ",
          "   ",
            ],
        '+':[
          "   ",
          "▗▙ ",
          " ▘ ",
            ],
        ',':[
          "   ",
          "   ",
          "▗▘ ",
            ],
        '-':[
          "   ",
          "▗▄ ",
          "   ",
            ],
        '.':[
          "   ",
          "   ",
          "▗  ",
            ],
        '/':[
          "  ▖",
          " ▞ ",
          "▞  ",
            ],
        '0':[
          "▄▄▖",
          "▌▖▌",
          "▙▄▌",
            ],
        '1':[
          " ▖ ",
          "▝▌ ",
          "▗▙ ",
            ],
        '2':[
          "▗▖ ",
          "▘▞ ",
          "▟▄ ",
            ],
        '3':[
          "▗▖ ",
          "▘▞ ",
          "▚▞ ",
            ],
        '4':[
          " ▗ ",
          "▗▘ ",
          "▀▛ ",
            ],
        '5':[
          "▄▄▖",
          "▙▄ ",
          "▄▄▘",
            ],
        '6':[
          "▗▄ ",
          "▙▄ ",
          "▚▄▘",
            ],
        '7':[
          "▄▄▖",
          " ▞ ",
          "▞  ",
            ],
        '8':[
          "▗▄ ",
          "▚▄▘",
          "▚▄▘",
            ],
        '9':[
          "▗▄ ",
          "▚▄▌",
          "▗▄▘",
            ],
        ':':[
          "   ",
          " ▘ ",
          " ▘ ",
            ],
        ';':[
          "   ",
          " ▘ ",
          "▗▘ ",
            ],
        '<':[
          " ▗▖",
          "▞▘ ",
          "▝▚▖",
            ],
        '=':[
          "   ",
          "▀▀▘",
          "▀▀▘",
            ],
        '>':[
          "▄  ",
          " ▀▖",
          "▄▀ ",
            ],
        '?':[
          " ▖ ",
          " ▞ ",
          " ▖ ",
            ],
        '@':[
          "▗▄ ",
          "▌▙▘",
          "▚▖ ",
            ],
        'A':[
          "▗▄ ",
          "▙▄▌",
          "▌ ▌",
            ],
        'B':[
          "▄▄ ",
          "▙▄▘",
          "▙▄▘",
            ],
        'C':[
          "▗▄▖",
          "▌  ",
          "▚▄▖",
            ],
        'D':[
          "▄▄ ",
          "▌ ▌",
          "▙▄▘",
            ],
        'E':[
          "▄▄▖",
          "▙▄▖",
          "▙▄▖",
            ],
        'F':[
          "▄▄▖",
          "▙▄ ",
          "▌  ",
            ],
        'G':[
          "▄▄▖",
          "▌▗▖",
          "▙▄▌",
            ],
        'H':[
          "▖ ▖",
          "▙▄▌",
          "▌ ▌",
            ],
        'I':[
          "▗▄ ",
          " ▌ ",
          "▗▙ ",
            ],
        'J':[
          " ▄▖",
          " ▐ ",
          "▚▞ ",
            ],
        'K':[
          "▖▗ ",
          "▙▘ ",
          "▌▚ ",
            ],
        'L':[
          "▖  ",
          "▌  ",
          "▙▄▖",
            ],
        'M':[
          "▖ ▖",
          "▛▞▌",
          "▌ ▌",
            ],
        'N':[
          "▖ ▖",
          "▛▖▌",
          "▌▝▌",
            ],
        'O':[
          "▗▄ ",
          "▌ ▌",
          "▚▄▘",
            ],
        'P':[
          "▄▄ ",
          "▙▄▘",
          "▌  ",
            ],
        'Q':[
          "▗▄ ",
          "▌ ▌",
          "▚▞▖",
            ],
        'R':[
          "▄▄ ",
          "▙▄▘",
          "▌▚ ",
            ],
        'S':[
          "▗▄▖",
          "▚▄ ",
          "▄▄▘",
            ],
        'T':[
          "▄▄▖",
          " ▌ ",
          " ▌ ",
            ],
        'U':[
          "▖ ▖",
          "▌ ▌",
          "▚▄▘",
            ],
        'V':[
          "▖ ▖",
          "▌ ▌",
          "▝▞ ",
            ],
        'W':[
          "▖ ▖",
          "▌ ▌",
          "▚▙▘",
            ],
        'X':[
          "▖ ▖",
          "▝▞ ",
          "▞▝▖",
            ],
        'Y':[
          "▖ ▖",
          "▝▞ ",
          " ▌ ",
            ],
        'Z':[
          "▄▄▖",
          " ▞ ",
          "▟▄▖",
            ],
        '[':[
          " ▄ ",
          " ▌ ",
          " ▙ ",
            ],
        '\\':[
          "▖  ",
          "▝▖ ",
          " ▝▖",
            ],
        ']':[
          "▗▖ ",
          " ▌ ",
          "▗▌ ",
            ],
        '^':[
          " ▖ ",
          "▝▝ ",
          "   ",
            ],
        '_':[
          "   ",
          "   ",
          "▄▄▖",
            ],
        '`':[
          "▗  ",
          " ▘ ",
          "   ",
            ],
        'a':[
          "   ",
          "▞▚ ",
          "▚▞▖",
            ],
        'b':[
          "▗  ",
          "▐▀▖",
          "▝▄▘",
            ],
        'c':[
          "   ",
          "▗▀ ",
          "▝▄ ",
            ],
        'd':[
          " ▗ ",
          "▞▜ ",
          "▚▞ ",
            ],
        'e':[
          "   ",
          "▟▙ ",
          "▚▖ ",
            ],
        'f':[
          " ▄ ",
          "▐▖ ",
          "▐  ",
            ],
        'g':[
          " ▄ ",
          "▝▟ ",
          " ▞ ",
            ],
        'h':[
          "▗  ",
          "▐▄ ",
          "▐ ▌",
            ],
        'i':[
          "   ",
          " ▘ ",
          " ▌ ",
            ],
        'j':[
          " ▖ ",
          " ▖ ",
          "▗▘ ",
            ],
        'k':[
          "   ",
          "▐▗ ",
          "▐▚ ",
            ],
        'l':[
          "   ",
          "▐  ",
          "▝▖ ",
            ],
        'm':[
          "   ",
          "▛▞▖",
          "▌ ▌",
            ],
        'n':[
          "   ",
          "▛▚ ",
          "▌▐ ",
            ],
        'o':[
          "   ",
          "▗▀▖",
          "▝▄▘",
            ],
        'p':[
          "   ",
          "▐▚ ",
          "▐▘ ",
            ],
        'q':[
          "   ",
          "▗▜ ",
          " ▜ ",
            ],
        'r':[
          "   ",
          " ▄ ",
          "▐  ",
            ],
        's':[
          "   ",
          "▐▛ ",
          "▗█ ",
            ],
        't':[
          "   ",
          "▗▙ ",
          " ▙ ",
            ],
        'u':[
          "   ",
          "▗▗ ",
          "▐▟ ",
            ],
        'v':[
          "   ",
          "▗▗ ",
          "▝▞ ",
            ],
        'w':[
          "   ",
          "▖ ▖",
          "▚▙▘",
            ],
        'x':[
          "   ",
          "▗▗ ",
          "▗▚ ",
            ],
        'y':[
          "   ",
          "▐▐ ",
          "▗▘ ",
            ],
        'z':[
          "   ",
          "▝█ ",
          "▐▙ ",
            ],
        '~':[
          "   ",
          "▞▖▖",
          " ▝ ",
            ],
    }

    # Calvin S font
    # https://www.texttool.com/ascii-font#p=display&f=Calvin%20S&t=Type%20Something%20%2012345s
    # https://github.com/phpjsnerd/ascii-fonts/blob/master/Calvin%20S.flf
    calvin_s = {
        '!':[
          "┬",
          "│",
          "o"],
        ' ':[
          "  ",
          "  ",
          "  "],
        '#':[
          "─┼─┼─",
          " │ │ ",
          "─┼─┼─"],
        '$':[
          "┌┼┐",
          "└┼┐",
          "└┼┘"],
        '%':[
          "O┬",
          "┌┘",
          "┴O"],
        '&':[
          " ┬ ",
          "┌┼─",
          "└┘ "],
        '*':[
          "\\│/",
          "─ ─",
          "/│\\"],
        ',':[
          " ",
          " ",
          "┘"],
        '-':[
          "   ",
          "───",
          "   "],
        '.':[
          " ",
          " ",
          "o"],
        ':':[
          "o",
          " ",
          "o"],
        ';':[
          "o",
          " ",
          "┘"],
        '?':[
          "┌─┐",
          " ┌┘",
          " o "],
        '@':[
          "┌─┐",
          "│└┘",
          "└──"],
        'A':[
          "╔═╗",
          "╠═╣",
          "╩ ╩"],
        'B':[
          "╔╗ ",
          "╠╩╗",
          "╚═╝"],
        'C':[
          "╔═╗",
          "║  ",
          "╚═╝"],
        'D':[
          "╔╦╗",
          " ║║",
          "═╩╝"],
        'E':[
          "╔═╗",
          "║╣ ",
          "╚═╝"],
        'F':[
          "╔═╗",
          "╠╣ ",
          "╚  "],
        'G':[
          "╔═╗",
          "║ ╦",
          "╚═╝"],
        'H':[
          "╦ ╦",
          "╠═╣",
          "╩ ╩"],
        'I':[
          "╦",
          "║",
          "╩"],
        'J':[
          "╦",
          "║",
          "╚╝"],
        'K':[
          "╦╔═",
          "╠╩╗",
          "╩ ╩"],
        'L':[
          "╦  ",
          "║  ",
          "╩═╝"],
        'M':[
          "╔╦╗",
          "║║║",
          "╩ ╩"],
        'N':[
          "╔╗╔",
          "║║║",
          "╝╚╝"],
        'O':[
          "╔═╗",
          "║ ║",
          "╚═╝"],
        'P':[
          "╔═╗",
          "╠═╝",
          "╩  "],
        'Q':[
          "╔═╗ ",
          "║═╬╗",
          "╚═╝╚"],
        'R':[
          "╦═╗",
          "╠╦╝",
          "╩╚═"],
        'S':[
          "╔═╗",
          "╚═╗",
          "╚═╝"],
        'T':[
          "╔╦╗",
          " ║ ",
          " ╩ "],
        'U':[
          "╦ ╦",
          "║ ║",
          "╚═╝"],
        'V':[
          "╦  ╦",
          "╚╗╔╝",
          " ╚╝ "],
        'W':[
          "╦ ╦",
          "║║║",
          "╚╩╝"],
        'X':[
          "═╗ ╦",
          "╔╩╦╝",
          "╩ ╚═"],
        'Y':[
          "╦ ╦",
          "╚╦╝",
          " ╩ "],
        'Z':[
          "╔═╗",
          "╔═╝",
          "╚═╝"],
        '(':[
          "┌─",
          "│ ",
          "└─"],
        ')':[
          "─┐",
          " │",
          "─┘"],
        '^':[
          "/\\",
          "  ",
          "  "],
        '_':[
          "   ",
          "   ",
          "───"],
        'a':[
          "┌─┐",
          "├─┤",
          "┴ ┴"],
        'b':[
          "┌┐ ",
          "├┴┐",
          "└─┘"],
        'c':[
          "┌─┐",
          "│  ",
          "└─┘"],
        'd':[
          "┌┬┐",
          " ││",
          "─┴┘"],
        'e':[
          "┌─┐",
          "├┤ ",
          "└─┘"],
        'f':[
          "┌─┐",
          "├┤ ",
          "└  "],
        'g':[
          "┌─┐",
          "│ ┬",
          "└─┘"],
        'h':[
          "┬ ┬",
          "├─┤",
          "┴ ┴"],
        'i':[
          "┬",
          "│",
          "┴"],
        'j':[
          " ┬",
          " │",
          "└┘"],
        'k':[
          "┬┌─",
          "├┴┐",
          "┴ ┴"],
        'l':[
          "┬  ",
          "│  ",
          "┴─┘"],
        'm':[
          "┌┬┐",
          "│││",
          "┴ ┴"],
        'n':[
          "┌┐┌",
          "│││",
          "┘└┘"],
        'o':[
          "┌─┐",
          "│ │",
          "└─┘"],
        'p':[
          "┌─┐",
          "├─┘",
          "┴  "],
        'q':[
          "┌─┐ ",
          "│─┼┐",
          "└─┘└"],
        'r':[
          "┬─┐",
          "├┬┘",
          "┴└─"],
        's':[
          "┌─┐",
          "└─┐",
          "└─┘"],
        't':[
          "┌┬┐",
          " │ ",
          " ┴ "],
        'u':[
          "┬ ┬",
          "│ │",
          "└─┘"],
        'v':[
          "┬  ┬",
          "└┐┌┘",
          " └┘ "],
        'w':[
          "┬ ┬",
          "│││",
          "└┴┘"],
        'x':[
          "─┐ ┬",
          "┌┴┬┘",
          "┴ └─"],
        'y':[
          "┬ ┬",
          "└┬┘",
          " ┴ "],
        'z':[
          "┌─┐",
          "┌─┘",
          "└─┘"],
        '0':[
          "▄▄▖",
          "▌▖▌",
          "▙▄▌",
            ],
        '1':[
          " ▖ ",
          "▝▌ ",
          "▗▙ ",
            ],
        '2':[
          "▗▖ ",
          "▘▞ ",
          "▟▄ ",
            ],
        '3':[
          "▗▖ ",
          "▘▞ ",
          "▚▞ ",
            ],
        '4':[
          " ▗ ",
          "▗▘ ",
          "▀▛ ",
            ],
        '5':[
          "▄▄▖",
          "▙▄ ",
          "▄▄▘",
            ],
        '6':[
          "▗▄ ",
          "▙▄ ",
          "▚▄▘",
            ],
        '7':[
          "▄▄▖",
          " ▞ ",
          "▞  ",
            ],
        '8':[
          "▗▄ ",
          "▚▄▘",
          "▚▄▘",
            ],
        '9':[
          "▗▄ ",
          "▚▄▌",
          "▗▄▘",
            ],
          }