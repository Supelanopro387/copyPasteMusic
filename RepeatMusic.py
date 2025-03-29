def detectar_duplicados(rutaArchivo):
    # Diccionario para almacenar las canciones que ya hemos visto
    canciones_vistas = {}
    # Lista para guardar las canciones duplicadas
    duplicados = []

    with open(rutaArchivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    for indice, linea in enumerate(lineas):
        # Limpiar la línea (eliminar espacios en blanco al final y saltos de línea)
        linea_limpiada = linea.strip()
        
        # Si la línea está vacía o es un comentario, omitirla
        if not linea_limpiada or linea_limpiada.startswith('#'):
            continue
        
        # Verificar si esta canción ya ha sido vista
        if linea_limpiada in canciones_vistas:
            # Agregar a la lista de duplicados
            duplicados.append((linea_limpiada, indice + 1))
        else:
            # Marcar como vista
            canciones_vistas[linea_limpiada] = True

    return duplicados

def main():
    rutaArchivo = r"C:\Users\nicop\Videos\Music\W0RK1N6.m3u"  # Ruta dura
    
    try:
        duplicados = detectar_duplicados(rutaArchivo)
        
        if len(duplicados) == 0:
            print("¡Felicidades! No hay canciones duplicadas.")
            return
        
        print("\nSe encontraron las siguientes canciones duplicadas:")
        for canción, linea in duplicados:
            print(f"Canción: {canción}")
            print(f"Ubicada en la línea {linea} del archivo .m3u")
            print("-------------------")
            
        # Opción para eliminar las canciones duplicadas
        eliminar = input("¿Quieres eliminar las canciones duplicadas? (s/n): ")
        
        if eliminar.lower() == 's':
            with open(rutaArchivo, 'r', encoding='utf-8') as archivo:
                lineas_a_eliminar = archivo.readlines()
            
            unique_songs = []
            for linea in lineas_a_eliminar:
                línea_limpiada = linea.strip()
                
                if not línea_limpiada or línea_limpiada.startswith('#'):
                    continue
                
                if línea_limpiada not in unique_songs:
                    unique_songs.append(linea)
            
            with open(rutaArchivo, 'w', encoding='utf-8') as archivo:
                archivo.writelines(unique_songs)
            
            print("¡Canciones duplicadas han sido eliminadas! Se han conservado solo las primeras versiones de cada canción.")
    except FileNotFoundError:
        print(f"El archivo {rutaArchivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
