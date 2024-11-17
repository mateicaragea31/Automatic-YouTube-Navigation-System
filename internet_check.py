# importarea librariilor necesare
import requests
import time
import threading
import sys
from logging_config import log_message, log_error, log_warning, log_debug

class NoInternetConnectionError(Exception):
    pass

def check_internet_connection():
    try:
        # incearca sa acceseze un site-ul google pentru a verifica conexiunea la internet
        response = requests.get('https://www.google.com', timeout=5)
        if response.status_code != 200:
            raise NoInternetConnectionError("Nu a fost detectata conexiune la internet.")
    except (requests.ConnectionError, requests.exceptions.Timeout):
        raise NoInternetConnectionError("Nu a fost detectata conexiune la internet.")

# verifica periodic conexiunea la internet in background
def monitor_connection(driver):
    while True:
        try:
            check_internet_connection()
            time.sleep(5)  # verifica la fiecare 5 secunde
        except NoInternetConnectionError as e:
            log_error(f"{str(e)} Conexiunea la internet a fost pierduta. Inchide programul.")

            # inchide browserul si opreste programul
            driver.quit()
            log_message("Browserul a fost inchis din cauza lipsei conexiunii la internet.")
            exit()
