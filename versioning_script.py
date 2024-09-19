import subprocess

def obtener_ultima_version():
    """Obtiene la última etiqueta de versión de Git."""
    try:
        version = subprocess.check_output(["git", "describe", "--tags"]).strip().decode()
        return version
    except subprocess.CalledProcessError:
        return "0.0.0"  # Si no hay etiquetas, empezar desde 0.0.0

def incrementar_version(version, tipo_incremento):
    """Incrementa la versión MAJOR, MINOR o PATCH."""
    major, minor, patch = map(int, version.split('.'))

    if tipo_incremento == "MAJOR":
        major += 1
        minor = 0
        patch = 0
    elif tipo_incremento == "MINOR":
        minor += 1
        patch = 0
    elif tipo_incremento == "PATCH":
        patch += 1

    return f"{major}.{minor}.{patch}"

def etiquetar_nueva_version(version):
    """Etiqueta la nueva versión en Git."""
    subprocess.call(["git", "tag", version])
    subprocess.call(["git", "push", "--tags"])

# Ejemplo de uso
ultima_version = obtener_ultima_version()
print("Última versión:", ultima_version)

# Incrementar la versión
nuevo_tipo = input("Indica el tipo de incremento (MAJOR, MINOR, PATCH): ").upper()
nueva_version = incrementar_version(ultima_version, nuevo_tipo)
print("Nueva versión:", nueva_version)

# Etiquetar y empujar nueva versión a Git
etiquetar_nueva_version(nueva_version)
print(f"Versión {nueva_version} etiquetada y subida a Git.")
