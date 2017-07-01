#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import lcddriver
from time import *

lcd = lcddriver.lcd()

lcd.lcd_clear();
lcd.lcd_display_string(u"абвгдежз", 1)
sleep(3)
lcd.lcd_display_string(u"АБВГДЖЗ", 2)

#sleep(3)
#lcd.lcd_clear();
#lcd.lcd_display_string(u"ийклмноп", 1)
#lcd.lcd_display_string(u"ИЙКЛМНОП", 2)


