# Python Libraries / Librerías Python
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

# Application Libraries / Librerías de la Aplicación
from success.common.tools.SuccessStrings import SuccessStrings

# Preconditions / Precondiciones


class SuccessRelations () :

  modelName  : str = ''
  snakeName  : str = ''
  pluralName : str = ''


  def __init__ ( self, modelName : str ) :
    self.modelName  = modelName
    self.snakeName  = SuccessStrings.snakeCase ( self.modelName )
    self.pluralName = SuccessStrings.toPlural ( self.snakeName )


  def hasOne ( self, modelNameToRelate : str ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName
    )


  def hasMany ( self, modelNameToRelate : str ):
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName,
      lazy           = 'dynamic'
    )


  def manyToMany ( self, modelNameToRelate: str, secondaryTable : str ) :
    return relationship (
      modelNameToRelate,
      secondary      = SuccessStrings.toPlural ( SuccessStrings.snakeCase ( secondaryTable ) ),
      back_populates = self.pluralName,
      lazy           = 'dynamic'
    )


  def manyToManyAssociation ( self, modelNameToRelate: str, backPopulates : str ) :
    return relationship (
      modelNameToRelate,
      back_populates = backPopulates
    )


  def manyToManySimple ( self, modelNameToRelate: str, secondaryTable : str ) :
    return relationship (
      modelNameToRelate,
      secondary      = SuccessStrings.toPlural ( SuccessStrings.snakeCase ( secondaryTable ) ),
      back_populates = self.pluralName,
      lazy           = 'dynamic'
    )


  def oneToOne ( self, modelNameToRelate : str ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName,
      uselist        = False
    )


  def oneToMany ( self, modelNameToRelate : str ) :
    return relationship (
      modelNameToRelate,
      back_populates = self.pluralName,
      lazy           = 'dynamic'
    )


  def relationalTable ( self, modelNameToRelate : str ) :
    return relationship (
      modelNameToRelate,
      backref = backref ( self.pluralName, cascade = 'all, delete-orphan' )
    )


  def relationalTable_2 ( self, modelNameToRelate : str, backPopulates : str ) :
    return relationship (
      modelNameToRelate,
      back_populates = backPopulates
    )
