puertos_tcp = [21, 22, 25, 80, 443, 8080, 445, 69]

puertos_tcp.append(9443)

for puerto in puertos_tcp:
    print(f"Este es el puerto: {puerto}")

puertos_tcp.sort()
print(puertos_tcp)

cve_list = ['CVE-2023-1435', 'CVE-2022-45761', 'CVE-2023-7863']

print(cve_list)
cve_list.remove('CVE-2023-7863')
print(cve_list)

attacks = ['Phishing', 'DDoS', 'SQL Injection', 'Man In The Middle', 'Cross-Site Scripting']
print(attacks)
#attacks.reverse()
#print(attacks)

primer_ataque = attacks[2]
print(primer_ataque)

another_attacks_list = attacks[:3]
print(another_attacks_list)

another_attacks_list = attacks[-3:]
print(another_attacks_list)

another_attacks_list = attacks[3:]
print(another_attacks_list)

another_attacks_list = attacks[-1]
print(another_attacks_list)

another_attacks_list = attacks[-2]
print(another_attacks_list)

another_attacks_list = attacks[2:5]
print(another_attacks_list)

i = 0 # Contador

while i < len(attacks):
    print(attacks[i])

    i += 1

for attack in attacks:
    print(f"Este es el ataque {attack}")

for i, attack in enumerate(attacks):
    print(f"Para la posicion {i+1} tendriamos el ataque {attack}")

attacks_uppercase = [attack.upper() for attack in attacks]

print(attacks_uppercase)

attacks_lowercase = [attack.lower() for attack in attacks]

print(attacks_lowercase)

names = ["Luis", "Laksmi", "Dionicio", "Fernando", "Israel", "Paco"]
edades = [31, 32, 55, 28, 18, 24]

for name, edad in zip(names, edades):
    print(f"{name} tiene {edad} años")

#del names[5] --> Elimina el indice indicado de la lista
#names.remove("Paco") --> Elimina el elemento indicado de la lista
#names.clear() --> Borra toda la lista
print(names)

names[5] = "Lalito"
print(names)

deleted_user = names.pop(5) # pop( elimina el ultimo elemento y lo podemos almacenar en una variable)
print(names)
print(f"El usuario eliminado es {deleted_user}")

names.insert(2, "Oscarito") # Inserta elementos a la lista
print(names)

more_names = ["Raul", "Rafa", "Pitagoras"]
names.extend(more_names) # Combina listas
print(names)