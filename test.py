from machine import I2C, Pin
from oledmenu import *

# Initialize I2C for the OLED display
i2c = I2C(1, sda=Pin(10), scl=Pin(11), freq=400000)

menu = OLED_MENU( i2c );

# code, Label
menu.add_label( "start", "Start Oven" )
menu.add_label( "stop" , "Stop Oven" , enabled=False )
menu.add_range( "preheat" , "PreHeat %s C", 25, 180, 5, 50 ) # Min, Max, Step, default
menu.add_label( "t1", "test1" ) # code, Label
menu.add_label( "t2", "test2" ) # code, Label
menu.add_label( "t3", "test3" ) # code, Label
menu.add_label( "t4", "test4" ) # code, Label
menu.add_label( "t5", "test5" ) # code, Label
menu.add_label( "t6", "test6" ) # code, Label
menu.add_label( "t7", "test7" ) # code, Label
menu.add_label( "t8", "test8" ) # code, Label

menu.start()

while True:
	if menu.update(): # true when entry selected
		entry = menu.selected # will reset selection
		if entry:
			print( "%s selected" % entry )

		if entry and entry.code=="t3":
			menu.by_code("stop").enabled=True
	# Process other tasks here
