import os
import subprocess

# === CONFIGURACIÓN ===
m3u_path = r"C:\Users\nicop\Videos\Music\M4L14NT30$.m3u"


def convertir_m4a_a_mp3(ruta_m4a):
    """Convierte un archivo .m4a a .mp3 usando ffmpeg"""
    ruta_mp3 = ruta_m4a.replace(".m4a", ".mp3")

    # Si ya existe el mp3, no lo vuelve a convertir
    if os.path.exists(ruta_mp3):
        print(f"✔ Ya existe: {ruta_mp3}")
        return ruta_mp3

    # Ejecutar conversión
    comando = [
        "ffmpeg", "-y",
        "-i", ruta_m4a,
        "-codec:a", "libmp3lame",
        "-qscale:a", "2",
        ruta_mp3
    ]

    try:
        subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"🎵 Convertido: {os.path.basename(ruta_m4a)} → {os.path.basename(ruta_mp3)}")

        # Eliminar el archivo original
        os.remove(ruta_m4a)
        print(f"🗑️ Eliminado: {os.path.basename(ruta_m4a)}")

        return ruta_mp3
    except subprocess.CalledProcessError:
        print(f"⚠️ Error al convertir: {ruta_m4a}")
        return None


def procesar_playlist(m3u_path):
    """Lee el .m3u, convierte canciones .m4a y actualiza el archivo"""
    if not os.path.exists(m3u_path):
        print("❌ No se encontró el archivo .m3u")
        return

    with open(m3u_path, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    nuevas_lineas = []
    for linea in lineas:
        linea_limpia = linea.strip()

        # Si la línea termina en .m4a, cámbiala a .mp3 incluso si el archivo ya no existe
        if linea_limpia.lower().endswith(".m4a"):
            ruta_mp3 = linea_limpia[:-4] + ".mp3"  # cambia extensión
            # Si el archivo .m4a existía antes, intenta convertirlo
            if os.path.exists(linea_limpia):
                convertir_m4a_a_mp3(linea_limpia)
            linea_limpia = ruta_mp3

        nuevas_lineas.append(linea_limpia + "\n")

    # Reescribir el mismo archivo .m3u con las rutas actualizadas
    with open(m3u_path, "w", encoding="utf-8") as f:
        f.writelines(nuevas_lineas)

    print(f"\n✅ Playlist actualizada correctamente: {m3u_path}")


# === EJECUCIÓN PRINCIPAL ===
if __name__ == "__main__":
    procesar_playlist(m3u_path)
