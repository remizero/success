# Python Libraries / Librerías Python
from sqlalchemy.orm import relationship


# Application Libraries / Librerías de la Aplicación
from . import (
  EnvVar,
  Strings
)


# Preconditions / Precondiciones


class Relations () :

  modelName = ''
  snakeName = ''
  pluralName = ''
  tableName = ''

  def __init__ ( self, modelName ) :
    self.modelName = modelName
    self.snakeName = Strings.snakeCase ( self.modelName )
    self.pluralName = Strings.toPlural ( self.snakeName )
    if ( EnvVar.isTrue ( 'SQLALCHEMY_TABLENAME_SUCCESS_MODEL' ) ) :
      self.tableName = self.snakeName
    else :
      self.tableName = self.pluralName

  def oneToOne ( self, modelNameToRelate ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.tableName,
      uselist = False
    )

  def oneToMany ( self, modelNameToRelate ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.tableName,
      lazy = 'dynamic'
    )

  def manyToMany ( self, modelNameToRelate, secondaryTable ) :
    return relationship (
      modelNameToRelate,
      secondary = Strings.toPlural ( Strings.snakeCase ( secondaryTable ) ),
      back_populates = self.tableName,
      lazy = 'dynamic'
    )

  def hasOne ( self, modelNameToRelate ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.tableName
    )

  def hasMany ( self, modelNameToRelate ):
    return relationship (
      modelNameToRelate,
      back_populates = self.tableName,
      lazy = 'dynamic'
    )
