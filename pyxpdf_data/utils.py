from pathlib import Path

ROOT = Path(__file__).parent
POPPLER_DATA_DIR = Path(ROOT, "poppler_data")
FONT_DATA_DIR = Path(ROOT, "fonts")


def _get_root_files(path):
    return [x for x in Path(path).iterdir() if x.is_file()]


def _get_root_dirs(path):
    return [x for x in Path(path).iterdir() if x.is_dir()]
