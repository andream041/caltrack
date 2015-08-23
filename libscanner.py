import os

import pandas as pd
import psycopg2
import numpy as np
import evdev as ev

# Provided as an example taken from my own keyboard attached to a Centos 6 box:
scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
}

scanpath = '/dev/input/barcode'

devices = [ev.InputDevice(fn) for fn in ev.list_devices()]
#print(ev.list_devices())
#for dev in devices:
    #print(dev.fn, dev.name, dev.phys)

scandev = ev.InputDevice(scanpath)
scandev.grab()

#print(scandev)
#print(scandev.capabilities(verbose=True))
#print(ev.events.event_factory)

barcodes = []
barcode = []
oldval = ''
for event in scandev.read_loop():
    if event.type == ev.ecodes.EV_KEY:
        #print(ev.categorize(event))

        data = ev.categorize(event)  
        scancode = data.scancode
        value = ev.ecodes.KEY[scancode].replace('KEY_','')
        print(repr(value))
        #if value != u'ENTER' or value != u'DOWN':
        if len(value) == 1:
            barcode.append(value)
        elif len(value) >1: 
            if barcode:
                #print(barcode) 
                fullbarcode = ''.join(barcode)[::2]
                barcodes.append(fullbarcode)
                barcode = []

    if barcodes:
        print(barcodes)

        #if value == 'ENTER' and oldval != 'ENTER':
            #barcodes.append(fullbarcode)
            #continue


        #if value == 'DOWN' and oldval == 'DOWN':
            #barcode=[]

        #if barcode:
            #fullbarcode = ''.join(barcode[::2])
            ##print(fullbarcode)
            #oldval = value

    #print(barcodes)
    #print(len(barcode))
    #print(event.code)
    #print(scancodes[event.code])
    #if data.keystate == 1:  # Down events only
        #key_lookup = scancodes.get(data.scancode) or u'UNKNOWN:{}'.format(data.scancode)  
        #print(u'You Pressed the {} key!'.format(key_lookup))



    #print(event.value)
    #print(str(chr(event.value)))

#dev = ev.InputDevice('/dev/input/event1')
#print(dev)

#from evdev import UInput, AbsInfo, ecodes as e

#cap = {
     #e.EV_KEY : [e.KEY_A, e.KEY_B],
     #e.EV_ABS : [
         #(e.ABS_X, AbsInfo(value=0, min=0, max=255,
                           #fuzz=0, flat=0, resolution=0)),
         #(e.ABS_Y, AbsInfo(0, 0, 255, 0, 0, 0)),
         #(e.ABS_MT_POSITION_X, (0, 255, 128, 0)) ]
#}

#ui = UInput(cap, name='example-device', version=0x3)
#print(ui)

#print(ui.capabilities())

 ## move mouse cursor
#ui.write(e.EV_ABS, e.ABS_X, 20)
#ui.write(e.EV_ABS, e.ABS_Y, 20)
#ui.syn()
