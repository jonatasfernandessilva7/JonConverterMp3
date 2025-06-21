# JonConverterMp3
Um conversor e baixador de vídeos direto do youtube para formato MP3

# Requisitos
Para rodar essa aplicação desktop windows deve-se preencher alguns requisitos, a saber:

- Ter o **ffmpeg.exe** dentro da mesma pasta do **main.py**
  
    > Faça o download do ffmpeg em: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
  
- Instalar as bibliotecas **yt_dlp** e **pyinstaller**, para isso copie e cole os comandos abaixo em seu terminal
  
  ```bash
  pip install yt-dlp
  pip install pyinstaller
  ```
  
O **pyinstaller** é o responsável por gerar o arquivo executável em sua máquina.

# Gerando o Executável
Tendo cumprido os requisitos, copie e cole o comando abaixo:

```bash
pyinstaller --onefile --windowed main.py --add-binary "ffmpeg.exe;."
```

Um arquivo executável será gerado dentro da pasta "/dist"

# Utilizando
- Passo 1: Execute a aplicação
- Passo 2: Copie no youtube o link da do vídeo música que deseja baixar
- Passo 3: Cole o link na aplicação
- Passo 4: Clique no botão "Baixar MP3"

**OBS: As músicas ficarão salvas dentro da pasta "/dist", no mesmo local onde o executável está salvo.***

# Autor
Jônatas Fernandes
