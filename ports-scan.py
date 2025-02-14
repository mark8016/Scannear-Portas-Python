import socket

def scan_ports(target):
    print(f"Escaneando portas abertas em {target}...\n")
    
    # Lista de portas comuns
    ports = [22, 80, 443, 8080, 53, 25, 21]
    
    # Loop sobre as portas
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        # Tentando conectar
        result = sock.connect_ex((target, port))
        
        # Se conectar com sucesso
        if result == 0:
            print(f"Porta {port} aberta.")
        sock.close()

# Alvo pode ser um IP ou domínio
target = "127.0.0.1"  # Coloque o IP ou domínio do alvo aqui
scan_ports(target)
