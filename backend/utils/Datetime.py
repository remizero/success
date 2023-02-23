# Python Libraries / Librerías Python
from datetime import datetime
import pytz


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones


class Datetime () :

  @staticmethod
  def dateTimeIsoFormatTimeZoneNow () -> str :
    tz      = pytz.timezone ( 'America/Caracas' )
    dateNow = datetime.now ()
    loc_dt  = tz.localize ( dateNow ).replace ( microsecond = 0 )
    return loc_dt.isoformat ()

  @staticmethod
  def dateTimeIsoFormatTimeZoneNowErp () -> str :
    tz                  = pytz.timezone ( 'America/Lima' )
    dateNow             = datetime.now ()
    loc_dt              = tz.localize ( dateNow )
    dateIsoFormat       = loc_dt.isoformat ()
    dateIsoFormatReturn = dateIsoFormat [ 0 : 23 ] + dateIsoFormat [ 26 : ]
    return dateIsoFormatReturn

  @staticmethod
  def getNow ( timezone = 'UTC' ) -> datetime :
    """ Obtiene la hora del sistema según la zona horaria indicada """
    return datetime.now ( pytz.timezone ( timezone ) )

  @staticmethod
  def getDuration ( data_decrypt ) -> int :
    due_date  = datetime.strptime (
      data_decrypt [ 'end_date' ], "%Y-%m-%dT%H:%M:%S.%f%z"
    )
    now_local = datetime.now ( due_date.tzinfo )
    duration  = round ( ( due_date - now_local ).total_seconds () )
    return duration
    