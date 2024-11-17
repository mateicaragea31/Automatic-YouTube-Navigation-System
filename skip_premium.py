import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging_config import log_message, log_error, log_warning, log_debug

def skip_premium_popup(driver):
    try:
        # asteapta ca butonul 'no thanks' sa fie vizibil si-l apasa
        no_thanks_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "No thanks")]'))
        )
        no_thanks_button.click()
        log_message("Popup-ul pentru YouTube Premium a fost omis.")
    except Exception as e:
        log_warning(f"Nu a fost gasit butonul 'No thanks' pentru popup-ul YouTube Premium: {e}")
