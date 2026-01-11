import os
from shutil import copyfile

# Configuración inicial
m3u_file = r"C:\Users\nicop\Videos\Music\W0RK1N6.m3u" # Actualiza con tu ruta
destino = r"C:\Users\nicop\Downloads\Music" # C:\Users\nicop\Videos\Rutes-Music\KL3T0$
# destino = r"C:\Users\nicop\Downloads\Music"

# Lista para archivos no encontrados
no_encontrados = []

# abre el archivo .m3u con codificación UTF-8
with open(m3u_file, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

for linea in lineas:
    # Omite líneas vacías y comentarios (líneas que empiezan con '#')
    if not linea.strip() or linea.startswith('#'):
        continue
    
    # Construye la ruta del archivo
    ruta_origen = os.path.normpath(linea.strip())
    
    # Verifica si el archivo existe
    if os.path.exists(ruta_origen):
        try:
            # Copia el archivo al destino
            copyfile(ruta_origen, os.path.join(destino, os.path.basename(ruta_origen)))
            print(f"Copiado: {os.path.basename(ruta_origen)}")
        except Exception as e:
            print(f"Error al copiar {os.path.basename(ruta_origen)}: {str(e)}")
            no_encontrados.append(os.path.basename(ruta_origen))
    else:
        # Si el archivo no existe, agrega a la lista de no encontrados
        print(f"No encontrado: {linea.strip()}")
        no_encontrados.append(os.path.basename(linea.strip()))

# Muestra los archivos que no fueron encontrados
print("\nArchivos no encontrados:")
for archivo in no_encontrados:
    print(archivo)
