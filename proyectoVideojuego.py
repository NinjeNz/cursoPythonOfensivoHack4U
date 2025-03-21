juegos = ["Super Mario Bros", "Zelda: Breath Of The Wild", "Cyberpunk 2077", "Final Fantasy VII"]

tope = 500

# Generos
generos = {
    "Super Mario Bros": "Aventura",
    "Zelda: Breath Of The Wild": "Aventura",
    "Cyberpunk 2077": "Rola",
    "Final Fantasy VII": "Rol"
}

# Ventas y Stock
ventas_y_stock = {
    "Super Mario Bros": (400, 200),
    "Zelda: Breath Of The Wild": (600, 20),
    "Cyberpunk 2077": (60, 120),
    "Final Fantasy VII": (924, 3)
}

#Clientes
clientes = {
    "Super Mario Bros": {"Marcelo", "Hackermate", "Hackavis", "Securiters", "Lobotec"},
    "Zelda: Breath Of The Wild": {"Hackermate", "Hackavis", "Lucia", "Manolo", "Pinolo"},
    "Cyberpunk 2077": {"Hackermate", "Lobotec", "Pepe", "Raquel", "Alberto"},
    "Final Fantasy VII": {"Lucia", "Manolo", "Pepe", "Securiters", "Patricia", "Moises"}
}

def sumario(juego):
    # Sumario
    print(f"\n[i] Resumen del juego {juego}\n")
    print(f"\t[+] Genero del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Total de stock para este juego: {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Clientes que han comprado este juego: {', '.join(clientes[juego])}")

for juego in juegos:
    if ventas_y_stock[juego][0] > tope:
        sumario(juego)

ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope)
print(f"\t[+] El total de ventas de todos los productos ha sido de {ventas_totales()} productos")