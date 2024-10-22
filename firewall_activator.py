import subprocess
import logging

def activate_firewall():
    code = ["netsh", "advfirewall", "set", "allprofiles", "state", "on"]
    try:
        status = subprocess.run(code, capture_output=True, text=True)
        if status.returncode == 0:
            print("Firewall bien activado")
            logging.info("Firewall activado exitosamente.")
        else:
            print("Error activando")
            print(status.stderr.strip())  # Imprimir el error en la consola
            logging.error("Error al activar el firewall: %s", status.stderr.strip())
    except FileNotFoundError as e:
        print("No se encontró el archivo")
        logging.error("Archivo no encontrado: %s", e)

