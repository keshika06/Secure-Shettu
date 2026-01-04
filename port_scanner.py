import socket
target = "localhost"



for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        try:
            service = socket.getservicebyport(port)
        except:
            service = "Unknown service"
        
        print(f"Port {port} is OPEN → Service: {service}")

    s.close()
print("Fast scanning ports 1 to 1024...\n")

threads = []

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
