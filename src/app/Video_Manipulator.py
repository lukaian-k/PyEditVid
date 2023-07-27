from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
import os

from app.Video_Utility import Video_Utility


class Video_Manipulator:
    def split_video(input_file, output_prefix, clip_duration=60):
        video = VideoFileClip(input_file)
        duration = video.duration

        if duration <= clip_duration:
            print("O vídeo é menor ou igual a 1 minuto. Nenhuma divisão necessária.")
            return

        num_clips = int(duration / clip_duration)

        for i in range(num_clips):
            start_time = i * clip_duration
            end_time = (i + 1) * clip_duration

            clip = video.subclip(start_time, end_time)

            output_file = f"{output_prefix}_{i+1}.mp4"
            clip.write_videofile(output_file, codec="libx264")

        video.reader.close()

    def join_videos_upright(self, videos, output):
        videos = [
            VideoFileClip(video)
            for video in videos
        ]
        total = len(videos)

        new_height = videos[0].h // total

        videos[0] = videos[0].resize(height=new_height)
        videos[0] = videos[0].set_position(("center", "top"))

        if total == 3:
            videos[1] = videos[1].resize(height=new_height)
            videos[1] = videos[1].set_position(("center", "center"))

        videos[-1] = videos[-1].resize(height=new_height)
        videos[-1] = videos[-1].set_position(("center", "bottom"))

        new_width = max(videos[0].w, videos[-1].w)

        final_video = CompositeVideoClip(
            [video for video in videos],
            size=(new_width, new_height * total)
        )

        final_video.write_videofile(
            output, codec='libx264', fps=videos[0].fps
        )

    def join_videos_layered(self, layers):
        directory = "data/output/video_subtitles"
        videos = Video_Utility.get_video_files_in_directory(directory)

        base_directory = os.getcwd()

        for i in range(0, len(videos), layers):
            output = f"data/output/final_videos/{layers}_layers/video_final_{i + 1}.mp4"

            video_paths = [
                os.path.join(
                    base_directory,
                    directory,
                    f"{videos[j]}"
                )
                for j in range(i, min(i + layers, len(videos)))
            ]
            self.join_videos_upright(video_paths, output)
