#!/usr/bin/env python3

# Expresiones regulares conocidas como regex

import re

text = "Mi gato esta en el tejado y mi otro gato esta en el jardin"
matches = re.findall("gato", text)
print(matches)

text2 = "Hoy estamos a fecha 04/04/2025, mañana estaremos a 05/04/2025"
matches = re.findall("\d{2}\/\d{2}\/\d{4}", text2)
print(matches)