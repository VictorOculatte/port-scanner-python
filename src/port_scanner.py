import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            return True
        else:
            return False
    except:
        return False

def main():
    target = input("Digite o IP ou domínio para scan: ")
    print(f"⟦ Port Scanner Iniciado em: {target} ⟧")

    ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389]

    for port in ports:
        if scan_port(target, port):
            print(f"[+] Porta {port} está aberta")
        else:
            print(f"[-] Porta {port} fechada")

if __name__ == "__main__":
    main()
input("\nPressione ENTER para sair...")
