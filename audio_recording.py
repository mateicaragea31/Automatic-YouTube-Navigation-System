import sounddevice as sd
import soundfile as sf
from logging_config import log_message, log_error, log_debug

def audio_recording(output_file, duration, sample_rate, device_index):
    try:
        log_debug(f"Inceperea inregistrarii audio de pe dispozitivul cu indexul {device_index}...")

        # porneste inregistrarea audio de pe dispozitivul selectat
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, device=device_index)

        # asteapta terminarea inregistrarii
        sd.wait()

        # salveaza inregistrarea audio in fisierul wav
        sf.write(output_file, audio_data, sample_rate)

        log_message(f"Fisierul audio a fost salvat in {output_file}")

    except Exception as e:
        log_error(f"Eroare in timpul inregistrarii audio: {e}")
