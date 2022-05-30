import socket
target_host = "127.0.0.1"
target_port = 80
# crear un objeto de enchufe
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# enviar algunos datos
client.sendto("AAABBBCCC",(target_host,target_port))
# recibe algunos datos
data, addr = client.recvfrom(4096)
print (data)