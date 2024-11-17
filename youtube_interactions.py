import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from logging_config import log_message, log_error, log_warning, log_debug

def initialize_driver(chromedriver_path='/usr/local/bin/chromedriver'):
    try:
        # initializeaza optiunile pentru chrome pentru o stabilitate mai buna
        options = Options()
        options.add_argument("--disable-infobars")  # dezactiveaza infobars pentru o interfata mai curata
        options.add_argument("--no-sandbox")  # evita problemele cu sandboxing in unele medii
        options.add_experimental_option("detach", True)  # mentine browserul deschis dupa finalizarea scriptului

        # initializeaza driverul chrome cu optiunile specificate
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)

        log_message("Driverul Chrome a fost initializat cu succes")
        return driver
    except Exception as e:
        log_error(f"Eroare la inițializarea driverului Chrome: {e}")
        raise

def open_youtube(driver):
    try:
        # deschide youtube si intra in modul ecran complet
        driver.get("https://www.youtube.com")
        driver.fullscreen_window()
        log_message("YouTube a fost deschis în modul ecran complet")
    except Exception as e:
        log_error(f"Eroare la deschiderea YouTube: {e}")
        driver.quit()
        raise

def search_youtube(driver, search_term):
    try:
        # asteapta ca bara de cautare sa fie vizibila si efectueaza cautarea
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'search_query'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", search_box)
        search_box.click()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        log_message(f"Cautare pe YouTube pentru termenul '{search_term}' initiata cu succes")
    except Exception as e:
        log_error(f"Nu s-a putut interactiona cu bara de cautare: {e}")
        driver.quit()
        raise

def select_video(driver):
    try:
        # asteapta ca al doilea videoclip sa fie accesibil
        time.sleep(2)  # asteapta putin pentru ca pagina sa se incarce corect
        video = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//*[@id="video-title"])[7]'))
        )

        # deruleaza catre videoclip inainte de a face click
        driver.execute_script("""
            var element = arguments[0];
            element.scrollIntoView({ behavior: 'smooth', block: 'center' });
        """, video)

        # asteapta ca animatia de derulare sa se finalizeze
        time.sleep(2)

        # face click pe al doilea videoclip
        video.click()
        log_message("Al doilea videoclip a inceput cu succes")
        time.sleep(5)  # asteapta ca videoclipul sa se incarce

    except Exception as e:
        log_error(f"Nu s-a putut reda al doilea videoclip: {e}")
        driver.quit()
        raise
