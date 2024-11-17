import time
from selenium.common.exceptions import WebDriverException
from logging_config import log_message, log_error

# mentine driverul activ si verifica daca este functional
def monitor_driver(driver):
    try:
        while True:
            try:
                # incearca sa acceseze URL-ul curent pentru a verifica daca driverul este activ
                current_url = driver.current_url
                time.sleep(5)  # asteapta putin si verifica din nou
            except WebDriverException:
                # daca WebDriverException este accesat, driverul nu mai este functional
                log_message("Driverul s-a inchis. Scriptul va fi oprit.")
                break
    except Exception as e:
        log_error(f"Eroare la monitorizarea driverului: {e}")

# mentine programul activ cat timp driverul este functional
def keep_running(driver):
    try:
        while True:
            try:
                # verifica continuu daca driverul este activ
                current_url = driver.current_url
                time.sleep(3)  # asteapta pentru a preveni utilizarea excesiva a procesorului
            except WebDriverException:
                log_message("Browserul s-a inchis. Programul se opreste.")
                break
    except Exception as e:
        log_error(f"Eroare la mentinerea programului in functiune: {e}")
        driver.quit()
