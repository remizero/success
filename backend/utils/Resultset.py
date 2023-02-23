# Python Libraries / Librerías Python
from flask_sqlalchemy.model import Model
from typing                 import Any


# Application Libraries / Librerías de la Aplicación
from kernel import Debug


# Preconditions / Precondiciones


class Resultset () :
  
  # @staticmethod
  # def dictToJson ( resultSet ) :
  #   myJsonList = []
  #   if resultSet is dict :
  #     for result in resultSet :
  #       myJsonList.append ( result [ 0 ] )
  #   return myJsonList

  @staticmethod
  def toJson ( resultSet : Any ) -> list :

    myJsonList = list ()
    if isinstance ( resultSet, list ) :

      for result in resultSet :

        if issubclass ( result, Model ) :

          myJsonList.append ( result.toJson () )

    elif isinstance ( resultSet, Model ) :

      myJsonList.append ( resultSet.toJson () )

    else :

      # TODO COMO PROCESAR ESTE TIPO DE DATO
      myJsonList.append ( resultSet.toJson () )

    return myJsonList
  
  # @staticmethod
  # def toJson ( resultSet ) :
  #   return resultSet.fetchone () [ 0 ]
