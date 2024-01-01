import socket

HOST = "127.0.0.1"
PORT = 65123

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
    listener.bind((HOST, PORT))
    listener.listen(1)
    print("Se estan esperando conexiones...")
    conn, adrr = listener.accept()

    with conn:
        print(f"Se logro conectar con {adrr}")
        while True:
            data = input("shell@shell: ")
            conn.sendall(data.encode('ascii'))
            result = conn.recv(1024)
            if not result:
                print("No se recibio ningun dato, quizas el comando no fue aceptado")
                break
            else:
                print(result.decode('utf-8', errors='ignore'))
