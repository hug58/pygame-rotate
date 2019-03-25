import socket
import threading as th


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("localhost",6000))
s.listen(2)


def main(conn,addr):
    
    #s.setblocking(False)
    
    print( f"Conexión establecida con: {addr}")

    while True:

        data = conn.recv(1024)
        if data:
            print("")
            data = data.decode("utf-8")
            print(data)
            print( f"Reevio del msj al cliente: {addr}")
            conn.sendall(bytes(data,"utf-8"))
            print(bytes(data,"utf-8"))
            if data == "exit":
                break

    s.close()

if __name__ == "__main__":
    while 1:
        conn,addr = s.accept()
        th.Thread(target = main, args = (conn,addr)).start()