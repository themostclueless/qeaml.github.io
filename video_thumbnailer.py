from pathlib import Path
from pyffmpeg import FFmpeg, FFprobe


def create_thumbnail(video: Path, thumbnail: Path) -> None:
    probe = FFprobe(str(video.absolute()))
    elem = probe.duration.split(":")
    seconds = float(elem[-1]) / 2
    minutes = int(elem[-2]) / 2
    hours = int(elem[-3]) / 2
    halftime = seconds + ((minutes + hours * 60) * 60)
    halftime_seconds = int(halftime % 60)
    halftime_minutes = int(halftime / 60) % 60
    halftime_hours = int(halftime / 3600) % 60
    halftime_stamp = f"{halftime_hours:02}:{halftime_minutes:02}:{halftime_seconds:02}"
    ff = FFmpeg()
    ff.options(
        f"-i {video.absolute()} -vf scale=320:-1 -ss {halftime_stamp} -vframes 1 {thumbnail.absolute()}"
    )


def create_thumbnails_in(dir: Path) -> None:
    for video in dir.rglob("*.mp4"):
        thumbnail = video.with_suffix(video.suffix + ".jpg")
        if not thumbnail.exists():
            create_thumbnail(video, thumbnail)


def main(args: list[str]) -> int:
    create_thumbnails_in(Path("static"))
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
