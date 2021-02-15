import os
import time
from pathlib import Path
from hashlib import md5
from appdirs import AppDirs

from .encodings import _get_encodings_block
from .fonts import _get_fonts_block, get_fonts
from .utils import POPPLER_DATA_DIR

__version__ = "1.1.0"
PYXPDF_RC_PATH = "PYXPDF_RC_PATH"


def _xpdfrc_header():
    return [
        "# {0}".format(time.ctime()),
        "# Generated by pyxpdf_poppler_data python module",
        "# THIS FILE WILL NOT WORK ON OTHER SYSTEM, ",
        "# AS IT USES ABSOLUTE PATHs",
        "",
    ]


def generate_xpdfrc():
    xpdfrc = _xpdfrc_header()

    xpdfrc += _get_encodings_block()
    xpdfrc += _get_fonts_block()

    return os.linesep.join(xpdfrc)


def get_poppler_dir():
    return str(POPPLER_DATA_DIR)

    
def get_xpdfrc_path():
    """
    Get the path of xpdfrc file.

    First try to get the path from an environment variable named `PYXPDF_RC_PATH`.
    If the variable does not exist, fall back to the user application  data directory
    using appdirs package.
    """
    if PYXPDF_RC_PATH in os.environ:
        xpdf_rc_path = Path(os.environ[PYXPDF_RC_PATH])
    else:
        pyxpdf_user_data_dir = AppDirs("pyxpdf", version=__version__).user_config_dir
        # Make sure that this config file is unique to this instance as multiple pyxpdf_data installations
        # may exist in one system (i.e. virtual environments and/or freezed applications).
        data_path_hash = md5(str(POPPLER_DATA_DIR.resolve()).encode('utf-8')).hexdigest()
        xpdf_rc_path = Path(pyxpdf_user_data_dir).joinpath(data_path_hash, "default.xpdf")
    return xpdf_rc_path


def get_xpdfrc(force_rewrite=True):
    """
    Get the generated xpdfrc file path.

    Parameters
    ----------
    force_rewrite: bool
        generate xpdfrc again even if it exists already. Helpful if somehow xpdfrc file
        got corrupted.
    """
    xpdfrc_path = get_xpdfrc_path()
    if (not xpdfrc_path.exists()) or force_rewrite:
        xpdfrc = generate_xpdfrc()
        xpdfrc_path.parent.mkdir(parents=True, exist_ok=True)
        with open(str(xpdfrc_path), "w") as fp:
            fp.write(xpdfrc)
    return str(xpdfrc_path.absolute().resolve())


__all__ = [get_fonts, get_xpdfrc, get_poppler_dir, generate_xpdfrc]
