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
from . import (
  EnvVar,
  Strings
)


# Preconditions / Precondiciones


class Fields () :

  @staticmethod
  def db_primary_key () -> Column :
    return Column (
      Integer,
      primary_key = True,
      autoincrement = True,
      index = True
    )

  @staticmethod
  def db_integer ( nullable : bool = False, default = 0 ) -> Column :
    return Column (
      Integer,
      nullable = nullable,
      default = default
    )

  @staticmethod
  def db_string ( size : int, nullable : bool = False, unique : bool = False ) -> Column :
    return Column (
      String ( size ),
      nullable = nullable
    )

  @staticmethod
  def db_text ( nullable : bool = False ) -> Column :
    return Column (
      Text (),
      nullable = nullable
    )

  @staticmethod
  def db_foreign_key ( modelName : str, nullable : bool = False ) -> Column :
    tableName = ''
    if ( EnvVar.isTrue ( 'SQLALCHEMY_TABLENAME_SUCCESS_MODEL' ) ) :
      tableName = Strings.snakeCase ( modelName )
    else :
      tableName = Strings.toPlural ( Strings.snakeCase ( modelName ) )
    return Column (
      Integer,
      ForeignKey (
        '{}.id'.format ( tableName )
      ),
      nullable = nullable,
      comment = '{} ID'.format ( tableName )
    )

  @staticmethod
  def db_datetime ( nullable : bool = False, default = False ) -> Column :
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
  def db_date ( nullable : bool = False, default = False ) -> Column :
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
  def db_boolean ( nullable : bool = False, default = False ) -> Column :
    return Column (
      Boolean,
      nullable = nullable,
      default = default
    )

  @staticmethod
  def db_decimal ( size : int, decimal_size, nullable : bool = False, default = None ) -> Column :
    return Column (
      DECIMAL ( size, decimal_size ),
      nullable = nullable,
      default = default
    )

  @staticmethod
  def db_float ( size : int, decimal_size, nullable : bool = False, default = None ) -> Column :
    return Column (
      Float ( size, decimal_size ),
      nullable = nullable,
      default = default
    )
