import socket
import _thread

host = "localhost"
port = 7777
s = socket.socket()
s.bind((host,port))
s.listen(5)

def operacoes(data):
    lst = data.split(" ")
    if len(lst) > 1:
        if(lst[1] == '+'):
            val = float(lst[0])+float(lst[2])
        elif(lst[1] == '-'):
            val = float(lst[0])-float(lst[2])
        elif(lst[1] == '*'):
            val = float(lst[0])*float(lst[2])
        elif(lst[1] == '/'):
            val = float(lst[0])/float(lst[2])
        else:
            val = "Mensagem nao reconhecivel ou formatada errada"
    else:
        val = "Mensagem nao reconhecivel ou formatada errada"
    return val

def connection(conn, addr):
    with conn:
        print('Conectado com o endereco:', addr)
        while True:
            data = conn.recv(1024)
            val = operacoes(data.decode("utf-8"))
            if not data:
                break
            conn.sendall(bytes(str(val), encoding = "utf-8"))

while True:
    conn, addr = s.accept()
    _thread.start_new_thread(connection,(conn,addr))

s.close()
