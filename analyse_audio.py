from pydub import AudioSegment
from logging_config import log_message, log_error

def analyse_audio(video_path, output_file):
    try:
        # extrage sunetul din fisierul video
        audio = AudioSegment.from_file(video_path, format="mp4")

        # calculeaza nivelul de sunet mediu in dbfs
        dBFS = audio.dBFS

        # scrie rezultatele in fisierul de iesire
        with open(output_file, "w") as file:
            file.write(f"Nivelul mediu de sunet (dbfs) pentru {video_path} este: {dBFS:.2f} db.\n")

        log_message(f"Analiza audio completa. Rezultatele au fost salvate in {output_file}")

    except Exception as e:
        log_error(f"Eroare la analizarea fisierului audio: {e}")
