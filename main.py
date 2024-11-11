#importarea librariilor necesare
import time
import threading
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#importarea fisierelor separate
from accept_terms import reject_terms
from skip_premium import skip_premium_popup
from screen_recording import record_screen
from audio_recording import record_audio
from internet_check import monitor_connection

# functie pentru a incepe inregistrarea ecranului intr-un thread separat
def start_screen_recording():
    record_screen(output_filename='screen_record.avi', fps=12.0, duration=15)

# functie pentru a incepe inregistrarea audio intr-un thread separat
def start_audio_recording():
    record_audio(output_filename="audio_recording.wav", sample_rate=44100, chunk_size=1024, duration=15)

if __name__ == "__main__":

    # seteaza selenium webdriver
    service = Service('/usr/local/bin/chromedriver')  # inlocuieste cu calea corecta pentru chromedriver
    driver = webdriver.Chrome(service=service)

    # incepe monitorizarea conexiunii de internet intr-un thread separat
    internet_thread = threading.Thread(target=monitor_connection, args=(driver,), daemon=True)
    internet_thread.start()

    # deschide youtube si intra in modul ecran complet
    driver.get("https://www.youtube.com")
    driver.fullscreen_window()

    # inchide popup-ul pentru termenii si conditiile prin reject
    time.sleep(5)  # permite timp pentru incarcare popup
    reject_terms(driver)

    # asteapta ca bara de cautare sa fie vizibila si efectueaza cautarea
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'search_query'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", search_box)  # deruleaza pana la bara de cautare
        search_box.click()  # asigura ca este interactiva
        search_box.send_keys('random video')  # introduce termenul de cautare
        search_box.send_keys(Keys.RETURN)  # efectueaza cautarea
        print("Cautare initiata cu succes.")
    except Exception as e:
        print("Nu s-a putut interactiona cu bara de cautare:", e)
        driver.quit()
        exit()

    # asteapta ca al doilea videoclip sa fie activabil si da click pe el
    time.sleep(5)  # asteapta rezultatele cautarii
    try:
        video = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//*[@id="video-title"])[2]'))  # da click pe al doilea videoclip
        )
        video.click()
        print("Al doilea videoclip a pornit cu succes.")
    except Exception as e:
        print("Nu s-a putut porni videoclipul:", e)
        driver.quit()
        exit()

    # inchide popup-ul youtube premium daca apare
    skip_premium_popup(driver)

    # incepe inregistrarea ecranului intr-un thread separat
    screen_thread = threading.Thread(target=start_screen_recording)
    screen_thread.start()

    # incepe inregistrarea audio intr-un thread separat
    audio_thread = threading.Thread(target=start_audio_recording)
    audio_thread.start()

    # asteapta terminarea ambelor thread-uri de inregistrare
    screen_thread.join()
    audio_thread.join()

    # inchide browserul
    driver.quit()

    print("Inregistrarea ecranului si audio completata.")

    # verifica daca fisierul de inregistrare a fost creat si contine date
    if os.path.exists("screen_record.avi") and os.path.getsize("screen_record.avi") > 0:
        print(f"Fisierul de inregistrare a fost creat cu dimensiunea: {os.path.getsize('screen_record.avi')} bytes.")
    else:
        print("Fisierul de inregistrare este gol sau nu exista.")
