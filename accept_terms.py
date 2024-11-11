#importarea librariilor necesare
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def reject_terms(driver):
    try:
        # asteapta ca butonul 'Reject all' sa devina activabil si da click pe el
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Reject all']]"))
        )
        button.click()
        print("Popup respins cu succes.")
    except Exception as e:
        print("Nu s-a putut gasi butonul 'Reject all':", e)
