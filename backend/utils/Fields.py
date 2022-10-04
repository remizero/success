# Python Libraries / Librerías Python
from sqlalchemy import (
  Boolean,
  Column,
  Date,
  DateTime,
  DECIMAL,
  Float,
  ForeignKey,
  Integer,
  String,
  Text
)


# Application Libraries / Librerías de la Aplicación
from utils import Strings


# Preconditions / Precondiciones


class Fields () :

  @staticmethod
  def db_primary_key () :
    return Column (
      Integer,
      primary_key = True,
      autoincrement = True,
      index = True
    )

  @staticmethod
  def db_integer ( nullable = False, default = 0 ) :
    return Column (
      Integer,
      nullable = nullable,
      default = default
    )

  @staticmethod
  def db_string ( size, nullable = False ) :
    return Column (
      String ( size ),
      nullable = nullable
    )

  @staticmethod
  def db_text ( nullable = False ) :
    return Column (
      Text (),
      nullable = nullable
    )

  @staticmethod
  def db_foreign_key ( model_name, nullable = False ) :
    table_name = Strings.toPlural ( Strings.snakeCase ( model_name ) )
    return Column (
      Integer,
      ForeignKey (
        '{}.id'.format ( table_name )
      ),
      nullable = nullable,
      comment = '{} ID'.format ( table_name )
    )

  @staticmethod
  def db_datetime ( nullable = False, default = False ) :
    if default :
      return Column (
        DateTime ( timezone = True ),
        nullable = nullable,
        default = default
      )
    return Column (
      DateTime ( timezone = True ),
      nullable = nullable
    )

  @staticmethod
  def db_date ( nullable = False, default = False ) :
    if default:
      return Column (
        Date,
        nullable = nullable,
        default = default
      )
    return Column (
      Date,
      nullable = nullable
    )

  @staticmethod
  def db_boolean ( nullable = False, default = False ) :
    return Column (
      Boolean,
      nullable = nullable,
      default = default
    )

  @staticmethod
  def db_decimal ( size, decimal_size, nullable = False, default = None ) :
    return Column (
      DECIMAL ( size, decimal_size ),
      nullable = nullable,
      default = default
    )

  @staticmethod
  def db_float ( size, decimal_size, nullable = False, default = None ) :
    return Column (
      Float ( size, decimal_size ),
      nullable = nullable,
      default = default
    )
