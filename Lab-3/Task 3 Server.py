import socket

host = "127.0.0.1"
port = 5000

def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((host, port))
    srv.listen(1)
    print(f"Server listening on {host}:{port}...")

    connection, address = srv.accept()
    print(f"Connected by {address}")

    msg = connection.recv(1024).decode()
    print(f"Received message: {msg}")

    connection.close()
    srv.close()

if __name__=="__main__":
    main()