# Python Libraries / Librerías Python
from abc import (
  ABC,
  abstractmethod
)


# Application Libraries / Librerías de la Aplicación
from exceptions import OutputException
from kernel import (
  Logger,
  Debug
)
from . import Schema
from utils import (
  EnvVar,
  Http,
  Structs
)


# Preconditions / Precondiciones


class Output ( ABC ) :

  __hasError      : bool   = None
  __isLogin       : bool   = None
  __logger        : Logger = None
  __output        : dict   = None
  __schemaOutput           = None
  __successOutput : bool   = None

  @abstractmethod
  def __init__ ( self, isLogin : bool = False ) -> None :
    self.__logger = Logger ( __name__ )
    self.__isLogin = isLogin
    self.__successOutput = EnvVar.isTrue ( 'SUCCESS_OUTPUT_MODEL' )
    if ( self.__successOutput ) :

      self.__schemaOutput = Structs.successOutputEmptySchema ()

    else :

      self.__schemaOutput = Schema ()

  @abstractmethod
  def data ( self, data : dict ) -> dict :
    pass

  def output ( self ) -> dict :
    if ( self.__successOutput ) :

      if ( Http.isMethod ( 'POST' ) ) :
        self.setData ( self.__output )
      return self.__schemaOutput

    elif ( self.__isLogin or self.__hasError ) :

      return self.__output

    else :

      return self.__schemaOutput.dump ( self.__output )

  def setAction ( self, action : str ) -> None :
    if ( self.__successOutput ) :

      self.__schemaOutput [ 'action' ] = action

    else :
      raise OutputException ()

  def setData ( self, data : list ) -> None :
    if ( self.__successOutput ) :

      self.__schemaOutput [ 'data' ].append ( data.copy () )

    else :
      raise OutputException ()

  def setOptions ( self, attribute : str, options : list ) -> None :
    if ( self.__successOutput ) :

      for model in self.__schemaOutput [ 'model' ] :

        if model [ 'name' ] == attribute :

          model [ 'options' ] = options
          break

    else :
      raise OutputException ()

  def error ( self, _msg : str, _type : str, _status : int ) -> None :
    self.__hasError = True
    self.__output = {
      'error' : _msg,
      'type' : _type, # warning, fatal, error, normal
      'status' : _status #200, 401, ...
    }

  def exception ( self, _msg : str, _type : str, _status : int ) -> None :
    self.error ( _msg, _type, _status )
