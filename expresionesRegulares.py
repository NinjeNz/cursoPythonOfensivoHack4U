#!/usr/bin/env python3

# Expresiones regulares conocidas como regex

import re

#--- Ejemplos de uso ---

#text = "Mi gato esta en el tejado y mi otro gato esta en el jardin"
#matches = re.findall("gato", text)
#print(matches)

#text2 = "Hoy estamos a fecha 04/04/2025, mañana estaremos a 05/04/2025"
#matches = re.findall("\d{2}\/\d{2}\/\d{4}", text2)
#print(matches)

#text3 = "Los usuarios pueden contactarnos a soporte@hack4u.io o a info@hack4u.io"
#matches = re.findall("(\w+)@(\w+\.\w{2,})", text3)
#print(matches)

#texto = "Mi gato esta en el tejado y mi perro esta en el jardin"
#nuevo_texto = re.sub("gato", "perro", texto)
#print(nuevo_texto)

#texto = "Campo1,Campo2,Campo3,Campo4,Campo5"
#nuevo_texto = re.split(",", texto)
#print(nuevo_texto)
#print(nuevo_texto[2])

"""def validar_correo(correo):
    patron = "[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}"

    if re.findall(patron, correo):
        return True
    else:
        return False
    
print(validar_correo("soporte@hack4u.io"))"""

texto = "Hoy estamos a dia 10/10/2023 y mañana estaremos 11/10/2023"
patron = r"\b(\d{2}\/\d{2}\/\d{4})\b"

for match in re.finditer(patron, texto):
    print(f"La fecha es: {match.group(0)}, la cual comienza en la posicion {match.start()} y termina en la posicion {match.end()}")