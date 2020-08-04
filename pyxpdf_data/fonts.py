from pathlib import Path

from .utils import FONT_DATA_DIR

# fmt: off
fonts_mapping = {
    "AvantGarde-Book":              "URWGothic-Book",
    "AvantGarde-BookOblique":       "URWGothic-BookOblique",
    "AvantGarde-Demi":              "URWGothic-Demi",
    "AvantGarde-DemiOblique":       "URWGothic-DemiOblique",
    "Bookman-Demi":                 "URWBookman-Demi",
    "Bookman-DemiItalic":           "URWBookman-DemiItalic",
    "Bookman-Light":                "URWBookman-Light",
    "Bookman-LightItalic":          "URWBookman-LightItalic",
    "Courier":                      "NimbusMonoPS-Regular",
    "Courier-Bold":                 "NimbusMonoPS-Bold",
    "Courier-BoldOblique":          "NimbusMonoPS-BoldItalic",
    "Courier-Oblique":              "NimbusMonoPS-Italic",
    "Helvetica":                    "NimbusSans-Regular",
    "Helvetica-Bold":               "NimbusSans-Bold",
    "Helvetica-BoldOblique":        "NimbusSans-BoldItalic",
    "Helvetica-Narrow":             "NimbusSansNarrow-Regular",
    "Helvetica-Narrow-Bold":        "NimbusSansNarrow-Bold",
    "Helvetica-Narrow-BoldOblique": "NimbusSansNarrow-BdOblique",
    "Helvetica-Narrow-Oblique":     "NimbusSansNarrow-Oblique",
    "Helvetica-Oblique":            "NimbusSans-Italic",
    "NewCenturySchlbk-Bold":        "C059-Bold",
    "NewCenturySchlbk-BoldItalic":  "C059-BdIta",
    "NewCenturySchlbk-Italic":      "C059-Italic",
    "NewCenturySchlbk-Roman":       "C059-Roman",
    "Palatino-Bold":                "P052-Bold",
    "Palatino-BoldItalic":          "P052-BoldItalic",
    "Palatino-Italic":              "P052-Italic",
    "Palatino-Roman":               "P052-Roman",
    "Symbol":                       "StandardSymbolsPS",
    "Times-Bold":                   "NimbusRoman-Bold",
    "Times-BoldItalic":             "NimbusRoman-BoldItalic",
    "Times-Italic":                 "NimbusRoman-Italic",
    "Times-Roman":                  "NimbusRoman-Regular",
    "ZapfChancery-MediumItalic":    "Z003-MediumItalic",
    "ZapfDingbats":                 "D050000L",
}


# fmt: on
def get_fonts():
    return {
        font: Path(FONT_DATA_DIR, "{0}.ttf".format(fname))
        for font, fname in fonts_mapping.items()
    }


def _get_fonts_block():
    xpdfrc_fonts = [
        "# 35 PostScript Level 2 base fonts".upper(),
    ]
    for font_name, font_file in get_fonts().items():
        xpdfrc_fonts.append("fontFile {0} {1}".format(font_name, font_file.absolute()))
    # extra blank line at end
    xpdfrc_fonts.append("")
    return xpdfrc_fonts
