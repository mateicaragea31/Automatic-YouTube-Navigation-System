import ffmpeg
from logging_config import log_message, log_error

def merge_audio_video(video_file, audio_file, output_file):
    try:
        # deschide fișierele video și audio ca fluxuri de input
        video_input = ffmpeg.input(video_file)
        audio_input = ffmpeg.input(audio_file)

        # configurare pentru îmbinarea audio și video
        (ffmpeg.output(video_input, audio_input, output_file,
                      vcodec='copy',
                      acodec='aac',
                      strict='experimental')
         .run(overwrite_output=True))

        log_message(f"Fișierele {video_file} și {audio_file} au fost combinate cu succes în {output_file}")

    except Exception as e:
        log_error(f"Eroare la imbinarea fisierelor audio si video: {e}")
