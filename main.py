import tkinter as tk
from tkinter import messagebox
import yt_dlp
import threading
import os
import sys

def baixar_audio():
    url = entrada_url.get().strip()

    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira a URL do vídeo.")
        return

    btn_baixar.config(state="disabled")
    status_label.config(text="Baixando e convertendo...")

    def processar():
        try:
            # Caminho para ffmpeg local (mesma pasta do .py ou .exe)
            if getattr(sys, 'frozen', False):
                ffmpeg_path = os.path.join(sys._MEIPASS, 'ffmpeg.exe')
            else:
                ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')

            ydl_opts = {
                'format': 'bestaudio/best',
                'ffmpeg_location': ffmpeg_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': '%(title)s.%(ext)s',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            status_label.config(text="Download concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao baixar: {str(e)}")
            status_label.config(text="Erro durante o download.")
        finally:
            btn_baixar.config(state="normal")

    threading.Thread(target=processar).start()

# Interface gráfica
janela = tk.Tk()
janela.title("YouTube para MP3")
janela.geometry("400x200")

label = tk.Label(janela, text="Insira a URL do vídeo:")
label.pack(pady=10)

entrada_url = tk.Entry(janela, width=50)
entrada_url.pack()

btn_baixar = tk.Button(janela, text="Baixar MP3", command=baixar_audio)
btn_baixar.pack(pady=10)

status_label = tk.Label(janela, text="")
status_label.pack()

janela.mainloop()