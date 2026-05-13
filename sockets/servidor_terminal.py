import socket

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= '127.0.0.1'
port=12345
server_socket.bind((host, port))
server_socket.listen(1)
print("Servidor esperando conexiones en {}:{}".format(host, port))
while True:
    client_socket, addr=server_socket.accept()
    print("Conexión establecida desde: {}".format(addr))

    # data=client_socket.recv(1024).decode()
    # mensaje_rcv="Mensaje recibido: {}".format(data)
    # print(mensaje_rcv)

    # respuesta= "se recibió el mensaje: {}".format(data)
    # client_socket.send(respuesta.encode())
    while True:
        data=client_socket.recv(1024)
        if not data:
            print("Conexión cerrada por el cliente: {}".format(addr))
            client_socket.close()
            break
        mensaje_rcv= data.decode()
        print("Mensaje recibido: {}".format(mensaje_rcv))
        respuesta= "se recibió el mensaje: {}".format(data)
        client_socket.send(respuesta.encode())