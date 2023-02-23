# Python Libraries / Librerías Python
import ast
import re

# Application Libraries / Librerías de la Aplicación
from kernel import Debug

# Preconditions / Precondiciones


class Strings () :

  tab       = '  '
  lineBreak = '\n'

  @staticmethod
  def cleanStdout ( string : str ) -> str :
    string = string [ 0:len ( string ) - 1:1 ]
    return string.decode ( "utf-8" )

  @staticmethod
  def sliceindex ( string : str ) -> str :
    i = 0
    for c in string :
      if c.isalpha () :
        i = i + 1
        return i
      i = i + 1

  @staticmethod
  def snakeCase ( string : str ) -> str :
    ''' Convierte un string en Snake Case '''
    case = re.sub ( '(.)([A-Z][a-z]+)', r'\1_\2', string )
    return re.sub ( '([a-z0-9])([A-Z])', r'\1_\2', case ).lower ()

  @staticmethod
  def CamelCase ( string : str ) -> str :
    ''' Convierte un string en Camel Case '''
    # split underscore using split
    temp = string.split ( '_' )
    # joining result
    res = temp [ 0 ] + ''.join ( ele.title () for ele in temp [ 1 : ] )
    return str ( res )

  @staticmethod
  def lowerFirst ( string : str ) -> str :
    i = Strings.sliceindex ( string )
    return string [ : i ].lower () + string [ i : ]

  @staticmethod
  def toPlural ( string : str ) -> str :
    """ Obtiene plural de un string """
    if string [ -1 ] == 'y' :
      return string [ 0:-1 ] + 'ies'
    if string [ -1 ] == 's' :
      return string [ 0:-1 ] + 'ses'
    if string [ -1 ] == 'x' :
      return string [ 0:-1 ] + 'xes'
    if string [ -1 ] == 'h' and string [ -2 ] == 'c' :
      return string [ 0:-1 ] + 'hes'
    return string + 's'

  @staticmethod
  def toSingular ( string : str ) -> str :
    """ Obtiene el singular a partir de un string en plural """
    if string [ len ( string ) - 3 : ] == 'ies' :
      return string [ 0 : -3 ] + 'y'
    if string [ len ( string ) - 3 : ] == 'ses' :
      return string [ 0 : -3 ] + 's'
    if string [ len ( string ) - 3 : ] == 'xes' :
      return string [ 0 : -3 ] + 'x'
    if string [ len ( string ) - 3 : ] == 'hes' :
      return string [ 0 : -3 ] + 'ch'
    if string [ -1 ] == 's' and string [ -2 ] in [ 'e', 'g', 'k', 'l', 'm', 'n', 'p', 'r', 't' ] :
      return string [ 0 : -1 ]
    return string

  @staticmethod
  def toList ( string : str, token : str = '' ) -> list :
    return string.strip ( token )

  @staticmethod
  def upperFirst ( string : str ) -> str :
    i = Strings.sliceindex ( string )
    return string [ : i ].upper () + string [ i : ]
