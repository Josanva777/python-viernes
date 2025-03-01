# Paso 1: Lista de participantes
# Crea una lista vacía llamada 'participantes'
participantes = []  # COMPLETAR: inicializa una lista vacía

# Agrega al menos 3 participantes iniciales usando .append()
participantes.append("Alex")  # COMPLETAR: agrega "Alex"
participantes.append("Sofia")  # COMPLETAR: agrega "Sofia"
participantes.append("Juan")  # COMPLETAR: agrega "Juan"

# Agrega 2 participantes más en una sola línea usando una lista y extend()
participantes.extend(["Luna", "Max"])  # COMPLETAR: agrega ["Luna", "Max"] usando extend

print("Participantes del torneo:", participantes)

# Paso 2: Tupla con detalles de un juego
# Crea una tupla llamada 'juego' con 3 elementos: nombre ("FIFA"), género ("Deportes"), año (1993)
juego = ("FIFA", "Deportes", 1993)  # COMPLETAR: define la tupla con ("FIFA", "Deportes", 1993)

# Imprime un mensaje usando los elementos de la tupla
print(f"El juego {juego[0]} es del género {juego[1]} y fue lanzado en {juego[2]}.")  # COMPLETAR: usa 'juego' y sus índices

# Paso 3: Conjunto de equipos
# Crea un conjunto vacío llamado 'equipos'
equipos = set()  # COMPLETAR: inicializa un conjunto vacío

# Agrega 4 equipos al conjunto usando .add(), incluyendo un duplicado (ej. "Leones" dos veces)
equipos.add("Leones")  # COMPLETAR: usa 'equipos'
equipos.add("Nacional")   # COMPLETAR: usa 'equipos'
equipos.add("junior")  # COMPLETAR: usa 'equipos'
equipos.add("Medellin")  # COMPLETAR: usa 'equipos' (duplicado)

print("Equipos registrados:", equipos)
 
# Paso 4: Diccionario de puntajes
# Crea un diccionario 'puntajes' con al menos 5 participantes y sus puntajes iniciales
puntajes = {
    "Alex": 100,  # COMPLETAR: asigna un puntaje (ej. 100)
    "Sofia": 85,  # COMPLETAR: asigna un puntaje (ej. 85)
    "Juan": 120,  # COMPLETAR: asigna un puntaje (ej. 120)
    "Luna": 90,   # COMPLETAR: asigna un puntaje (ej. 90)
    "Max": 110    # COMPLETAR: asigna un puntaje (ej. 110)
}

print("Puntajes del torneo:", puntajes)

# Paso 5: Operaciones con las colecciones
# a) Elimina a "Juan" de la lista 'participantes' usando .remove()
participantes.remove("Juan")  # COMPLETAR: elimina "Juan" de 'participantes'

print("Participantes después de la retirada de Juan:", participantes)

# b) Imprime el año de lanzamiento del juego desde la tupla 'juego'
print("Año de lanzamiento del juego:", juego[2])  # COMPLETAR: accede al año con índice

# c) Agrega un nuevo equipo "Águilas" al conjunto y verifica si está presente con 'in'
equipos.add("Águilas")  # COMPLETAR: agrega "Águilas" a 'equipos'
print("¿Águilas está en los equipos?", "Águilas" in equipos)  # COMPLETAR: verifica con 'in'

# d) Actualiza el puntaje de "Max" a 150 en el diccionario
puntajes["Max"] = 150  # COMPLETAR: actualiza el puntaje de "Max" a 150

print("Puntajes actualizados:", puntajes)

# Paso 6: Interacción con el usuario
# Pide al usuario un nombre y un puntaje, y actualiza/añade ese dato al diccionario 'puntajes'
nombre = input("Ingresa el nombre del participante: ")
puntaje = int(input("Ingresa el puntaje del participante: "))  # COMPLETAR: convierte la entrada a entero

puntajes[nombre] = puntaje  # COMPLETAR: actualiza/añade el puntaje en 'puntajes'

print("Puntajes actualizados:", puntajes)