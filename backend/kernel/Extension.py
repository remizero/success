# Python Libraries / Librerías Python
from abc import ABC, abstractmethod
from flask import Flask


# Application Libraries / Librerías de la Aplicación
from kernel import Logger


# Preconditions / Precondiciones


class Extension ( ABC ) :

  extension = None
  logger : Logger = None

  def __init__ ( self ) -> None :
    self.logger = Logger ( __name__ )

  @abstractmethod
  def config ( self ) -> None :
    raise NotImplementedError ()

  @abstractmethod
  def register ( self, _app : Flask ) -> None :
    self.config ()
    self.userConfig ()

  @abstractmethod
  def userConfig ( self, **kwargs ) -> None :
    raise NotImplementedError ()
