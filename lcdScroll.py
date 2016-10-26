#!/usr/bin/python
"""
lcdScroll.py
Author             :  Eric Pavey 
Creation Date      :  2014-02-08
Blog               :  http://www.akeric.com/blog

Free and open for all to use.  But put credit where credit is due.

OVERVIEW:-----------------------------------------------------------------------
Create scrolling text on a LCD display.  Designed to work on the the 
Adafruit LCD  + keypad, but it's not tied to any specific hardware, and should
work on a LCD of any size.

See lcdScrollTest.py for simple example usage.
"""

class Scroller(object):
    """
    Object designed to auto-scroll text on a LCD screen.  Every time the scroll()
    method is called to, it will scroll the text from right to left by one character
    on any line that is greater than the provided with.
    If the lines ever need to be reset \ updated, call to the setLines() method.
    """
    def __init__(self, lines=[], space = " :: ", width=16, height=2):
        """
        Instance a LCD scroller object.
        
        Parameters:
        lines : list / string : Default empty list : If a list is passed in, each 
            entry in the list is a  string that should be displayed on the LCD, 
            one line after the next.  If a string, it will be split by any embedded 
            linefeed \n characers into a list of multiple lines . 
            Ultimately, the number of entries in this list must be equal to or 
            less than the height argument.
        space : string : Default " :: " : If a given line is longer than the width
            argument, this string will be added to the end to help designate the
            end of the line has been hit during the scroll.
        width : int : Default 16 : The width of the LCD display, number of columns.
        height : int : Default 2 : the height of the LCD, number of rows.
        """
        self.width = width
        self.height = height
        self.space = space
        self.setLines(lines)
                
    def setLines(self, lines):
        """
        Set (for the first time) or reset (at any time) the lines to display.
        Sets self.lines
        
        Parameters:
        lines : list : Each entry in the list is a string
            that should be displayed on the LCD, one line after the next.  The 
            number of entries in this list must be equal to or less than the 
            height argument.
        """
        # Just in case a string is passed in, turn it into a list, and split
        # by any linefeed chars:
        if isinstance(lines, basestring):   
            lines = lines.split("\n")
        elif not isinstance(lines, list):
            raise Exception("Argument passed to lines parameter must be list, instead got: %s"%type(lines))
        if len(lines) > self.height:
            raise Exception("Have more lines to display (%s) than you have lcd rows (%s)"%(len(lines), height))            
        self.lines = lines
        # If the line is over the width, add in the extra spaces to help separate
        # the scroll:
        for i,ln in enumerate(self.lines[:]):
            if len(ln) > self.width:
                self.lines[i] = "%s%s"%(ln,self.space)
        
    def scroll(self):
        """
        Scroll the text by one character from right to left each time this is
        called to.
        
        Return : string : The message to display to the LCD.  Each line is separated
            by the \n (linefeed) character that the Adafruit LCD expects.  Each line
            will also be clipped to self.width, so as to not confuse the LCD when
            later drawn.
        """
        for i,ln in enumerate(self.lines[:]):
            if len(ln) > 16:
                shift = "%s%s"%(ln[1:], ln[0])
                self.lines[i] = shift
        truncated = [ln[:self.width] for ln in self.lines]
        return "\n".join(truncated)         
