import csv
import os

# Cargar datos desde paises.csv
def cargar_datos(nombre_archivo="paises.csv"): 
    paises = []  
    
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))  
    
    ruta_completa = os.path.join(carpeta_actual, nombre_archivo)  
    
    try:
        
        with open(ruta_completa, "r", encoding="utf-8") as archivo: 
            lector = csv.reader(archivo) 
            next(lector) 
            
            for fila in lector: 
                if len(fila) != 4: 
                    continue 
                
                nombre = fila[0].strip()
                try: 
                    poblacion = int(fila[1]) 
                    superficie = int(fila[2]) 
                except ValueError: 
                    continue 
                
                continente = fila[3].strip()
                paises.append({ 
                    "nombre": nombre, 
                    "poblacion": poblacion, 
                    "superficie": superficie, 
                    "continente": continente 
                }) 
        print(f"¡Éxito! Se cargaron {len(paises)} países.")  
    except FileNotFoundError: 
        print("\nError: No se encontró el archivo.") 
        print(f"Python está buscando aquí: {ruta_completa}") 
        print("Asegúrate de que 'paises.csv' esté en ESA carpeta exacta.")
    return paises


# Guardar en CSV
def guardar_datos(paises, nombre_archivo="paises.csv"): 
    encabezado = ["nombre", "poblacion", "superficie", "continente"] 
    try: 
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo: 
            escritor = csv.DictWriter(archivo, fieldnames=encabezado) 
            escritor.writeheader() 
            escritor.writerows(paises) 
        print("✔ Datos guardados en el archivo CSV correctamente.") 
    except IOError: 
        print(" Error: No se pudo escribir en el archivo.")


# Validar que no esté vacío
def obtener_dato_no_vacio(mensaje): 
    dato = input(mensaje).strip() 
    while dato == "": 
        print("Error: el campo no puede estar vacío.") 
        dato = input(mensaje).strip() 
    return dato


# Valida que la opción ingresada sea un número entero válido
def validar_opcion_menu(opcion): 
    opcion = opcion.strip()
    if not opcion.isdigit(): 
        return None
    return int(opcion)


# Agregar un país
def agregar_pais(paises): 
    print("\n--- Agregar nuevo país ---")
    nombre = obtener_dato_no_vacio("Ingrese el nombre del país: ").title() 
    continente = obtener_dato_no_vacio("Ingrese el continente: ").title()
    
    while True: 
        try: 
            poblacion = int(obtener_dato_no_vacio("Ingrese la población: ")) 
            superficie = int(obtener_dato_no_vacio("Ingrese la superficie (km2): "))
            if poblacion < 0 or superficie < 0: 
                print("Error: los valores numéricos no pueden ser negativos.") 
                continue
            break 
        except ValueError: 
            print("Error: deben ser números enteros.")
            
    paises.append({ 
        "nombre": nombre, 
        "poblacion": poblacion, 
        "superficie": superficie, 
        "continente": continente 
    })
    print("\nPaís agregado con éxito.")


# Actualiza un país existente
def actualizar_pais(pais):
    print("\n--- Actualizar país ---") 
    print("Datos actuales:") 
    mostrar_pais(pais)
    
    # Actualizar población 
    while True: 
        try: 
            nueva_poblacion = int(obtener_dato_no_vacio("Nueva población: ")) 
            if nueva_poblacion < 0: 
                print("Error: la población no puede ser negativa.") 
                continue 
            break 
        except ValueError: 
            print("Error: debe ser un número entero válido.")
            
    # Actualizar superficie 
    while True: 
        try: 
            nueva_superficie = int(obtener_dato_no_vacio("Nueva superficie (km2): ")) 
            if nueva_superficie < 0: 
                print("Error: la superficie no puede ser negativa.") 
                continue 
            break 
        except ValueError: 
            print("Error: debe ser un número entero válido.")
            
    # Guardar cambios 
    pais["poblacion"] = nueva_poblacion 
    pais["superficie"] = nueva_superficie
    print("\nPaís actualizado correctamente.") 
    mostrar_pais(pais)



def obtener_nombre(pais): return pais["nombre"].lower()
def obtener_poblacion(pais): return pais["poblacion"]
def obtener_superficie(pais): return pais["superficie"]


# Buscar país por nombre 
def buscar_pais(paises, nombre): 
    nombre = nombre.lower()
    
    for pais in paises: 
        if pais["nombre"].lower() == nombre: 
            return pais
    
    for pais in paises: 
        if nombre in pais["nombre"].lower(): 
            return pais
    return None


# Filtrar por continente
def filtrar_continente(paises, continente): 
    resultado = [] 
    continente = continente.lower() 
    for pais in paises: 
        if pais["continente"].lower() == continente: 
            resultado.append(pais)
            
    if not resultado: 
        print("No se encontraron países en ese continente.") 
    
    return resultado  


# Filtrar país según rango de población
def filtrar_rango_poblacion(paises): 
    print("\n--- Filtrar por rango de población ---")
    while True: 
        try: 
            minimo = int(obtener_dato_no_vacio("Ingrese la población mínima: ")) 
            if minimo < 0: 
                print("Error: la población no puede ser negativa.") 
                continue 
            break 
        except ValueError: 
            print("Error: debe ingresar un número entero válido.")
            
    while True: 
        try: 
            maximo = int(obtener_dato_no_vacio("Ingrese la población máxima: ")) 
            if maximo < 0: 
                print("Error: la población no puede ser negativa.") 
                continue 
            break 
        except ValueError: 
            print("Error: debe ingresar un número entero válido.")
            
    if minimo > maximo: 
        print("Error: el mínimo no puede ser mayor que el máximo.") 
        return None
        
    filtrados = [] 
    for pais in paises: 
        if minimo <= pais["poblacion"] <= maximo: 
            filtrados.append(pais)
            
    if not filtrados: 
        print("No se encontraron países dentro de ese rango.") 
    else: 
        print(f"\nPaíses con población entre {minimo} y {maximo}:") 
        mostrar_paises(filtrados) 
    return filtrados


# Filtrar países según un rango de superficie
def filtrar_rango_superficie(paises): 
    print("\n--- Filtrar por rango de superficie ---")
    while True: 
        try: 
            minimo = int(obtener_dato_no_vacio("Ingrese la superficie mínima (km2): ")) 
            if minimo < 0: 
                print("Error: la superficie no puede ser negativa.") 
                continue 
            break 
        except ValueError: 
            print("Error: debe ingresar un número entero válido.")
            
    while True: 
        try: 
            maximo = int(obtener_dato_no_vacio("Ingrese la superficie máxima (km2): ")) 
            if maximo < 0: 
                print("Error: la superficie no puede ser negativa.") 
                continue 
            break 
        except ValueError: 
            print("Error: debe ingresar un número entero válido.")
            
    if minimo > maximo: 
        print("Error: el mínimo no puede ser mayor que el máximo.") 
        return None
        
    filtrados = [] 
    for pais in paises: 
        if minimo <= pais["superficie"] <= maximo: 
            filtrados.append(pais)
            
    if not filtrados: 
        print("No se encontraron países dentro de ese rango de superficie.") 
    else: 
        print(f"\nPaíses con superficie entre {minimo} y {maximo} km2:") 
        mostrar_paises(filtrados) 
    return filtrados



def algoritmo_burbuja(lista, clave_funcion, descendente=False):
    """
    Ordena una copia de la lista usando el algoritmo de burbuja 
    según la función de clave provista.
    """
    lista_copia = lista.copy()  
    n = len(lista_copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = clave_funcion(lista_copia[j])
            val2 = clave_funcion(lista_copia[j+1])
            
            
            intercambiar = val1 > val2 if not descendente else val1 < val2
            
            if intercambiar:
                lista_copia[j], lista_copia[j+1] = lista_copia[j+1], lista_copia[j]
    return lista_copia


def ordenar_por_nombre(paises): 
    paises_ordenados = algoritmo_burbuja(paises, obtener_nombre, descendente=False)
    mostrar_paises(paises_ordenados) 
    return paises_ordenados

def ordenar_por_poblacion(paises): 
    paises_ordenados = algoritmo_burbuja(paises, obtener_poblacion, descendente=False) 
    mostrar_paises(paises_ordenados) 
    return paises_ordenados 

def ordenar_por_superficie(paises, descendente=True): 
    paises_ordenados = algoritmo_burbuja(paises, obtener_superficie, descendente=descendente) 
    mostrar_paises(paises_ordenados) 
    return paises_ordenados


def ordenar_paises(paises): 
    if not paises:
        print("No hay países para ordenar.")
        return
        
    print("""\n--- OPCIONES DE ORDENAMIENTO ---
    1) Nombre (A-Z)
    2) Población (Menor a Mayor)
    3) Superficie (Ascendente)
    4) Superficie (Descendente)
    5) Volver al menú principal""")

    while True: 
        opcion = validar_opcion_menu(input("Ingrese la opción de ordenamiento: ")) 
        match opcion: 
            case 1: 
                ordenar_por_nombre(paises) 
                break 
            case 2: 
                ordenar_por_poblacion(paises) 
                break 
            case 3: 
                ordenar_por_superficie(paises, descendente=False) 
                break 
            case 4: 
                ordenar_por_superficie(paises, descendente=True) 
                break 
            case 5: 
                break 
            case _: 
                print("🚨 Opción inválida. Elija de 1 a 5.")


def menu_filtros(): 
    print("""\n--- FILTROS ---
    1) Filtrar por continente
    2) Filtrar por rango de población
    3) Filtrar por rango de superficie
    4) Volver al menú principal""") 
    opcion = input("Ingrese una opción: ") 
    return validar_opcion_menu(opcion)


# Estadísticas
def estadistica_mayor_y_menor_poblacion(paises): 
    mayor_poblacion = None 
    menor_poblacion = None
    
    for pais in paises: 
        if mayor_poblacion is None or pais['poblacion'] > mayor_poblacion['poblacion']: 
            mayor_poblacion = pais 
        if menor_poblacion is None or pais['poblacion'] < menor_poblacion['poblacion']: 
            menor_poblacion = pais
            
    print(f"\nEl país con mayor población es {mayor_poblacion['nombre']} con {mayor_poblacion['poblacion']} habitantes") 
    print(f"El país con menor población es {menor_poblacion['nombre']} con {menor_poblacion['poblacion']} habitantes\n")


def estadistica_promedio_poblacion(paises): 
    total_poblacion = 0 
    for pais in paises: 
        total_poblacion += pais['poblacion']
        
    promedio_poblacion = total_poblacion / len(paises) 
    print(f"\nEl promedio de población es {promedio_poblacion:.2f} habitantes\n")


def estadistica_promedio_superficie(paises): 
    total_superficie = 0 
    for pais in paises: 
        total_superficie += pais['superficie'] 
        
    promedio_superficie = total_superficie / len(paises) 
    print(f"\nEl promedio de superficie es {promedio_superficie:.2f} km²\n")


def estadistica_cantidad_paises_por_continente(paises): 
    cantidad_paises_por_continente = {}
    
    for pais in paises: 
        continente = pais['continente'] 
        if continente not in cantidad_paises_por_continente: 
            cantidad_paises_por_continente[continente] = 0 
        cantidad_paises_por_continente[continente] += 1
        
    print("\nCantidad de países por continente:") 
    for continente, cantidad in cantidad_paises_por_continente.items(): 
        print(f" - {continente}: {cantidad} países") 
    print()


# Muestra estadísticas
def mostrar_estadisticas(paises): 
    if not paises:
        print("No hay países cargados para calcular estadísticas.")
        return

    print("""\n--- ESTADÍSTICAS ---
    1) País con mayor y menor población
    2) Promedio de población
    3) Promedio de superficie
    4) Cantidad de países por continente
    5) Volver al menú principal""")
    
    while True: 
        opcion = validar_opcion_menu(input("Ingrese la opción de estadística: "))
        match opcion: 
            case 1: 
                estadistica_mayor_y_menor_poblacion(paises) 
            case 2: 
                estadistica_promedio_poblacion(paises) 
            case 3: 
                estadistica_promedio_superficie(paises) 
            case 4: 
                estadistica_cantidad_paises_por_continente(paises) 
            case 5: 
                break 
            case _: 
                print("Opción inválida")


# Mostrar país 
def mostrar_pais(pais): 
    print("------------------------------") 
    print("Nombre:", pais["nombre"]) 
    print("Población:", pais["poblacion"], "hab") 
    print("Superficie:", pais["superficie"], "km2") 
    print("Continente:", pais["continente"]) 
    print("------------------------------")


# Mostrar lista de países 
def mostrar_paises(lista): 
    if not lista:
        return
    print("------------------------------------------------")
    for p in lista: 
        print(f"{p['nombre']:<15} | {p['poblacion']:>12} hab | {p['superficie']:>10} km2 | {p['continente']}")
    print("------------------------------------------------")


def mostrar_menu(): 
    print("""\n================ MENU PRINCIPAL ================""")
    print("1) Agregar un país")
    print("2) Actualizar un país")
    print("3) Buscar un país")
    print("4) Filtrar países")
    print("5) Ordenar países")
    print("6) Mostrar estadísticas")
    print("7) Salir")
    print("================================================")
    opcion = input("Ingrese una opción: ") 
    return validar_opcion_menu(opcion)


# Programa principal
def main(): 
    paises = cargar_datos()
    
    while True: 
        opcion = mostrar_menu()
        
        if opcion is None:
            print("Opción inválida. Debe ingresar un número del 1 al 7.")
            continue
            
        # Agregar país 
        if opcion == 1: 
            agregar_pais(paises) 
            guardar_datos(paises)
            
        # Actualizar país 
        elif opcion == 2: 
            nombre = input("Ingrese el nombre del país a actualizar: ") 
            pais = buscar_pais(paises, nombre)
            if pais: 
                actualizar_pais(paises)
                guardar_datos(paises) 
            else: 
                print("País no encontrado.")
                
        # Buscar país 
        elif opcion == 3: 
            nombre = input("Ingrese el nombre del país: ") 
            pais = buscar_pais(paises, nombre)
            if pais: 
                mostrar_pais(pais) 
            else: 
                print("País no encontrado.")
                
        # Filtros 
        elif opcion == 4: 
            while True: 
                sub = menu_filtros()
                if sub is None:
                    print("Opción inválida.")
                    continue
                
                if sub == 1: 
                    cont = input("Ingrese el continente: ") 
                    lista = filtrar_continente(paises, cont) 
                    mostrar_paises(lista)
                elif sub == 2: 
                    filtrar_rango_poblacion(paises) 
                elif sub == 3: 
                    filtrar_rango_superficie(paises) 
                elif sub == 4: 
                    break 
                else: 
                    print("Opción inválida.")
                    
        # Ordenamientos  
        elif opcion == 5: 
            ordenar_paises(paises)
            
        # Estadísticas
        elif opcion == 6: 
            mostrar_estadisticas(paises)
            
        # Salir  
        elif opcion == 7: 
            print("Saliendo del programa... ¡Hasta luego!") 
            break
        else: 
            print("Opción inválida.")

if __name__ == "__main__":
    main()