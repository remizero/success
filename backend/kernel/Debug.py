# Python Libraries / Librerías Python
import os


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones


class Debug () :

  file = None
  fileName = './log/debug.txt'

  #  path : str, name : str, ext : str = ''
  def __init__ ( self ) -> None :
    self.fileName = './log/debug.txt'

  def close ( self ) :
    self.file.close ()

  def create ( self ) :
    self.file = open ( file = self.fileName, mode = 'w', encoding = 'utf-8' )
    self.close ()

  def open ( self, mode = 'a' ) :
    self.file = open ( self.fileName, mode )

  def write ( self, line ) :
    self.file.write ( str ( line ) + os.linesep )

  @staticmethod
  def log ( data ) :
    with open ( "./log/debug.txt", "a" ) as external_file :
      print ( "DATA <==> %s"%data, file = external_file )
      external_file.close ()
