#importarea librariilor necesare
import ffmpeg

def merge_audio_video(video_file, audio_file, output_file):
    try:
        # input video si audio separat cu 'analyzeduration' si 'probesize' crescute?
        video = ffmpeg.input(video_file, analyzeduration=2147483647, probesize=2147483647)
        audio = ffmpeg.input(audio_file)

        # re-encodeaza video-ul intr-un format standard cu codec h.264 si audio aac
        ffmpeg.output(video, audio, output_file, vcodec='libx264', acodec='aac', strict='experimental').run()
        print(f"Imbinarea si re-encodarea audio si video s-au finalizat cu succes in {output_file}")
    except ffmpeg.Error as e:
        print(f"A aparut o eroare la imbinarea si re-encodarea audio si video: {e}")
