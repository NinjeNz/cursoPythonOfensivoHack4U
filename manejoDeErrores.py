try:
     
     num = 10/2

except ZeroDivisionError:
     print("No se puede divir un numero entre cero")
except TypeError:
     print("¡Las operaciones matematicas solo deben realizarse con numeros!")
else:
     print(f"La division de ambos numeros da como resultado {num}")
finally:
     print("Esto siempre se va a ejecutar")

x = -5

if x < 0:
     raise Exception("No se pueden utilizar numeros negativos")

