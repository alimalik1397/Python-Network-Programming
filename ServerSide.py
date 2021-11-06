#Writing a File Finder Server (FFS) and its corresponding File Finder client (FFC) in Python.

#Server Side Code:
#Implemented by Hassan Rasheed, taken help from stackoverflow.com and bogotobogo.com
#FileFinderServer.py


from socket import*
import os
import json
import datetime
import sys

host='10.3.31.213'
port=12000
filename=''
try:
    server=socket(AF_INET,SOCK_STREAM)
    server.bind((host,port))
    server.listen(5)
    print "Server waiting for client"
    conn, addr = server.accept()  # Establish connection with client.
    print 'Got connection from', addr
except IOError:
    sys.exit(1)
namereceived_time=datetime.time
openLog=open("slog.txt","a+")
openLog.write("Time:"+namereceived_time+":"+"Filename received from client"+":Source IP "+host+":Destination IP "+"10.3.31.213")
openLog.close()
filename = conn.recv(1024)
print('Server received', filename)
print(filename)
os.chdir("d:/")
results = {}
for root, dirs, files in os.walk("d:/"):
    if filename in files:
        results[os.path.join(root, filename)]=str(os.stat(os.path.join(root, filename)).st_size)+" Bytes"
if not results:
    print("There is no file with the given name on this server!")
    conn.send("There is no file with the given name on this server!")
    conn.close()
else:
    for result in results:
        conn.send(json.dumps(result))
        print('Sent ', result)
    print('Done sending file paths')
    conn.send('Waiting for Client to choose the file!')
    pathsent_time=datetime.time
    openLog=open("slog.txt","a+")
    openLog.write("Time:"+pathsent_time+":"+"File paths sent to client"+":Source IP "+"10.3.31.213"+":Destination IP "+host)
    openLog.close()
    filetotransfer=conn.recv(1024)
    print(filetotransfer)
    fileselect_time=datetime.time
    openLog=open("slog.txt","a+")
    openLog.write("Time:"+fileselect_time+":"+"File selected by the client"+":Source IP "+host+":Destination IP "+"10.3.31.213")
    openLog.close()
    fileread = open(filetotransfer, "r")
    data = fileread.read()
    fileread.close()
    conn.send(data)
    print("File sent successfully!")
    conn.send("File sent completely")
    filesent_time=datetime.time
    openLog=open("slog.txt","a+")
    openLog.write("Time:"+filesent_time+":"+"File sent to the client"+":Source IP "+"10.3.31.213"+":Destination IP "+host)
    openLog.close()
    conn.close()
