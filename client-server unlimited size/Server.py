from socket import *

# server-side
try:
    s = socket(AF_INET, SOCK_STREAM)
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 7002  # Port to listen on (non-privileged ports are > 1023)

    s.bind((HOST, PORT))
    s.listen()
    c, addr = s.accept()
    print("accepted by", addr)
    HEADER_LENGTH = 4  # Assuming 4 bytes for message length

    while True:
        # Receive message length
        message_length = int.from_bytes(c.recv(HEADER_LENGTH), byteorder="big")

        # Receive message data
        data = b''
        received = 0
        while received < message_length:
            chunk = c.recv(4096)
            received += len(chunk)
            data += chunk

        message = data.decode('utf-8')
        print("client:", message)

        # Send response (example)
        response = input("server:")
        response_length = len(response.encode('utf-8'))
        c.sendall(response_length.to_bytes(HEADER_LENGTH, byteorder="big"))
        c.sendall(response.encode('utf-8'))

except error as e:
    print(e)

except KeyboardInterrupt:
    print("chat is terminated")