from hashlib import new
import socket
import time
import os

HOST = ''  # The server's hostname or IP address
PORT = 	12345        # The port used by the server

root = os.path.dirname(os.path.abspath(__file__))


def get_ip_address():
    s =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("114.114.114.114",80))
    ipaddr=s.getsockname()[0]
    s.close()
    return ipaddr



def get_old_ip():
    with open(root+'/ip.txt', 'r') as f:
       old_ip = [x.strip() for x in f.read().strip().splitlines() if len(x.strip())]
    return old_ip[0]



def modify_file(new_ip):
    with open(root+'/ip.txt', 'w') as f:
        f.write(new_ip+'\n')
    print('ip changes to %s'%new_ip)



def send_msg(new_ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = 'right+' + new_ip
        s.sendall(msg.encode())



if  __name__ == '__main__' :
    # old_ip = get_old_ip()
    new_ip = get_ip_address()
    print(new_ip)
    send_msg(new_ip)
