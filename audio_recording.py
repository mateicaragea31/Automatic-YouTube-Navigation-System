#importarea librariilor necesare
import pyaudio
import wave
import time

def record_audio(output_filename="audio_record.wav", sample_rate=44100, chunk_size=1024, duration=15):
    # setari audio
    FORMAT = pyaudio.paInt16  # formatul esantionului
    channels = 1  # mono
    frames = []

    # initializeaza obiectul pyaudio
    p = pyaudio.PyAudio()

    # deschide stream-ul ca input si output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk_size)

    print(f"Inregistrare audio pentru {duration} secunde...")

    start_time = time.time()  # timpul de inceput pentru inregistrare

    while True:
        # citeste date audio din stream
        data = stream.read(chunk_size)

        # adauga datele in lista de frame-uri
        frames.append(data)

        # opreste inregistrarea dupa durata specificata
        if time.time() - start_time >= duration:
            print("Inregistrare oprita dupa durata specificata.")
            break

    # opreste si inchide stream-ul
    stream.stop_stream()
    stream.close()

    # termina obiectul pyaudio
    p.terminate()

    # salveaza inregistrarea audio in fisierul de iesire
    with wave.open(output_filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))

    print(f"Inregistrarea a fost salvata in {output_filename}")
