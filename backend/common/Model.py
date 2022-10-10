# Python Libraries / Librerías Python
from sqlalchemy.ext.declarative import declared_attr


# Application Libraries / Librerías de la Aplicación
from extensions import database
from utils import (
  Datetime,
  Fields,
  Relations,
  Strings
)


# Preconditions / Precondiciones


class Model ( database.extension.Model ) :

  __abstract__ = True
  id = Fields.db_primary_key ()
  enabled = Fields.db_boolean ()
  created_at = Fields.db_datetime ( default = Datetime.getNow () )
  updated_at = Fields.db_datetime ( nullable = True, default = None )
  deleted = Fields.db_boolean ()

  @declared_attr
  def __tablename__ ( cls ) :
    relatorAux = Relations ( cls.__name__ )
    return relatorAux.tableName

  def __init__ ( self, **kwargs ) :
    self.inputData ( **kwargs )

  def inputData ( self, **kwargs ) :
    for kwarg in kwargs :
      setattr ( self, kwarg, kwargs [ kwarg ] )

  def insert ( self ) :
    self.created_at = Datetime.getNow ()
    self.__save ()

  def update ( self ) :
    self.updated_at = Datetime.getNow ()
    self.__save ()

  def delete ( self ) :
    self.updated_at = Datetime.getNow ()
    self.deleted = False
    self.__save ()

  def findAll ( self ) :
    return self.query.all ()

  def findById ( self ) :
    return self.query.get ( self.id )

  def findByName ( self ) :
    return self.query.filter_by ( name = self.name ).first ()

  def findByFilters ( self, **kwargs ) :
    retorno = self.__validateFilters ( **kwargs )
    if retorno == True :
      kwargs [ 'deleted' ] = False
      return self.query.filter_by ( **kwargs ).all ()
    return retorno

  def scalar ( self, **kwargs ) :
    retorno = self.__validateFilters ( **kwargs )
    if retorno == True :
      kwargs [ 'deleted' ] = False
      return self.query.filter_by ( **kwargs ).scalar ()
    return retorno

  def rollback ( self ) :
    database.extension.session.rollback ()

  def __save ( self ) :
    database.extension.session.add ( self )
    database.extension.session.commit ()

  def toJson ( self ) :
    fe_dict = self.__dict__
    del fe_dict [ '_sa_instance_state' ]
    return fe_dict

  def as_dict ( self ) :
    return { c.name: getattr ( self, c.name ) for c in self.__table__.columns }

  def __validateFilters ( self, **kwargs ) :
    # Obtener los atributos de la clase,
    # Verificar que los indices de **kwargs correspondan con los atributos de la clase
    # Si al menos uno de los indices de **kwargs no corresponde emitir un error y detener la ejecucion del metodo
    return True
