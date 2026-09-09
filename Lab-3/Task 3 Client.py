import socket

host = "127.0.0.1"
port = 5000

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    msg = input("Enter a message to send: ")
    sock.send(msg.encode())

    sock.close()
    print("Message sent. Connection closed.")

if __name__=="__main__":
    main()