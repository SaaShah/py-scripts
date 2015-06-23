__author__ = "Saad Bin Shahid"


 # color codes
D  = "\033[0m"; 	 	#	danger
W  = "\033[01;37m";  	#	white
O  = "\033[01;33m"; 	#	yellow
# SUCESS = "\033[01;32m";
FAIL = "\033[01;31m";


# print usage 
def usage():

	print O+ "+----------------------------------------------------------------------------+"
	print "|   GETDNS                                                                   |"
	print "+----------------------------------------------------------------------------+"
	print "|   usage :: python /your/dir/getdns.py hostname.com                         |"
	print "+----------------------------------------------------------------------------+"
	print W+""

import socket
import sys

try: 	
	domain = sys.argv[1]

except IndexError:
	usage()
	domain = raw_input("Enter domain name: ") # www.domain.com
 
try:
    ip = socket.gethostbyname( domain )
 
except socket.gaierror:
    print FAIL+'Invalid Domain' + W
    sys.exit()

print ip
