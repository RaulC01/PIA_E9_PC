import requests
import logging

# Configurar el logging para que se guarde en un archivo .txt
logging.basicConfig(filename="script_usage.txt",  # Cambia el nombre a script_usage.txt
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Función para reportar la ip
def reportip(ipfortest, comment, category):
    api_key = "e05e746c9560a6ab1bf42cd0890678e812608307097bb0b4b90232b6d0e290df5f7933302609d2fb"
    
    url = "https://api.abuseipdb.com/api/v2/report"
    headers = { 
        "Accept": 'application/json',
        "Key": api_key
    }
    
    data = {
        "ip": ipfortest,
        "comment": comment,
        "categories": category
    }
    
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print("Todo funcionó bien")
        print(response.json())
        logging.info("IP reportada exitosamente: %s", ipfortest)
    else:
        print("No funcionó el reporte de la IP")
        print(response.text)
        logging.error("Error al reportar la IP %s: %s", ipfortest, response.text) 
# Función para checarla
def checkip(ipfortest):
    api_key = "e05e746c9560a6ab1bf42cd0890678e812608307097bb0b4b90232b6d0e290df5f7933302609d2fb"

    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Accept": 'application/json',
        "Key": api_key
    }

    params = {
        "ipAddress": ipfortest,
        "maxAgeInDays": "3"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        score = data["data"]["abuseConfidenceScore"]
        if score > 0:
            print("La IP ha sido reportada con un puntaje de: " + str(score))
            logging.info("La IP %s ha sido reportada antes con un puntaje de: " + str(score)) 
        else:
            print("La IP no se reportó antes")
            logging.info("La IP %s no se reportó antes", ipfortest) 
    else:
        print("No funcionó el chequeo de la IP, intente con otra")
        print(response.text)
        logging.error("Error al chequear la IP %s: %s", ipfortest, response.text)
