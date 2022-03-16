import socket
import os
import time

HOST = ''  
PORT = 12345

def build_socket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        c, addr = s.accept()
        print('Got connection from', addr)
        data = c.recv(1024)
        rec_msg = data.decode()
        if len(rec_msg.split('+')) == 2:
            name, rec_ip = rec_msg.split('+')
            if len(rec_ip.split('.')) == 4:
                change_ip(rec_ip, name)
        # c.sendall(data)
        c.close()

def change_ip(new_ip, name):
    if name == 'right':
        pos = 253
    elif name == 'left':
        pos = 249
    print('save %s to /var/www/html/index.html'%new_ip)
    cmd = 'sed -i \'%dc %s\' /var/www/html/index.html'%(pos, new_ip)
    os.system(cmd)



if  __name__ == '__main__' :
    socket.setdefaulttimeout(120)
    build_socket()