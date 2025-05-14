import urllib3
import json

"""
http = urllib3.PoolManager() # Controlador de conexiones

response = http.request('GET', 'https://httpbin.org/get')
print(response.data.decode())
"""

"""
http = urllib3.PoolManager() # Controlador de conexiones

response = http.request('POST', 'https://httpbin.org/post')
print(response.data.decode())
"""

"""
http = urllib3.PoolManager() # Controlador de conexiones

data = "Esto es una prueba"
encoded_data = data.encode()

response = http.request('POST', 'https://httpbin.org/post', body=encoded_data)
print(response.data.decode())
"""

"""
http = urllib3.PoolManager() # Controlador de conexiones

data = {'atributo': 'valor'}
encoded_data = json.dumps(data).encode()

response = http.request('POST', 'https://httpbin.org/post', body=encoded_data)
print(response.data.decode())
"""
"""
http = urllib3.PoolManager() # Controlador de conexiones

response = http.request('POST', 'https://httpbin.org/post', fields={'atributo': 'valor'})
print(response.data.decode())

"""
"""
http = urllib3.PoolManager() # Controlador de conexiones

data = {'atributo': 'valor'}
encoded_data = json.dumps(data).encode()

response = http.request('POST', 'https://httpbin.org/post', body=encoded_data, headers={'Content-Type': 'application/json'})
print(response.data.decode())
"""
"""
http = urllib3.PoolManager() # Controlador de conexiones


response = http.request('GET', 'https://httpbin.org/get', headers={'NuevaCabecera': 'se tensa'})
print(response.data.decode())
"""

"""
http = urllib3.PoolManager() # Controlador de conexiones


response = http.request('GET', 'https://httpbin.org/redirect/1', redirect = False)
print(response.status)
print(response.get_redirect_location())
"""
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_NONE') # Controlador de conexiones "verify_ssl=False"
response = http.request('GET', 'https://13.109.185.30/')
print(response.data.decode())