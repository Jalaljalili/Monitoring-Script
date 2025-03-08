import requests
import socket
import concurrent.futures
import xlsxwriter

def is_url_up(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code < 400
    except requests.RequestException:
        return False

def scan_ports(host, ports=range(1, 65536)):
    open_ports = []
    
    def check_port(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            if sock.connect_ex((host, port)) == 0:
                open_ports.append(port)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(check_port, ports)
    
    return open_ports

def main(file_path, output_file):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines() if line.strip()]
    
    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, ["URL", "Status", "Open Ports"])
    
    row = 1
    for url in urls:
        print(f"Checking {url}...")
        status = "UP" if is_url_up(url) else "DOWN"
        open_ports = "N/A"
        
        if status == "UP":
            hostname = url.split('//')[-1].split('/')[0]
            ports = scan_ports(hostname)
            open_ports = ", ".join(map(str, ports)) if ports else "None"
        
        worksheet.write_row(row, 0, [url, status, open_ports])
        row += 1
    
    workbook.close()
    print(f"Results saved in {output_file}")

if __name__ == "__main__":
    file_path = "urls.txt"  # Change this to your file path
    output_file = "scan_results.xlsx"
    main(file_path, output_file)
