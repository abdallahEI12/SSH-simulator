import socket
import sys



def create_socket():
    try:
        global host
        global port 
        global s
        host = ""
        port = 9999    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("socket couldn't be created" + str(msg))

#bind socket and listen to connections

def bind_socket():
    try:
        global host
        global port
        global s
        print(f"binding port {port}")
        
        s.bind((host,port))
        s.listen(5)
        
    except socket.error as msg:
        print("socket binding error{msg} \n retrying....")
        bind_socket()

#establish connection with a client {socket must be listening}

def socket_accept():
    
    connection,List = s.accept()
    print(f"we are connected | IP => {List[0]} | port => {List[1]}")
    send_commands(connection)
    
#send things to the client
def send_commands(connection):
    while True:
        
        cmd = input()
        
        if cmd == "end":
            connection.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) >0:
            connection.send(str.encode(cmd))
            response = str(connection.recv(1024) , "utf-8")
            print(response, end = "\n")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()