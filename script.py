import json
import os

from usuario import Usuario

def manejar_excepcion(error, linea):
    with open("error.log", "a", encoding="utf-8") as log:
        log.write(f"Error al procesar la línea: {linea.strip()}\n")
        log.write(f"Tipo de error: {type(error).__name__}\n")
        log.write(f"Descripción del error: {str(error)}\n\n")

def procesar_archivo():
    try:
        with open("usuarios.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                try:
                    datos_usuario = json.loads(linea)
                    usuario = Usuario(datos_usuario["nombre"], datos_usuario["apellido"], datos_usuario["email"], datos_usuario["genero"])
                    print("Usuario creado:", usuario.nombre)
                except json.JSONDecodeError as e:
                    manejar_excepcion(e, linea)
                except KeyError as e:
                    manejar_excepcion(e, linea)
                except Exception as e:
                    manejar_excepcion(e, linea)
    except FileNotFoundError as e:
        with open("error.log", "a", encoding="utf-8") as log:
            log.write(f"Error: No se pudo encontrar el archivo usuarios.txt\n")
            log.write(f"Tipo de error: {type(e).__name__}\n")
            log.write(f"Descripción del error: {str(e)}\n\n")

if __name__ == "__main__":
    procesar_archivo()
