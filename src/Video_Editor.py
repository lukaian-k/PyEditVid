import subprocess


class Video_Editor:
    def add_text_to_video(input_file, output_prefix, text, duration=60):
        ffmpeg_cmd = [
            'ffmpeg', '-i', input_file,
            '-vf', f"drawtext=text='{text}':fontsize=50:fontcolor=white:x=(w-text_w)/2:y=h-text_h-20:enable='between(t,0,{duration})'",
            '-codec:a', 'copy', output_prefix
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print("Texto adicionado com sucesso ao vídeo!")
        except subprocess.CalledProcessError as error:
            print(f"Erro ao adicionar texto ao vídeo: {error}")
