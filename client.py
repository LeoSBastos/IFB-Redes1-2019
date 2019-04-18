import socket

host = "localhost"
port = 7777

while True:
    try:
        message = bytes(input("CLIENT >> "), encoding = 'utf-8')
        if message == "SAIR":
            break
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(message)
            data = s.recv(1024)

        print('SERVER >>', data.decode("utf-8"))
    except:
        print("Conexao recusada")
        break