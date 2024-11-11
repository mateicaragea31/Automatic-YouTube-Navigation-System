# importarea librariilor necesare
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def skip_premium_popup(driver):
    try:
        # asteapta ca butonul sa fie vizibil si-l apasa
        no_thanks_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "No thanks")]'))
        )
        no_thanks_button.click()
        print("Popup-ul pentru youtube premium a fost omis.")
    except Exception as e:
        print("Nu a fost gasit butonul 'nu multumesc':", e)
