from machine import I2C, Pin
from oledmenu import *

print("OLED Menu Test")
print("Press Ctrl + C to exit")

# Initialize I2C for the OLED display
i2c = I2C(1, sda=Pin(10), scl=Pin(11), freq=400000)

menu = OLED_MENU( i2c );

# code, Label
menu.add_label( "start", "Start Oven" )
menu.add_label( "t1", "test1" ) # code, Label
menu.add_label( "t2", "test2" ) # code, Label
menu.add_combo( "combo4", "Mode: %s", [("v1", "value 1"),("v2", "value 2"),("v3", "value 3"),("v4", "value 4"),("v5", "value 5"),("v6", "value 6"),("v7", "value 7"),("v8", "value 8")], "v8" ) # code, Label
menu.add_label( "t3", "test3" ) # code, Label
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

		if entry and entry.code=="combo4":
			print( "Combo selection is '%s' " % menu.by_code("combo4").cargo.value )
			print( "  +-> with label '%s'" % menu.by_code("combo4").cargo.label )
	# Process other tasks here
