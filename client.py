import socket
import ssl

# Server'ın IP adresi ve portu
HOST = "127.0.0.1"
PORT = 3131

# SSL sertifikalarının yolunu belirtin
ssl_cert = "server.crt"

# Soketi oluşturun
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_verify_locations(ssl_cert)
client_sock = ssl_context.wrap_socket(client_sock, server_hostname=HOST)

# Server'a bağlanın
client_sock.connect((HOST, PORT))
print("Server'a bağlandı")

# Gelen mesajları okuyun ve gönderin
while True:
    message = input("Mesajınızı girin: ")
    client_sock.send(message.encode())
    data = client_sock.recv(1024)
    if not data:
        break
    print("Server'dan mesaj geldi:", data.decode())

# Bağlantıyı kapatın
client_sock.close()
