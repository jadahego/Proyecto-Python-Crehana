# Clase 1 Proyecto: Definiendo la aventura

# Equipamiento - Costo en monedas dragul (nueva moneda del juego)
print("Define el equipamiento para una aventura de exploración y su valor en draguls (moneda del juego):")

equipamiento = {
    "mapa": 50.0,
    "botas": 100.0,
    "batería": 20.0,
    "linterna": 30.0,
    "agua": 10.0,
    "botella": 5.0,
    "snacks": 15.0,
    "brújula": 25.0,
    "reloj": 40.0,
    "lentes_sol": 60.0,
}

def mostrar_objetos(equipamiento, objetos):
    for obj in objetos:
        print(f"{obj}: {equipamiento[obj]} draguls")

# Mostrando tres objetos del equipamiento
print("Lista tres objetos del equipamiento: Nombre y valor")
mostrar_objetos(equipamiento, ["botella", "agua", "snacks"])

# Operadores
print("\n¿Puedes combinar elementos de tu equipo para prepararte mejor?")

agua_en_botella = equipamiento["agua"] + equipamiento["botella"]
linterna_funcional = equipamiento["linterna"] + equipamiento["batería"]

print(f"Agua en botella: {agua_en_botella} draguls")
print(f"Linterna funcional: {linterna_funcional} draguls")

print("\n¿El precio del agua en botella es menor al de la linterna funcional?")
print(agua_en_botella < linterna_funcional)

print("\n¿Cuánto valdría comprar unos snacks y una brújula?")
print(equipamiento["snacks"] + equipamiento["brújula"])

print("\n¿Si tengo 100 draguls, me alcanza para comprar unas botas?")
print(equipamiento["botas"] <= 100)

# Clase 2 Proyecto: Tomando decisiones

print("\nNo colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 draguls: ¿Cuáles elementos colocarías?")

def verificar_mochila(limite, *args):
    total = sum(args)
    if total <= limite:
        return total
    return None

mochila = verificar_mochila(200, agua_en_botella, linterna_funcional, equipamiento["brújula"], equipamiento["reloj"], equipamiento["snacks"])

if mochila:
    print(f"El valor de los elementos es menor a 200: {mochila} draguls")
else:
    print("Ups! Ninguna de tus combinaciones fue exitosa")

# Ciclos

print("\nEs tu día de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")
mochila_dos = 0

while mochila_dos + agua_en_botella <= 200:
    mochila_dos += agua_en_botella
    print(f"Mochila dos: {mochila_dos} draguls")

print(f"Nos pasamos, vamos a restar una botella de agua, ahora tenemos: {mochila_dos - agua_en_botella} draguls")

# Clase 3 Proyecto: Diccionarios

print("\nLa esfinge le hizo una actualización a tu mochila, ahora sabrás el objeto que tienes, la cantidad y su valor unitario")

mochila_actualizada = {
    "agua_en_botella": {"cantidad": 1, "valor_unitario": agua_en_botella},
    "linterna_funcional": {"cantidad": 1, "valor_unitario": linterna_funcional},
    "brújula": {"cantidad": 1, "valor_unitario": equipamiento["brújula"]},
}

mochila_dos_actualizada = {
    "agua_en_botella": {"cantidad": 2, "valor_unitario": agua_en_botella},
}

# Clase 4 Proyecto: Listas

print("\nEn esta aventura te van a acompañar 7 integrantes más, y te han pedido que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehículo")

vehiculo = []

for _ in range(7):
    vehiculo.append(mochila_actualizada.copy())

for idx, mochila in enumerate(vehiculo, start=1):
    print(f"Acabas de armar la mochila para el compartimiento: {idx}")
    print(mochila)

print("\nLa esfinge te pide que para tres integrantes se recolecten 3 elementos sin importar las cantidades y te da las siguientes opciones: brújula, linterna_funcional, snacks y agua_en_botella")

def agregar_elementos_a_mochilas(vehiculo, elementos):
    for i in range(3):
        vehiculo[i].update(elementos)

def calcular_total_elementos_en_mochilas(vehiculo):
    total_elementos = {}
    for mochila in vehiculo:
        for item, detalles in mochila.items():
            if item in total_elementos:
                total_elementos[item] += detalles["cantidad"]
            else:
                total_elementos[item] = detalles["cantidad"]
    return total_elementos

elementos_nuevos = {
    "agua_en_botella": {"cantidad": 1, "valor_unitario": agua_en_botella},
    "linterna_funcional": {"cantidad": 2, "valor_unitario": linterna_funcional},
    "brújula": {"cantidad": 3, "valor_unitario": equipamiento["brújula"]},
    "snacks": {"cantidad": 2, "valor_unitario": equipamiento["snacks"]},
}

agregar_elementos_a_mochilas(vehiculo, elementos_nuevos)
total_elementos = calcular_total_elementos_en_mochilas(vehiculo)

print("\nTotal de elementos en todas las mochilas:")
for elemento, cantidad in total_elementos.items():
    print(f"{elemento}: {cantidad} unidades")
