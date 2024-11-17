import threading
import os
import time
from selenium.common.exceptions import WebDriverException

# importarea functiilor
from youtube_interactions import initialize_driver, open_youtube, search_youtube, select_video
from accept_terms import reject_terms
from skip_premium import skip_premium_popup
from screen_recording import record_screen
from audio_recording import audio_recording
from internet_check import monitor_connection
from logging_config import log_message, log_error, log_warning, log_debug
from driver_monitoring import monitor_driver, keep_running
from merge_audio_video import merge_audio_video
from analyse_audio import analyse_audio
from video_data_collector import collect_video_data
from set_playback_speed import set_playback_speed
from youtube_filters import filter_videos_by_duration

if __name__ == "__main__":
    driver = None
    try:
        # initializeaza driverul si deschide youtube
        driver = initialize_driver()
        log_message("Driver initializat cu succes")

        # porneste monitorizarea driverului intr-un thread separat
        monitoring_thread = threading.Thread(target=monitor_driver, args=(driver,))
        monitoring_thread.daemon = True  # asigura-te ca se opreste cand programul principal se termina
        monitoring_thread.start()
        log_message("Monitorizarea driverului a inceput")

        # deschide youtube si-l face full screen
        open_youtube(driver)
        log_message("YouTube deschis in modul ecran complet")

        # porneste monitorizarea conexiunii de internet intr-un thread separat
        internet_thread = threading.Thread(target=monitor_connection, args=(driver,), daemon=True)
        internet_thread.start()
        log_debug("Monitorizarea conexiunii de internet a pornit")

        # porneste inregistrarea audio intr-un thread separat
        audio_thread = threading.Thread(target=audio_recording,
                                        args=("audio_recording.wav", 30, 44100, 6))
        audio_thread.start()
        log_debug("Inregistrarea audio a fost pornita.")

        # porneste inregistrarea ecranului intr-un thread separat
        screen_thread = threading.Thread(target=record_screen,
                                         args=("screen_recording.mp4", 30, 25))  # 60 secunde la 25.1 FPS
        screen_thread.start()
        log_debug("Inregistrarea ecranului a fost pornita.")

        # inchide popup-ul pentru termenii si conditiile
        time.sleep(5)
        reject_terms(driver)
        log_message("Popup-ul pentru termeni si conditii inchis")

        # efectueaza cautarea
        search_youtube(driver, 'test video')
        log_message("Cautare pe YouTube realizata cu succes")
        time.sleep(1)

        # aplica filtrul pentru durata videoclipurilor sub 4 minute
        filter_videos_by_duration(driver, 'Under 4 minutes')
        time.sleep(1)

        # porneste videoclipul
        select_video(driver)
        time.sleep(3)

        # setează viteza de redare la 1.5x
        set_playback_speed(driver, speed=1.5)
        log_message("Viteza de redare a fost setată la 1.5x.")

        # inchide popup-ul pentru youtube premium
        skip_premium_popup(driver)

        # așteaptă terminarea înregistrărilor video și audio si efectueza operatia de merge
        screen_thread.join()
        audio_thread.join()
        log_message("Inregistrarile video si audio sunt pregatite de merge")

        # colecteaza datele video
        collect_video_data(driver, "video_data.txt")

        # merge intre fisierul audio si cel video
        merge_audio_video("screen_recording.mp4", "audio_recording.wav", "final_recording.mp4")

        # analiza audio a fisierului de inregistrare final
        analyse_audio("final_recording.mp4", "audio_analysis.txt")
        log_message("Analiza audio a fost completă. Rezultatele sunt salvate.")

        log_message("Merge complet. Programul se inchide.")

    except Exception as e:
        log_error(f"Eroare in script: {e}")
    finally:
        if driver:
            driver.quit()
        log_message("Browserul inchis si programul a fost incheiat.")
