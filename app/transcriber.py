from pathlib import Path

from faster_whisper import WhisperModel


class Transcriber:

    def __init__(
        self,
        model_name: str = "medium",
        device: str = "cuda",
        compute_type: str = "float16",
    ):
        self.model = WhisperModel(
            model_name,
            device=device,
            compute_type=compute_type,
        )

    def transcribe(
        self,
        audio_path: Path,
        language: str = "pt",
    ):

        segments, info = self.model.transcribe(
            str(audio_path),
            language=language,
            beam_size=5,
            vad_filter=True,
        )

        return segments, info
