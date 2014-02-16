#!/usr/bin/env python

import os
import sys

from setuptools import setup

if sys.platform == 'win32':
    sys.exit('error: this module is not meant to work on Windows')

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.rst')).read()

VERSION = '6.2.4.1'
DESCRIPTION = 'Legacy wrapper around the gnureadline package'
LONG_DESCRIPTION = README + '\n\n' + NEWS
CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name="readline",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    install_requires=['gnureadline'],
    maintainer="Ludwig Schwardt; Sridhar Ratnakumar",
    maintainer_email="ludwig.schwardt@gmail.com; github@srid.name",
    url="http://github.com/ludwigschwardt/python-readline",
    license="GNU GPL",
    platforms=['MacOS X', 'Posix'],
    py_modules=['readline'],
    zip_safe=False,
)
