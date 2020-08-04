from setuptools import setup

# remember to bump the version in __init__.py also.
VERSION = "1.1.0"

with open("README.md", "r", encoding="utf-8") as fp:
    readme = fp.read()

setup(
    name="pyxpdf_data",
    version=VERSION,
    packages=["pyxpdf_data"],
    description=(
        "This package contains additional encoding files for pyxpdf. "
        "(credit poppler_data)"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Ashutosh Varma",
    author_email="ashutoshvarma11@live.com",
    url="https://github.com/ashutoshvarma/pyxpdf_data",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Text Processing",
    ],
    include_package_data=True,
)
