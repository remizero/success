# Python Libraries / Librerías Python
from abc   import ABC, abstractmethod
from flask import Flask

# Application Libraries / Librerías de la Aplicación
from success.common.patterns.creational.singleton.SingletonMetaclass import SingletonMetaclass

# Preconditions / Precondiciones


class Singleton ( ABC, metaclass = SingletonMetaclass ) :

  _initialized : bool = False


  @abstractmethod
  def customInit ( self, apps : Flask = None, *args, **kwargs ) :
    raise NotImplementedError ( "customInit() must be implemented by subclass." )
