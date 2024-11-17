from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from logging_config import log_message, log_error


def filter_videos_by_duration(driver, duration_filter):
    try:
        log_message("Începe aplicarea filtrului de durata...")

        # accesează butonul de filtru
        log_message("Căutăm butonul de filtru...")
        filter_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="filter-button"]//button'))
        )

        log_message("Butonul de filtru a fost găsit și este clicabil.")
        filter_button.click()

        # asteapta ca optiunile de filtre să fie vizibile
        yt_filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[3]/ytd-search-filter-renderer[1]/a/div/yt-formatted-string'))
        )
        log_message(f"Opțiunea {duration_filter} a fost găsită.")

        # selectează filtrul dorit din optiuni
        yt_filter.click()
        log_message(f"Filtrul {duration_filter} a fost aplicat cu succes.")

    except TimeoutException as te:
        log_error(f"Eroare de timeout la localizarea elementului: {te}")
    except Exception as e:
        log_error(f"Eroare la aplicarea filtrului de durata: {e}")
