# Ejemplos para practicar y comprender mejor le uso de self.

class Calculadora:

    def __init__(self, numero): # Calculadora.__init__(calc, numero)
        self.numero = numero # calc.numero = 5

    def suma(self, otro_numero): # Calculadora.suma(calc, 9)
        return self.numero + otro_numero # calc.numero + 9 -> 5 + 9 = 14
    
    def doble_suma(self, num1, num2): # Calculadora.doble_suma(calc, 2, 9)
        return self.suma(num2) # calc.sum(2) + calc.suma(9) -> Calculadora.suma(calc, 2) + Calculadora.suma(calc, 9) = 14 + 7
    
calc = Calculadora(5)
calc.suma(8)

print(calc.doble_suma(2, 9))