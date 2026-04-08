# Python Libraries / Librerías Python
from sqlalchemy.ext.declarative import declared_attr

# Success Libraries / Librerías Success
from success.core.SuccessContext            import SuccessContext
from success.engine.models.SuccessFields    import SuccessFields
from success.engine.models.SuccessRelations import SuccessRelations
from success.common.tools.SuccessDatetime   import SuccessDatetime

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones
database = SuccessContext ().getExtension ( "SuccessDatabaseExtension" )
if database is None :
  raise RuntimeError ( "La extensión Sqlalchemy no está cargada" )


# TODO como realizar busquedas parametrizadas
class SuccessBaseModel ( database._extension.Model ) :

  __abstract__ = True
  id           = SuccessFields.primaryKey ()


  @declared_attr
  def __tablename__ ( cls ) :
    relatorAux = SuccessRelations ( cls.__name__ )
    return relatorAux.pluralName


  def __init__ ( self, **kwargs ) :
    self.inputData ( **kwargs )


  def inputData ( self, **kwargs ) :
    for kwarg in kwargs :
      setattr ( self, kwarg, kwargs [ kwarg ] )


  def insert ( self ) :
    self.created_at = SuccessDatetime.getNow ()
    self.__save ()


  def update ( self ) :
    self.updated_at = SuccessDatetime.getNow ()
    self.__save ()


  def delete ( self ) :
    self.updated_at = SuccessDatetime.getNow ()
    self.deleted    = False
    self.__save ()


  def findAll ( self ) :
    return self.query.all ()


  def findById ( self ) :
    return self.query.get ( self.id )


  def findByName ( self ) :
    return self.query.filter_by ( name = self.name ).first ()


  def findByFilters ( self, many : bool = True, **kwargs ) :
    retorno = self.__validateFilters ( **kwargs )
    if retorno == True :
      kwargs [ 'deleted' ] = False
      if ( many ) :
        return self.query.filter_by ( **kwargs ).all ()

      else :
        return self.query.filter_by ( **kwargs ).first ()

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
    fe_dict = self.__dict__.copy ()
    del fe_dict [ '_sa_instance_state' ]

    return fe_dict


  def as_dict ( self ) :
    return { c.name: getattr ( self, c.name ) for c in self.__table__.columns }


  def __validateFilters ( self, **kwargs ) :
    # Obtener los atributos de la clase,
    # Verificar que los indices de **kwargs correspondan con los atributos de la clase
    # Si al menos uno de los indices de **kwargs no corresponde emitir un error y detener la ejecucion del metodo
    return True


  @classmethod
  def get_by_id ( cls, id ) :
    return cls.query.get ( id )


  @classmethod
  def list_all ( cls ) :
    return cls.query.filter_by ( deleted = False ).all ()


  @classmethod
  def query ( cls, filters : dict, many : bool = True ) :
    filters [ "deleted" ] = False
    q = cls.query.filter_by ( **filters )
    return q.all () if many else q.first ()


  @classmethod
  def create_from_payload ( cls, payload : dict ) :
    instance = cls ( **payload )
    instance.insert ()
    return instance
