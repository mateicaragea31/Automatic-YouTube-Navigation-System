# importarea librariilor necesare
import cv2
import numpy as np
import mss
import time

def record_screen(output_filename="screen_recording.avi", fps=12.0, duration=15):
    # obtine rezolutia ecranului
    with mss.mss() as sct:
        screen_size = sct.monitors[1]['width'], sct.monitors[1]['height']

        # aleg codec-ul pentru encodarea video
        fourcc = cv2.VideoWriter_fourcc(*"XVID")

        # creez obiectul videowriter pentru a salva iesirea
        out = cv2.VideoWriter(output_filename, fourcc, fps, screen_size)

        print(f"Inregistrare ecran pentru {duration} secunde...")

        # timpul de inceput pentru inregistrare
        start_time = time.time()

        while True:
            # face un screenshot folosind mss
            screenshot = sct.shot(output="temp.png")

            # citeste screenshot-ul
            img = cv2.imread(screenshot)

            # converteste imaginea din bgr in rgb
            frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # scrie cadrul in fisierul video
            out.write(frame)

            # opreste inregistrarea dupa durata specificata
            if time.time() - start_time >= duration:
                print("Inregistrarea a fost oprita dupa durata specificata.")
                break

        # elibereaza videowriter si inchide toate ferestrele opencv
        out.release()
        cv2.destroyAllWindows()
        print(f"Inregistrarea a fost salvata in {output_filename}")
