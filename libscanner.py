import os
import pandas as pd
import psycopg2
import numpy as np
import evdev as ev
import datetime

conn = psycopg2.connect("dbname=caltrack user=andrea")
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
    curtime = datetime.datetime.now().isoformat()
    if event.type == ev.ecodes.EV_KEY:
        #print(ev.categorize(event))

        data = ev.categorize(event)  
        scancode = data.scancode
        value = ev.ecodes.KEY[scancode].replace('KEY_','')
        #print(repr(value))
        #if value != u'ENTER' or value != u'DOWN':
        if len(value) == 1:
            barcode.append(value)
        elif len(value) >1: 
            if barcode:
                #print(barcode) 
                fullbarcode = ''.join(barcode)[::2]
                print(curtime, fullbarcode)
                # Before used the barcodes list to display barcodes.
                #barcodes.append(fullbarcode)

                cur = conn.cursor()
                cmd =   "INSERT INTO scantest (time, barcode) VALUES \
                        ('{0}', {1}) \
                        ;".format(curtime, fullbarcode)
                cur.execute(cmd)
                conn.commit()
                cur.close()

                barcode = []


    #if barcodes:
        #print(barcodes)

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
