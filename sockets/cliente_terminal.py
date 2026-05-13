import socket

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= '127.0.0.1'
port=12345
client_socket.connect((host, port))
print("Conectado al servidor en {}:{}".format(host, port))

mensaje= "Hola, servidor!"
client_socket.send(mensaje.encode())
while True:
    data=client_socket.recv(1024)
    if not data:
        print("Conexión cerrada por el servidor")
        client_socket.close()
        break
    mensaje_rcv= data.decode()
    print("Mensaje recibido: {}".format(mensaje_rcv))