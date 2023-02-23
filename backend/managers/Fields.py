# Python Libraries / Librerías Python
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import DECIMAL
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text


# Application Libraries / Librerías de la Aplicación
from utils import Strings


# Preconditions / Precondiciones


class Fields () :

  @staticmethod
  def boolean ( nullable : bool = False, default = False ) -> Column :
    return Column (
      Boolean,
      nullable = nullable,
      default  = default
    )

  @staticmethod
  def date ( nullable : bool = False, default = False ) -> Column :
    if default:
      return Column (
        Date,
        nullable = nullable,
        default  = default
      )
    return Column (
      Date,
      nullable = nullable
    )

  @staticmethod
  def datetime ( nullable : bool = False, default = False ) -> Column :
    if default :
      return Column (
        DateTime ( timezone = True ),
        nullable = nullable,
        default  = default
      )
    return Column (
      DateTime ( timezone = True ),
      nullable = nullable
    )

  @staticmethod
  def decimal ( size : int, decimal_size, nullable : bool = False, default = None ) -> Column :
    return Column (
      DECIMAL ( size, decimal_size ),
      nullable = nullable,
      default  = default
    )

  @staticmethod
  def float ( size : int, decimal_size, nullable : bool = False, default = None ) -> Column :
    return Column (
      Float ( size, decimal_size ),
      nullable = nullable,
      default  = default
    )

  @staticmethod
  def foreignKey ( modelName : str, nullable : bool = False, primaryKey : bool = False ) -> Column :
    tableName = Strings.toPlural ( Strings.snakeCase ( modelName ) )
    return Column (
      Integer,
      ForeignKey (
        '{}.id'.format ( tableName )
      ),
      nullable    = nullable,
      primary_key = primaryKey,
      comment     = '{} ID'.format ( tableName )
    )

  @staticmethod
  def integer ( nullable : bool = False, default = 0 ) -> Column :
    return Column (
      Integer,
      nullable = nullable,
      default  = default
    )

  @staticmethod
  def primaryKey () -> Column :
    return Column (
      Integer,
      primary_key   = True,
      autoincrement = True,
      index         = True
    )

  @staticmethod
  def string ( size : int, nullable : bool = False, unique : bool = False ) -> Column :
    return Column (
      String ( size ),
      nullable = nullable
    )

  @staticmethod
  def text ( nullable : bool = False ) -> Column :
    return Column (
      Text (),
      nullable = nullable
    )
