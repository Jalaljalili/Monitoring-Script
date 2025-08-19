import socket
import ssl

# TLS versions we want to test
TLS_VERSIONS = {
    "SSLv3": ssl.PROTOCOL_SSLv3 if hasattr(ssl, "PROTOCOL_SSLv3") else None,
    "TLSv1.0": ssl.PROTOCOL_TLSv1,
    "TLSv1.1": ssl.PROTOCOL_TLSv1_1,
    "TLSv1.2": ssl.PROTOCOL_TLSv1_2,
    "TLSv1.3": ssl.PROTOCOL_TLS_CLIENT,  # TLS 1.3 requires PROTOCOL_TLS_CLIENT
}

def check_tls_version(ip, port=443):
    supported = []
    for name, proto in TLS_VERSIONS.items():
        if proto is None:
            continue
        try:
            context = ssl.SSLContext(proto)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            with socket.create_connection((ip, port), timeout=3) as sock:
                with context.wrap_socket(sock, server_hostname=ip) as ssock:
                    # If handshake succeeds, version is supported
                    supported.append(ssock.version())
        except ssl.SSLError:
            continue
        except Exception:
            continue
    return list(set(supported))


def main():
    with open("ip.txt") as f:
        ips = [line.strip() for line in f if line.strip()]

    for ip in ips:
        versions = check_tls_version(ip)
        if versions:
            print(f"{ip}: supports {', '.join(versions)}")
        else:
            print(f"{ip}: no TLS versions detected (maybe not HTTPS?)")


if __name__ == "__main__":
    main()
