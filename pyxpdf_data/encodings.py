import os
from pathlib import Path

from .utils import POPPLER_DATA_DIR, _get_root_dirs, _get_root_files


def _process_poppler_data(entry):
    lines = [
        "# {0}".format(entry),
    ]

    if entry == "nameToUnicode":
        for file in _get_root_files(Path(POPPLER_DATA_DIR, entry)):
            lines.append('nameToUnicode "{0}"'.format(file.absolute()))
    elif entry == "cidToUnicode":
        for file in _get_root_files(Path(POPPLER_DATA_DIR, entry)):
            lines.append('cidToUnicode {0} "{1}"'.format(file.name, file.absolute()))
    elif entry == "unicodeMap":
        for file in _get_root_files(Path(POPPLER_DATA_DIR, entry)):
            lines.append('unicodeMap {0} "{1}"'.format(file.name, file.absolute()))
    elif entry == "cMap":
        for directory in _get_root_dirs(Path(POPPLER_DATA_DIR, entry)):
            lines.append(
                'cMapDir {0} "{1}"'.format(directory.name, directory.absolute())
            )

    lines.append("")
    return lines


def _get_encodings_block():
    enc_block = [
        "# Extra Encodings".upper(),
    ]
    for entry in ["nameToUnicode", "cidToUnicode", "unicodeMap", "cMap"]:
        enc_block += _process_poppler_data(entry)
    enc_block.append("")
    return enc_block
