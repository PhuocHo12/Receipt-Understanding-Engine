from pathlib import Path


def validate_image(path: str):

    p = Path(path)

    if not p.exists():
        return False

    if p.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        return False

    return True