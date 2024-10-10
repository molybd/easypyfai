# easypyfai

A pyfai & silx packaging easy to install and launch

## Installation

The purpose of this project is providing an easy-to-install pyFAI installer for users with less programming knowledge, avoid terminal operation and command line. Download installer or portable zip from [release](https://github.com/molybd/easypyfai/releases) is all you need.

If you want to package yourself or package on Linux or MacOS, you can download or git clone the source code, install required python packages, install pyinstaller and package it using

```sh
pyinstaller --hidden-import numpy --hidden-import matplotlib --hidden-import PyQt5 --hidden-import silx --hidden-import fabio --hidden-import pyFAI --hidden-import pyopencl --hidden-import siphash24 --collect-all fabio --collect-all silx --collect-all pyFAI ./src/easypyfai/easypyfai.py
```

## Tips

pyFAI source code has been modified at `io.__init__.DefaultAiWriter.save1D` line 631, add `encoding='utf-8'` :

```python
with open(filename, "w", encoding='utf-8') as f:
```

The original code will raise `UnicodeEncodeError: 'gbk' codec can't encode character '\xb5'` on Windows Simplified Chinese version since system uses gbk.
