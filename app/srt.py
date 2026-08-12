from pathlib import Path


def format_timestamp(seconds: float) -> str:

    milliseconds = int(seconds * 1000)

    hours = milliseconds // 3_600_000
    milliseconds %= 3_600_000

    minutes = milliseconds // 60_000
    milliseconds %= 60_000

    secs = milliseconds // 1000
    milliseconds %= 1000

    return (
        f"{hours:02}:"
        f"{minutes:02}:"
        f"{secs:02},"
        f"{milliseconds:03}"
    )


def generate_srt(
    segments,
    output_path: Path,
) -> Path:

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        index = 1

        for segment in segments:

            text = segment.text.strip()

            if not text:
                continue

            start = format_timestamp(
                segment.start
            )

            end = format_timestamp(
                segment.end
            )

            file.write(
                f"{index}\n"
                f"{start} --> {end}\n"
                f"{text}\n\n"
            )

            index += 1

    return output_path
