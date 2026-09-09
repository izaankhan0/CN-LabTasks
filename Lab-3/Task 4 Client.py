import socket

host = "127.0.0.1"
port = 5001

def main():
    sid = input("Enter Student ID: ")
    sname = input("Enter Student Name: ")
    dept = input("Enter Department: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    payload = f"{sid}|{sname}|{dept}"
    sock.send(payload.encode())

    response = sock.recv(1024).decode()
    print(f"\nServer response: {response}")
    sock.close()

if __name__=="__main__":
    main()