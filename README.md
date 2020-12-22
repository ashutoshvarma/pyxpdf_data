[![Python package](https://github.com/ashutoshvarma/pyxpdf_data/workflows/Python%20package/badge.svg)](https://github.com/ashutoshvarma/pyxpdf_data/actions)
[![PyPI](https://img.shields.io/pypi/v/pyxpdf_data)](https://pypi.org/project/pyxpdf-data/)

# pyxpdf_data
This python package consists of encoding files for use with [pyxpdf](https://github.com/ashutoshvarma/pyxpdf).
The encoding files are taken from [poppler_data](https://gitlab.freedesktop.org/poppler/poppler-data) repo .
It is optional and pyxpdf will automatically utilize them if module is install.

## Install
```
pip install pyxpdf_data
```

### Why make seprate module for just encoding files ?
I would love to ship them with pyxpdf but some of these files have different license
than pyxpdf so we have to distribute them seprately.


## License
While pyxpdf is licensed under the GPL, these encoding files have different 
license,  and thus distributed separately.
The cMap data files in the poppler_data folder are under the COPYING.adobe 
license.
The cidToUnicode, nameToUnicode and unicodeMap data files in the the poppler_data 
folder are Copyright Glyph & Cog, LLC and are under the COPYING.gpl2 license.

Fonts in fonts folder are released under the GNU Affero General Public License v3.0.
Verbatim copies of the Ghostscript project's licensing info are included with this
package see fonts/COPYING.affero

The rest of module is licensed under MIT.


## Changelog

### v1.1.0 (04/08/2020)
- remove default settings for pyxpdf (now resides in pyxpdf itself)
- add option to disable rewriting of xpdfrc in `get_xpdfrc()`
- add 35 Postscript base fonts from ghostscript

### v1.0.1 (31/03/2020)
- Fix `xpdfrc` path not readable when installed in system site package

### v1.0 (20/03/2020)
- Initial Version



