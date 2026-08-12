import subprocess
from pathlib import Path


def extract_audio(
    video_path: Path,
    output_dir: Path,
) -> Path:

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    audio_path = output_dir / f"{video_path.stem}.mp3"

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(video_path),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        "-codec:a",
        "libmp3lame",
        "-b:a",
        "128k",
        str(audio_path),
    ]

    subprocess.run(
        command,
        check=True,
    )

    return audio_path
