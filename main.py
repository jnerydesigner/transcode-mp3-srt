from pathlib import Path

from app.audio import extract_audio
from app.srt import generate_srt
from app.transcriber import Transcriber

INPUT_DIR = Path("in")
OUTPUT_DIR = Path("out")

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".mkv",
    ".webm",
}


def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    videos = [
        file
        for file in INPUT_DIR.iterdir()
        if file.suffix.lower() in VIDEO_EXTENSIONS
    ]

    if not videos:
        print("Nenhum vídeo encontrado.")
        return

    print("Carregando Whisper...")

    transcriber = Transcriber(
        model_name="medium",
        device="cpu",
        compute_type="int8",
    )

    for video in videos:

        print()
        print("=" * 60)
        print(f"Processando: {video.name}")
        print("=" * 60)

        # VIDEO -> MP3

        print("Extraindo áudio...")

        audio_path = extract_audio(
            video,
            OUTPUT_DIR,
        )

        print(
            f"MP3: {audio_path}"
        )

        # MP3 -> TRANSCRIÇÃO

        print("Transcrevendo...")

        segments, info = transcriber.transcribe(
            audio_path,
            language="pt",
        )

        # TRANSCRIÇÃO -> SRT

        srt_path = (
            OUTPUT_DIR /
            f"{video.stem}.srt"
        )

        generate_srt(
            segments,
            srt_path,
        )

        print(
            f"SRT: {srt_path}"
        )

    print()
    print("Processamento concluído.")


if __name__ == "__main__":
    main()
