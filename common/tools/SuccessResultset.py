# Python Libraries / Librerías Python
from flask_sqlalchemy.model import Model
from typing                 import Any

# Success Libraries / Librerías Success
from success.common.SuccessDebug import SuccessDebug

# Preconditions / Precondiciones


class SuccessResultset () :
  """
  Resultset utilities for converting database results to JSON.

  Provides static methods for converting SQLAlchemy models and
  resultsets to JSON format.
  """

  # @staticmethod
  # def dictToJson ( resultSet ) :
  #   myJsonList = []
  #   if resultSet is dict :
  #     for result in resultSet :
  #       myJsonList.append ( result [ 0 ] )
  #   return myJsonList

  @staticmethod
  def toJson ( resultSet : Any ) -> list :
    """
    Convert a resultset to JSON format.

    Args:
      resultSet: SQLAlchemy model or list of models to convert.

    Returns:
      list: List of JSON-serialized models.
    """

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
