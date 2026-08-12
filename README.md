# Transcode MP3 SRT

![Banner do Transcode MP3 SRT](banner.png)

Aplicação local para transformar vídeos em arquivos de áudio e legendas. Para cada vídeo colocado na pasta `in/`, o programa:

1. extrai o áudio em formato MP3 usando o FFmpeg;
2. transcreve o áudio em português com o modelo `medium` do Whisper;
3. gera um arquivo de legendas no formato SRT, com os tempos de início e fim de cada segmento.

Os arquivos gerados são salvos na pasta `out/`.

## Formatos de entrada

São processados vídeos com as seguintes extensões:

- `.mp4`
- `.mov`
- `.mkv`
- `.webm`

Os nomes dos arquivos de saída preservam o nome do vídeo. Por exemplo:

```text
in/aula.mp4
out/aula.mp3
out/aula.srt
```

## Pré-requisitos

- Python 3.10 ou superior;
- FFmpeg instalado e disponível no `PATH` do sistema;
- memória e espaço em disco suficientes para executar o modelo Whisper.

O projeto está configurado para usar CPU com quantização `int8`, portanto não exige uma GPU.

## Instalação

Clone o projeto, crie um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

No Windows, ative o ambiente com:

```powershell
.venv\Scripts\Activate.ps1
```

Instale também o FFmpeg. Em distribuições baseadas em Debian/Ubuntu, por exemplo:

```bash
sudo apt install ffmpeg
```

## Uso

Coloque um ou mais vídeos em `in/` e execute:

```bash
python main.py
```

O modelo do Whisper é carregado uma vez e reutilizado para todos os vídeos encontrados. A transcrição é feita em português, com filtro de atividade de voz ativado.

Se a pasta `in/` não contiver vídeos compatíveis, o programa informa que nenhum vídeo foi encontrado e encerra a execução.

## Estrutura do projeto

```text
.
├── app/
│   ├── audio.py       # Extração do áudio com FFmpeg
│   ├── srt.py         # Geração e formatação das legendas SRT
│   └── transcriber.py # Integração com faster-whisper
├── in/                # Vídeos de entrada
├── out/               # MP3 e SRT gerados
├── main.py            # Ponto de entrada da aplicação
└── requirements.txt   # Dependências Python
```

## Observações

- O áudio é convertido para mono, com taxa de amostragem de 16 kHz e bitrate de 128 kbps.
- Os arquivos existentes em `out/` com o mesmo nome são sobrescritos.
- A primeira execução pode ser mais demorada, pois o modelo Whisper precisa ser baixado e carregado.
