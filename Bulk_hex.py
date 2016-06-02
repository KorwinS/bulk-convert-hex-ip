######
# Bulk Hex to IP - v1
# 
# Instructions
# 1. Populate the hex values you want to convert to "input.csv" file in same directory as this file
# 2. Run the script
# 3. Results output to terminal window
######

import socket
import struct
import csv

with open('input.csv') as csvfile:
	hex_converter = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in hex_converter:
		# Convert list to string
		string_hex = str(row)
		# Isolate the hex value from the other junk in AppD Report
		if "IP" in string_hex: 
			int_hex = string_hex[5:13]
		elif "I-" in string_hex:
			int_hex = string_hex[4:12]
		# Exception if it doesn't fit
		else:
			print(string_hex, " not converted, skipping")
			continue
		# Convert the hex string to int, then to IPv4 address 
		addr_long = int(int_hex,16) 
		hex(addr_long)
		ip_addy = socket.inet_ntoa(struct.pack(">L", addr_long))
		# Print the results to terminal
		print(string_hex, " = ", ip_addy)