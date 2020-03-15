import sys
import csv
from yeelight import Bulb

if len(sys.argv) != 3:
	print("Not enough parameters given. Please use:")
	print("python yeelightctl.py <bulb_ip> <on|off>")
	sys.exit(0)
	
name_found = False
	
try:
	with open('bulbs.csv', mode='r') as bulbs_csv:
		csv_reader = csv.DictReader(bulbs_csv)
		for row in csv_reader:
			if sys.argv[1] == row["name"]:
				bulb = Bulb(row["ip"])
				name_found = True
except Exception as ex:
	print(ex)

if name_found == False:
	bulb = Bulb(sys.argv[1])

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
