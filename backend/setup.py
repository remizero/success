import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read ( filename ) :
  filename = os.path.join ( os.path.dirname ( __file__ ), filename )
  text_type = type ( u"" )
  with io.open ( filename, mode = "r", encoding = 'utf-8' ) as fd:
    return re.sub ( text_type ( r':[a-z]+:`~?(.*?)`' ), text_type ( r'``\1``' ), fd.read () )


setup (
  name = 'success',

  version = '0.1.0',

  url = 'https://github.com/remyzero/pylane',

  license = 'MIT',

  author = 'Filiberto Zaa Avila - remizero',

  description = "Paquete creado para el tutorial 'Creación de paquetes de Python'",

  long_description = read ( 'README.rst' ),

  packages = find_packages ( exclude = ( 'tests', ) ),

  install_requires = [],

  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
  ],
)