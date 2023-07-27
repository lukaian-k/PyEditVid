import os


class Video_Utility:
    def get_video_files_in_directory(directory):
        video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv']
        video_files = []

        for filename in os.listdir(directory):
            if any(filename.lower().endswith(ext) for ext in video_extensions):
                video_files.append(filename)

        return sorted(video_files)

    def clean_subdirectories(directory):
        for foldername, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                os.remove(file_path)
            if foldername != directory:
                shutil.rmtree(foldername)
