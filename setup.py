import os, sys

# Figure out the version number and write it to
#     src/qinfer/version.py
# so that we don't have to import qinfer before it's
# installed. This technique seems to be popular amongst
# scientific libraries for ensuring that PEP-440 is adhered
# to, and that version numbers in __init__.py match those in
# setup.py.

MAJOR = 1
MINOR = 0
PRE = 'b3'
VERSION = "{major}.{minor}{pre}".format(
    major=MAJOR, minor=MINOR, pre=PRE if PRE is not None else ''
)
VERSION_TARGET = 'src/qinfer/version.py'

def write_version(filename=VERSION_TARGET):
    contents = """\
# This file is automatically generated by setup.py.
# Do not modify.
version = "{version}"
""".format(version=VERSION)
    
    with open(filename, 'w') as version_file:
        version_file.write(contents)

if os.path.exists(VERSION_TARGET):
    os.remove(VERSION_TARGET)

write_version()

from distutils.core import setup

try:
    with open('README.rst', 'r') as readme:
        long_description = readme.read()
except:
    long_description = ''

setup(
    name='QInfer',
    version=VERSION,
    url='https://github.com/QInfer/python-qinfer',
    download_url='https://github.com/QInfer/python-qinfer/archive/v1.0b1.tar.gz',
    author='Chris Granade and Chris Ferrie',
    author_email='cgranade@cgranade.com',
    maintainer='Chris Granade and Chris Ferrie',
    maintainer_email='cgranade@cgranade.com',
    package_dir={'': 'src'},
    packages=[
        'qinfer',
        'qinfer._lib',
        'qinfer.tomography'
    ],
    keywords=['quantum', 'Bayesian', 'estimation'],
    description=
        'Bayesian particle filtering for parameter estimation in quantum '
        'information applications.',
    long_description=long_description,
    license='http://www.gnu.org/licenses/agpl-3.0.en.html',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    platforms=['any'],
    install_requires=[
        'numpy',
        'scipy',
        'future>=0.15'
    ]
)
