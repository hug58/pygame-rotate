import socket

def main():
    s = socket.socket()
    s.connect(("localhost",6000))
    #s.setblocking(False)

    while True:

        data = input(">")
        s.send(bytes(data,"utf-8"))

        if data == "exit": break
        data_server = s.recv(1024)
        if data_server:print(f"Mensaje Enviado del servidor: {data_server.decode('utf-8')}")
            


    s.close()

if __name__ == "__main__":
    main()