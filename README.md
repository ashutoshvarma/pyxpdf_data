# pyxpdf_data
This python package consists of encoding files for use with pyxpdf.
The encoding files are taken from [poppler_data](https://gitlab.freedesktop.org/poppler/poppler-data) repo .
It is optional and pyxpdf will automatically utilize them if module is install.

## Install
```
pip install pyxpdf_data
```

## License
While pyxpdf is licensed under the GPL, these encoding files have different 
license,  and thus distributed separately.
The cMap data files in the poppler_data folder are under the COPYING.adobe 
license.
The cidToUnicode, nameToUnicode and unicodeMap data files in the the poppler_data 
folder are Copyright Glyph & Cog, LLC and are under the COPYING.gpl2 license.

The rest of module is licensed under MIT.

