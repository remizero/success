# Python Libraries / Librerías Python
from sqlalchemy.orm import (
  relationship,
  backref
)


# Application Libraries / Librerías de la Aplicación
from . import Strings


# Preconditions / Precondiciones


class Relations () :

  modelName : str = ''
  snakeName : str = ''
  pluralName : str = ''

  def __init__ ( self, modelName : str ) :
    self.modelName = modelName
    self.snakeName = Strings.snakeCase ( self.modelName )
    self.pluralName = Strings.toPlural ( self.snakeName )

  def oneToOne ( self, modelNameToRelate : str ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName,
      uselist = False
    )

  def oneToMany ( self, modelNameToRelate : str ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName,
      lazy = 'dynamic'
    )

  def manyToMany ( self, modelNameToRelate: str , secondaryTable : str ) :
    return relationship (
      modelNameToRelate,
      secondary = Strings.toPlural ( Strings.snakeCase ( secondaryTable ) ),
      back_populates = self.pluralName,
      lazy = 'dynamic'
    )

  def hasOne ( self, modelNameToRelate : str ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName
    )

  def hasMany ( self, modelNameToRelate : str ):
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName,
      lazy = 'dynamic'
    )

  def relationalTable ( self, modelNameToRelate : str ) :
    return relationship (
      modelNameToRelate,
      backref = backref ( self.pluralName, cascade = 'all, delete-orphan' )
    )
