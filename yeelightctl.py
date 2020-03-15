import sys
from yeelight import Bulb

if len(sys.argv) != 3:
	print("Not enough parameters given. Please use:")
	print("python yeelightctl.py <bulb_name> <on|off>")
	sys.exit(0)

if sys.argv[1] == "st":
	bulb = Bulb("192.168.178.60")
elif sys.argv[1] == "tv":
	bulb = Bulb("192.168.178.61")
	
if sys.argv[2] == "on":
	try:
		bulb.turn_on()
	except Exception as ex:
		print(ex)
elif sys.argv[2] == "off":
	try:
		bulb.turn_off()
	except Exception as ex:
		print(ex)
