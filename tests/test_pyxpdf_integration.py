import pyxpdf_data
from pyxpdf import Config

# def test_integration():
#    assert Config.cfg_path == pyxpdf_data.get_xpdfrc(force_rewrite=False)


def test_xpdfrc_load():
    Config.text_encoding = "Big5"
