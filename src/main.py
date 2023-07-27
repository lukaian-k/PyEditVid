import tkinter as tk
from tkinter import messagebox

from app.Video_Utility import Video_Utility
from app.Video_Manipulator import Video_Manipulator
from app.Video_Editor import Video_Editor


class App:
    DIR_DATA_INPUT = "data/input"
    DIR_DATA_OUTPUT = "data/output"

    def split():
        videos_collected = Video_Utility.get_video_files_in_directory(
            App.DIR_DATA_INPUT
        )
        input_file = f"{App.DIR_DATA_INPUT}/{videos_collected[0]}"
        output_prefix = f"{App.DIR_DATA_OUTPUT}/cropped_videos/part"

        Video_Manipulator.split_video(input_file, output_prefix)
        messagebox.showinfo("Cortar o vídeo", "Todos os cortes foram feitos!")

    def add_text():
        directory = f"{App.DIR_DATA_OUTPUT}/cropped_videos"
        video_files = Video_Utility.get_video_files_in_directory(directory)

        for index, filename in enumerate(video_files):
            output_prefix = f"{App.DIR_DATA_OUTPUT}/video_subtitles/{filename}"
            text = f"Parte {index+1}"

            Video_Editor.add_text_to_video(
                input_file=f"{directory}/{filename}",
                output_prefix=output_prefix,
                text=text
            )
        messagebox.showinfo("Adicionar texto", "Os textos foram adicionados!")

    def join_videos():
        directory = f"{App.DIR_DATA_OUTPUT}/video_subtitles"

        video_manipulator = Video_Manipulator()
        video_manipulator.join_videos_layered(2, directory)
        video_manipulator.join_videos_layered(3, directory)
        del video_manipulator

        messagebox.showinfo(
            "Juntar vídeos",
            "Os videos de 2 e 3 camadas foram criados!"
        )

    def clean():
        directorys = [
            "cropped_videos",
            "video_subtitles",
            "final_videos/2_layers",
            "final_videos/3_layers",
        ]

        for directory in directorys:
            Video_Utility.clean_subdirectories(
                f"{App.DIR_DATA_OUTPUT}/{directory}"
            )

        messagebox.showinfo(
            "Limpar diretórios",
            "Todos os vídeos foram deletados!"
        )

    def quit_application():
        root.quit()


root = tk.Tk()
root.title("PyEditVid")
root.geometry("235x300")

palette = [
    "#4d2600",
    "#704214",
    "#8c5c2f",
    "#a97d5b",
    "#c3a080",
]

root.config(bg=palette[2])
custom_font = ("Helvetica", 14, "bold")

btn_01 = tk.Button(
    root, text="Cortar o vídeo",
    command=App.split,
    font=custom_font,
    bg=palette[0],
    fg="white",
    padx=20
)
btn_01.grid(row=0, pady=10, padx=20, sticky="ew")

btn_02 = tk.Button(
    root,
    text="Adicionar texto",
    command=App.add_text,
    font=custom_font,
    bg=palette[1],
    fg="white",
    padx=20
)
btn_02.grid(row=1, pady=10, padx=20, sticky="ew")

btn_03 = tk.Button(
    root,
    text="Juntar vídeos",
    command=App.join_videos,
    font=custom_font,
    bg=palette[3],
    fg="white",
    padx=20
)
btn_03.grid(row=2, pady=10, padx=20, sticky="ew")

btn_04 = tk.Button(
    root,
    text="Limpar diretórios",
    command=App.clean,
    font=custom_font,
    bg=palette[0],
    fg="white",
    padx=20
)
btn_04.grid(row=3, pady=10, padx=20, sticky="ew")

quit_btn = tk.Button(
    root,
    text="Quit",
    command=App.quit_application,
    font=custom_font,
    bg=palette[4],
    fg="white",
    padx=20
)
quit_btn.grid(row=4, pady=20, padx=20, sticky="ew")

window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()

position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)

root.geometry(f"+{position_right}+{position_down}")
root.mainloop()
