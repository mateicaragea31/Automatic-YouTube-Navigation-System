from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging_config import log_message, log_error


def set_playback_speed(driver, speed=1.5):
    try:
        # așteaptă până când elementul video este prezent
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'video'))
        )

        # folosesc JavaScript pentru a seta viteza de redare
        driver.execute_script(f"document.querySelector('video').playbackRate = {speed};")

        log_message(f"Playback-ul video-ului a fost setat la {speed}x.")
    except Exception as e:
        log_error(f"Eroare la setarea vitezei de redare: {e}")
