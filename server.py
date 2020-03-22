import socket
import json
import data
import hashlib

def main():
    IP = "127.0.0.1"
    PORT = 8080
    cl_dict = {"mode" : 200 , "data" : "this is just test !"}
    connect = True
    lis_sok = socket.socket()
    lis_sok.bind(('' , PORT))

    while True:
        try:
            lis_sok.listen(1)
            cl_sok , cl_addr = lis_sok.accept()
            connect = 1
            cl_dict["mode"] = 200
            cl_sok.sendall("Enter password please : ".encode())
            PASS = cl_sok.recv(1024).decode()
            #checking if recived password is the password
            if (check_pass(PASS) == False):
                cl_sok.sendall("wrong password ! (restart the program and try again)".encode())
                connect = False
                cl_sok.close()
            else:
                cl_sok.sendall("correct password !".encode())
            while connect:
                cl_dict["data"] = ""
                cl_dict["mode"] = 200
                #sending menu
                cl_sok.sendall("welcome to the server! ,  \n1- list of albums.\n2 - songs in album.\n3 - length of song.\n4 - lyrics of song\n5 - album of song.\n6 - word in songs name.\n7 - word in song lyrics.\n8 - exit.\nEnter option: ".encode())
                cl_msg = cl_sok.recv(1024)
                #decoding dict using json
                cl_msg_json = json.loads(cl_msg.decode("utf-8"))
                mode = cl_msg_json["mode"]
                #checking if mode is illigle
                if mode > 208 or mode < 201:
                    cl_dict["mode"] = 201
                else:
                    cl_dict["data"] = get_ans(mode , cl_msg_json["data"])
                if mode == 208:
                    connect = False
                #encoding dict using json
                cl_sok.sendall(json.dumps(cl_dict).encode("utf-8"))
        except Exception as e:
            print("conection closed by client")

def get_ans(mode , data_s ):
    """
    func getting the relvant data the user asked for
    :param option (mode):
    :param song album word or whatever (data_s)
    :return: the asked data
    """
    if mode == 201:
        return  data.get_all_albums()
    elif mode == 202:
        return data.get_album_songs(data_s)
    elif mode == 203:
        return data.get_song_len(data_s)
    elif mode == 204:
        return  data.get_song_lyrics(data_s)
    elif mode == 205:
        return  data.get_song_album(data_s)
    elif mode == 206:
        return data.get_song_word(data_s)
    elif mode == 207:
        return data.get_lyrics_word(data_s)
    elif mode == 208:
        return "bye bye"

def check_pass (password):
    """
    func checking if given password equal to saved password (using hash and md5 encryption
    :param given password:
    :return: true \ false
    """
    if (hashlib.md5(password.encode()).hexdigest() == "dffb14c19bcd777a089b94add3deb885"):
        return True
    return False


if __name__ == '__main__':
    main()















