import socket
import ssl

# Server'ın dinleyeceği IP adresi ve portu
HOST = "127.0.0.1"
PORT = 3131

# SSL sertifikalarının yolunu belirtin
ssl_cert = "server.crt"
ssl_key = "server.key"

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(ssl_cert, ssl_key)
server_sock = ssl_context.wrap_socket(server_sock, server_side=True)

# Server'ı bağlantı isteklerini dinlemeye hazır hale getirin
server_sock.bind((HOST, PORT))
server_sock.listen()
print("Server başlatıldı ve dinlemeye hazır")

# Client ile bağlantı kurun
client_sock, client_addr = server_sock.accept()
print("Client bağlandı:", client_addr)

# Gelen mesajları okuyun ve gönderin
while True:
    data = client_sock.recv(1024)
    if not data:
        break
    print("Client'dan mesaj geldi:", data.decode())
    message = input("Mesajınızı girin: ")
    client_sock.send(message.encode())

# Bağlantıyı kapatın
client_sock.close()
server_sock.close()
