from __future__ import (absolute_import,
                        division,
                        print_function,
                        unicode_literals)

import os
from codecs import open

from setuptools import find_packages, setup
import versioneer

here = os.path.abspath(os.path.dirname(__file__))

# Dependencies.
with open('requirements.txt') as f:
    requirements = f.readlines()
install_requires = [t.strip() for t in requirements]

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ogh',
    version=versioneer.get_version(),
    description='Tools for observing the terrestrial and aquatic surfaces of Earth',
    long_description=long_description,
    url='',
    author='Jimmy Phuong',
    author_email='jphuong@uw.edu',
    maintainer='Landung Setiawan',
    maintainer_email='landungs@uw.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering'
    ],
    keywords='Freshwater Intiative Tools',
    packages=find_packages(),
    install_requires=install_requires,
)