import socket
import threading as th 
import json 

class Client:
    
    def __init__(self):
        self.s = socket.socket()
        self.s.connect(('localhost',6000))        

        rc = th.Thread(target = self.recevie, daemon = True)
        rc.start()

        self.msg_input()


    def msg_input(self):

        while 1:

            data = input("-> ")

            if data == "exit":
                self.s.close()
                break

            data = json.dumps(data)
            
            self.s.send(bytes(data,"utf-8"))
           


    def recevie(self):

        while 1:

            try:
                data_server = self.s.recv(1024)
                if data_server:
                    print("Mensaje Enviado del servidor: {}".format(json.loads(data_server)))

            except:
                pass

if __name__ == "__main__":

    client = Client()