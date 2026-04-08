# Python Libraries / Librerías Python
import os

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessPathResolver () :

  __baseDir : str = None


  def __init__ ( self, path : str ) -> None :
    self.__baseDir = os.path.dirname ( os.path.abspath ( path ) )


  @staticmethod
  def getPath ( path : str ) -> str :
    return os.path.dirname ( os.path.abspath ( path ) )


  def templatesFolder ( self ) -> str :
    return os.path.join ( self.__baseDir, "templates" )


  def staticFolder ( self ) -> str :
    return os.path.join ( self.__baseDir, "static" )
