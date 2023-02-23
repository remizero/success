# Python Libraries / Librerías Python
from textwrap import TextWrapper
import os


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones


class Debug () :

  file     : TextWrapper = None
  fileName : str         = './log/debug.txt'

  #  path : str, name : str, ext : str = ''
  def __init__ ( self ) -> None :
    self.fileName = './log/debug.txt'

  def close ( self ) -> None :
    self.file.close ()

  def create ( self ) -> None :
    self.file = open ( file = self.fileName, mode = 'w', encoding = 'utf-8' )
    self.close ()

  def open ( self, mode = 'a' ) -> None :
    self.file = open ( self.fileName, mode )

  def write ( self, line ) -> None :
    self.file.write ( str ( line ) + os.linesep )

  @staticmethod
  def log ( data ) -> None :
    with open ( "./log/debug.txt", "a" ) as external_file :
      print ( "DEBUG <==> %s"%data, file = external_file )
      external_file.close ()
