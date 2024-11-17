# importarea librariilor necesare
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging_config import log_message, log_error, log_warning, log_debug

def reject_terms(driver):
    try:
        # asteapta ca butonul 'reject all' sa devina activabil si da click pe el
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Reject all']]"))
        )
        button.click()
        log_message("Popup-ul pentru termeni si conditii a fost respins cu succes.")
    except Exception as e:
        log_warning(f"Nu s-a putut gasi butonul 'Reject all' pentru termeni si conditii: {e}")
