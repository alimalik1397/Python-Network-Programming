
#Writing a File Finder Server (FFS) and its corresponding File Finder client (FFC) in Python.
#Client Side Code:


from socket import *
import datetime
import sys
import json

server_host = "10.3.31.213"
server_port = 12000
clientIP = "10.3.31.202"
files = raw_input('Enter file name with extension:')
host_port = "%s:%s" % (server_host, server_port)
try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_host, int(server_port)))
    client_socket.send(files)
    namesent_time = datetime.time
    openLog = open("clog.txt", "a+")
    openLog.write("Time:" + namesent_time + ":" + "Filename received from client" + ":Source IP " + clientIP + ":Destination IP " + server_host)
    openLog.close()
except IOError:
    sys.exit(1)
data = ""
while True:
    print(client_socket.recv(1024))
pathreceived_time=datetime.time
openLog=open("clog.txt","a+")
openLog.write("Time:"+pathreceived_time+":"+"File paths sent to client"+":Source IP "+server_host+":Destination IP "+clientIP)
openLog.close()
filetoreceive = raw_input("Enter complete path of the file to receive! Enter double backslashes as a single forward slash")
client_socket.send(filetoreceive)
fileselect_time = datetime.time
openLog = open("clog.txt", "a+")
openLog.write("Time:" + fileselect_time + ":" + "File selected by the client" + ":Source IP " + clientIP + ":Destination IP " + server_host)
openLog.close()
while rmsg:
    rmsg = client_socket.recv(json.loads(1024))
    data += rmsg
client_socket.close()
filereceived_time = datetime.time
openLog = open("clog.txt", "a+")
openLog.write("Time:" + filereceived_time + ":" + "File received by the client" + ":Source IP " + server_host + ":Destination IP " + clientIP)
openLog.close()
print "\nClient IP: ", clientIP
print "\ndata:", data
file = open("file_found.txt", "w")
file.write(data)
file.close()

