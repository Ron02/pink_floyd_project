import socket
import json
def main():
    IP = "127.0.0.1"
    PORT = 8080
    data = ""
    cl_sok = socket.socket()
    cl_sok.connect((IP , PORT))
    msg = {"mode" : 0 , "data" : ""}
    mode = 0
    cl_sok.sendall(input(cl_sok.recv(1024).decode()).encode())
    print(cl_sok.recv(1024).decode())
    while mode != 8:
        keep_try = True
        welcome_msg = cl_sok.recv(1024)
        #scaning the option user choose and checks it
        while keep_try:
            try:
                mode = int(input(welcome_msg.decode()))
                if (type(mode) == int):
                    keep_try = False
            except Exception as e:
                print ("illgle input...")
        if mode != 1 and mode != 8:
            while 1:
                data = input("enter the song\\album\word etc...")
                if data.replace(" " , "").isalpha():
                    break
        msg["mode"] = 200 + mode
        msg["data"] = data
        #encode and send dict using json
        json_data = json.dumps(msg).encode("utf-8")
        cl_sok.sendall(json_data)
        serv_msg = cl_sok.recv(2000)
        #decode dict sent using json
        serv_msg_json = json.loads(serv_msg.decode("utf-8"))
        if serv_msg_json["mode"] == 200:
            print(serv_msg_json["data"])
        else:
            print("data is unreachable...")

    cl_sok.close()

if __name__ == '__main__':
    main()



