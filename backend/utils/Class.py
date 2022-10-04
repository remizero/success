# Python Libraries / Librerías Python
from pprint import pprint
from typing import Any


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones


class Class () :

  @staticmethod
  def instanceFromString ( className : str, params : set ) -> dict [ str, Any ] :
    # https://programmerclick.com/article/23561860026/
    # https://cosasdedevs.com/posts/crear-una-instancia-de-una-clase-mediante-un-string-con-python/
    pprint ( globals () )
    return globals () [ className ] ( params )

  @staticmethod
  def hasMethod ( instance : object, methodName : str ) -> bool :
    return hasattr ( instance, methodName )
