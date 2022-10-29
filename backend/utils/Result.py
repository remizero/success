# Python Libraries / Librerías Python
from flask_sqlalchemy.model import Model


# Application Libraries / Librerías de la Aplicación
#from kernel import Model
from kernel import (
  Debug
)


# Preconditions / Precondiciones


class Result () :
  
  # @staticmethod
  # def dictToJson ( resultSet ) :
  #   myJsonList = []
  #   if resultSet is dict :
  #     for result in resultSet :
  #       myJsonList.append ( result [ 0 ] )
  #   return myJsonList

  @staticmethod
  def toJson ( resultSet ) -> list :

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
