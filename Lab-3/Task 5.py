import socket

def lookup(p, proto):
    try:
        return socket.getservbyport(p, proto)
    except OSError:
        return "unknown"

def main():
    port_list = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]

    print(f"{'Port':<8}{'TCP Service':<20}{'UDP Service':<20}")
    print("-"*48)

    for p in port_list:
        tcp = lookup(p, "tcp")
        udp = lookup(p, "udp")
        print(f"{p:<8}{tcp:<20}{udp:<20}")

if __name__=="__main__":
    main()