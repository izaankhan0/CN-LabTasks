import socket

host = "127.0.0.1"
port = 5001

def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((host, port))
    srv.listen(1)
    print(f"Server listening on {host}:{port}...")

    connection, address = srv.accept()
    print(f"Connected by {address}")

    raw = connection.recv(1024).decode()
    sid, sname, dept = raw.split("|")

    print("\n--- Student Information Received ---")
    print(f"Student ID: {sid}")
    print(f"Name: {sname}")
    print(f"Department: {dept}")

    connection.send("Acknowledged: Student information received successfully.".encode())
    connection.close()
    srv.close()

if __name__=="__main__":
    main()