import requests
import socket
import concurrent.futures

def is_url_up(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code < 400
    except requests.RequestException:
        return False

def scan_ports(host, ports=[80, 443, 22, 21, 3306, 8080, 8443]):
    open_ports = []
    def check_port(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((host, port)) == 0:
                open_ports.append(port)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(check_port, ports)
    
    return open_ports

def main(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines() if line.strip()]
    
    for url in urls:
        print(f"Checking {url}...")
        if is_url_up(url):
            print(f"  {url} is UP")
            hostname = url.split('//')[-1].split('/')[0]
            open_ports = scan_ports(hostname)
            if open_ports:
                print(f"  Open ports: {', '.join(map(str, open_ports))}")
            else:
                print("  No common open ports found")
        else:
            print(f"  {url} is DOWN")

if __name__ == "__main__":
    file_path = "urls.txt"  # Change this to your file path
    main(file_path)