#!/usr/bin/env python3

import requests

"""
response = requests.get("https://www.google.com")
print(f"\n[+] Status code: {response.status_code}")
print(f"\n[+] Mostrando codigo fuente de la respuesta:\n")

#print(response.text)

with open("index.html", "w") as f:
    f.write(response.text)
"""
"""
values = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

response = requests.get("https://httpbin.org/get", params=values)

print(f"\n[+] URL final: {response.url}\n")
print(response.text)
"""

"""
payload = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
headers = {'User-Agent': 'my-app-agrisem/1.0.0'}

response = requests.post("https://httpbin.org/post", params=payload, headers=headers)

print(response.text)
"""

"""
headers = {'User-Agent': 'Se tensa'}
response = requests.get("https://google.com.mx", headers=headers)
print(response.request.headers)
"""

"""
# request con manejo de exepciones

try:
    response = requests.get('https://google.com.mxx', timeout=1)
    response.raise_for_status()

except requests.Timeout:
    print(f"\n[!] La peticion ha excedido el limite de tiempo de espera")

except requests.HTTPError as http_err:
    print(f"\n[!] Error HTTP: {http_err}")

except requests.RequestException as err:
    print(f"\n[!] Error: {err}")

else:
    print(f"\n[+] No ha habido ningun error en la solicitud")
"""

"""
# Operando con JSON

response = requests.get('https://httpbin.org/get')
data = response.json()

if 'headers' in data and 'User-Agent' in data['headers']:
    user_agent = data['headers']['User-Agent']
    print(f"\n[+] User-Agent: {user_agent}\n")
else:
    print(f"\n[!] No existe este campo en la respuesta\n")
"""

"""
# Usando requests en autenticacion

response = requests.get('https://httpbin.org/basic-auth/foo/bar', auth=('foo', 'bar'))

print(response.status_code)
print(response.text)
"""
"""
# Usando cookies

cookies = dict(cookies_are='working')
response = requests.get('https://httpbin.org/cookies', cookies=cookies)

print(response.text)
"""

"""
# POST de archivos

url = 'https://httpbin.org/post'
my_file = {'archivo': open('example.txt', 'r')}

response = requests.post(url, files=my_file)
print(response.text)
"""

"""
# Estableciendo sesiones de cookies

url = 'https://httpbin.org/cookies'
set_cookies_url = 'http://httpbin.org/cookies/set/my_cookie/123123'

s = requests.Session() # Creamos la sesion de cookies para mantener la autenticacion

response = s.get(set_cookies_url)
response = s.get(url)

print(response.text)
"""

# Preparado de solicitud personalizada

from requests import Request, Session

url = 'https://httpbin.org/get'
s = Session()
headers = {'Custom-Header': 'my_custom_header'}

req = Request('GET', url, headers=headers)

prepped = req.prepare()

prepped.headers['Custom-Header'] = 'my_header_changed'
prepped.headers['Another-Header'] = 'this_is_another_header'
response = s.send(prepped)

print(response.text) 

