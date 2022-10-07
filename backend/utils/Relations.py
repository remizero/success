# Python Libraries / Librerías Python
from sqlalchemy.orm import relationship


# Application Libraries / Librerías de la Aplicación
from . import Strings


# Preconditions / Precondiciones


class Relations () :

  modelName = ""
  snakeName = ""
  pluralName = ""

  def __init__ ( self, modelName ) :
    self.modelName = modelName
    self.snakeName = Strings.snakeCase ( self.modelName )
    self.pluralName = Strings.toPlural ( self.snakeName )

  def oneToOne ( self, modelNameToRelate ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName,
      uselist = False
    )

  def oneToMany ( self, modelNameToRelate ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName,
      lazy = 'dynamic'
    )

  def manyToMany ( self, modelNameToRelate, secondaryTable ) :
    return relationship (
      modelNameToRelate,
      secondary = Strings.toPlural ( Strings.snakeCase ( secondaryTable ) ),
      back_populates = self.pluralName,
      lazy = 'dynamic'
    )

  def hasOne ( self, modelNameToRelate ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName
    )

  def hasMany ( self, modelNameToRelate ):
    return relationship (
      modelNameToRelate,
      back_populates = self.snakeName,
      lazy = 'dynamic'
    )
