# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import codecs
import os
import re

from setuptools import find_packages, setup


def get_version(filename):
    with codecs.open(filename, 'r', 'utf-8') as fp:
        contents = fp.read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", contents).group(1)


version = get_version(os.path.join('patchy', '__init__.py'))

with codecs.open('README.rst', 'r', 'utf-8') as readme_file:
    readme = readme_file.read()

with codecs.open('HISTORY.rst', 'r', 'utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')


setup(
    name='patchy',
    version=version,
    description="Patch the inner source of python functions at runtime.",
    long_description=readme + '\n\n' + history,
    author="Adam Johnson",
    author_email='me@adamj.eu',
    url='https://github.com/adamchainz/patchy',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'six>=1.9.0',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    license="BSD",
    zip_safe=False,
    keywords='patchy',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
