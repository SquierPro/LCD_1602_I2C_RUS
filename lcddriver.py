import i2c_lib
from time import *

# LCD Address
ADDRESS = 0x3f

# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

En = 0b00000100 # Enable bit
Rw = 0b00000010 # Read/Write bit
Rs = 0b00000001 # Register select bit
#RUS

letters=[65,
[0b11111,0b10000,0b10000,0b11110,0b10001,0b10001,0b11110,0b00000],
66,
[0b11111,0b10000,0b10000,0b10000,0b10000,0b10000,0b10000,0b00000],
[0b00110,0b01010,0b01010,0b01010,0b01010,0b01010,0b11111,0b10001],
69,
[0b10101,0b10101,0b10101,0b01110,0b10101,0b10101,0b10101,0b00000],
[0b01110,0b10001,0b00001,0b00110,0b00001,0b10001,0b01110,0b00000],
[0b10001,0b10001,0b10001,0b10011,0b10101,0b11001,0b10001,0b00000],
[0b10101,0b10001,0b10001,0b10011,0b10101,0b11001,0b10001,0b00000],
75,
[0b00111,0b01001,0b01001,0b01001,0b01001,0b01001,0b10001,0b00000],
77,
72,
79,
[0b11111,0b10001,0b10001,0b10001,0b10001,0b10001,0b10001,0b00000],
80,
67,
84,
[0b10001,0b10001,0b10001,0b01111,0b00001,0b10001,0b01110,0b00000],
[0b00100,0b01110,0b10101,0b10101,0b10101,0b01110,0b00100,0b00000],
88,
[0b10010,0b10010,0b10010,0b10010,0b10010,0b10010,0b11111,0b00001],
[0b10001,0b10001,0b10001,0b01111,0b00001,0b00001,0b00001,0b00000],
[0b10001,0b10001,0b10001,0b10101,0b10101,0b10101,0b11111,0b00000],
[0b10001,0b10001,0b10001,0b10101,0b10101,0b10101,0b11111,0b00001],
[0b11000,0b01000,0b01000,0b01110,0b01001,0b01001,0b01110,0b00000],
[0b10001,0b10001,0b10001,0b11101,0b10011,0b10011,0b11101,0b00000],
[0b10000,0b10000,0b10000,0b11110,0b10001,0b10001,0b11110,0b00000],
[0b01110,0b10001,0b00001,0b00111,0b00001,0b10001,0b01110,0b00000],
[0b10010,0b10101,0b10101,0b11101,0b10101,0b10101,0b10010,0b00000],
[0b01111,0b10001,0b10001,0b01111,0b00101,0b01001,0b10001,0b00000],
97,
[0b00011,0b01100,0b10000,0b11110,0b10001,0b10001,0b01110,0b00000],
[0b00000,0b00000,0b11110,0b10001,0b11110,0b10001,0b11110,0b00000],
[0b00000,0b00000,0b11110,0b10000,0b10000,0b10000,0b10000,0b00000],
[0b00000,0b00000,0b00110,0b01010,0b01010,0b01010,0b11111,0b10001],
101,
[0b00000,0b00000,0b10101,0b10101,0b01110,0b10101,0b10101,0b00000],
[0b00000,0b00000,0b01110,0b10001,0b00110,0b10001,0b01110,0b00000],
[0b00000,0b00000,0b10001,0b10011,0b10101,0b11001,0b10001,0b00000],
[0b01010,0b00100,0b10001,0b10011,0b10101,0b11001,0b10001,0b00000],
[0b00000,0b00000,0b10010,0b10100,0b11000,0b10100,0b10010,0b00000],
[0b00000,0b00000,0b00111,0b01001,0b01001,0b01001,0b10001,0b00000],
[0b00000,0b00000,0b10001,0b11011,0b10101,0b10001,0b10001,0b00000],
[0b00000,0b00000,0b10001,0b10001,0b11111,0b10001,0b10001,0b00000],
111,
[0b00000,0b00000,0b11111,0b10001,0b10001,0b10001,0b10001,0b00000],
112,
99,
[0b00000,0b00000,0b11111,0b00100,0b00100,0b00100,0b00100,0b00000],
121,
[0b00000,0b00000,0b00100,0b01110,0b10101,0b01110,0b00100,0b00000],
120,
[0b00000,0b00000,0b10010,0b10010,0b10010,0b10010,0b11111,0b00001],
[0b00000,0b00000,0b10001,0b10001,0b01111,0b00001,0b00001,0b00000],
[0b00000,0b00000,0b10101,0b10101,0b10101,0b10101,0b11111,0b00000],
[0b00000,0b00000,0b10101,0b10101,0b10101,0b10101,0b11111,0b00001],
[0b00000,0b00000,0b11000,0b01000,0b01110,0b01001,0b01110,0b00000],
[0b00000,0b00000,0b10001,0b10001,0b11101,0b10011,0b11101,0b00000],
[0b00000,0b00000,0b10000,0b10000,0b11110,0b10001,0b11110,0b00000],
[0b00000,0b00000,0b01110,0b10001,0b00111,0b10001,0b01110,0b00000],
[0b00000,0b00000,0b10010,0b10101,0b11101,0b10101,0b10010,0b00000],
[0b00000,0b00000,0b01111,0b10001,0b01111,0b00101,0b01001,0b00000]]

rus=[]


class lcd:
   #initializes objects and lcd
   def __init__(self):
      self.lcd_device = i2c_lib.i2c_device(ADDRESS)

      self.lcd_write(0x03)
      self.lcd_write(0x03)
      self.lcd_write(0x03)
      self.lcd_write(0x02)

      self.lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
      self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
      self.lcd_write(LCD_CLEARDISPLAY)
      self.lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
      sleep(0.2)

   # clocks EN to latch command
   def lcd_strobe(self, data):
      self.lcd_device.write_cmd(data | En | LCD_BACKLIGHT)
      sleep(.0005)
      self.lcd_device.write_cmd(((data & ~En) | LCD_BACKLIGHT))
      sleep(.0001)

   def lcd_write_four_bits(self, data):
      self.lcd_device.write_cmd(data | LCD_BACKLIGHT)
      self.lcd_strobe(data)

   # write a command to lcd
   def lcd_write(self, cmd, mode=0):
      self.lcd_write_four_bits(mode | (cmd & 0xF0))
      self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))

   # put string function
   def lcd_display_string(self, string, line):

      mass=[]
      for char in string:
         sym=ord(char)
         if sym >= 1040 and sym <= 1103:
             sym=self.rus_char(sym)
         mass.append(sym)

      if line == 1:
         self.lcd_write(0x80)
      if line == 2:
         self.lcd_write(0xC0)
      if line == 3:
         self.lcd_write(0x94)
      if line == 4:
         self.lcd_write(0xD4)

      for char in mass: 
         self.lcd_write(char, Rs)
   # clear lcd and set to home
   def lcd_clear(self):
      self.lcd_write(LCD_CLEARDISPLAY)
      self.lcd_write(LCD_RETURNHOME)
      del rus[:]

   def rus_char(self, char):
      num=char-1040
      if type(letters[num]) == int:
          sym=letters[num]
      else:
          if rus.count(char):
              sym=rus.index(char)
          else:
              if len(rus)<8:
                  self.lcd_write(LCD_SETCGRAMADDR+len(rus)*8)
                  for i in range(8):
                      self.lcd_write(letters[num][i],True)
                  sym=len(rus)
                  rus.append(char)
              else:
                  sym=255
      return sym
