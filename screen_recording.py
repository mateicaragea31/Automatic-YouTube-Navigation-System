import numpy as np
import cv2
import time
from mss import mss
from logging_config import log_message, log_error, log_debug

def record_screen(output_file, duration, fps):
    # dimensiunile ecranului
    SCREEN_SIZE = (2880, 1800)

    # seteaza formatul fisierului video
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(output_file, fourcc, fps, SCREEN_SIZE)
    log_message(f"Începerea înregistrării ecranului pentru {duration} secunde la {fps} FPS")

    # seteaza dimensiunile video-ului
    monitor = {"top": 0, "left": 0, "width": 1440, "height": 900}
    start_time = time.time()  # salveaza timpul de start

    try:
        with mss() as sct:
            while True:
                last_time = time.time()

                # captureaza ecranul
                img = np.array(sct.grab(monitor))

                # converteste imaginea din bgra in bgr (elimina canalul alpha)
                img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

                # scrie captura in fisierul video
                out.write(img)

                # afiseaza fps-ul
                fps_value = 1 / (time.time() - last_time)

                # opreste inregistrarea dupa durata specificata
                if time.time() - start_time > duration:
                    log_message("Timpul de înregistrare a expirat.")
                    break  # opreste bucla dupa durata specificata

    except Exception as e:
        log_error(f"Eroare în timpul capturării ecranului: {e}")
    finally:
        # elibereaza resursele
        out.release()
        cv2.destroyAllWindows()
        log_message("Înregistrarea ecranului s-a încheiat și resursele au fost eliberate.")
