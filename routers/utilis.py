import socket
import ssl
import whois
import requests
from urllib.parse import urlparse

def extract_domain(url: str) -> str:
    return urlparse(url).netloc

def get_whois_info(domain: str):
    try:
        w = whois.whois(domain)
        return {
            "domain_name": str(w.domain_name),
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "registrar": str(w.registrar),
            "name_servers": w.name_servers,
        }
    except Exception as e:
        return {"error": str(e)}

def get_ssl_info(domain: str):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(5)
            s.connect((domain, 443))
            cert = s.getpeercert()
            return {
                "issuer": dict(x[0] for x in cert["issuer"]),
                "subject": dict(x[0] for x in cert["subject"]),
                "notBefore": cert["notBefore"],
                "notAfter": cert["notAfter"]
            }
    except Exception as e:
        return {"error": str(e)}

def get_ip_geo(domain: str):
    try:
        ip = socket.gethostbyname(domain)
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        return {
            "ip": ip,
            "country": res.get("country"),
            "region": res.get("regionName"),
            "org": res.get("org"),
            "isp": res.get("isp")
        }
    except Exception as e:
        return {"error": str(e)}

def analyze_url(url: str):
    domain = extract_domain(url)
    return {
        "domain": domain,
        "whois": get_whois_info(domain),
        "ssl": get_ssl_info(domain),
        "ip_geo": get_ip_geo(domain)
    }
