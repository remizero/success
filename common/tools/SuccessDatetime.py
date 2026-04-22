# Python Libraries / Librerías Python
from datetime import datetime
import pytz

# Success Libraries / Librerías Success

# Preconditions / Precondiciones


class SuccessDatetime () :
  """
  Datetime utilities for the Success framework.

  Provides static methods for working with dates, times, and timezones.
  """


  @staticmethod
  def dateTimeIsoFormatTimeZoneNow () -> str :
    """
    Get the current datetime in ISO format with timezone (America/Caracas).

    Returns:
      str: Current datetime in ISO format with timezone.
    """
    tz      = pytz.timezone ( 'America/Caracas' )
    dateNow = datetime.now ()
    loc_dt  = tz.localize ( dateNow ).replace ( microsecond = 0 )

    return loc_dt.isoformat ()


  @staticmethod
  def dateTimeIsoFormatTimeZoneNowErp () -> str :
    """
    Get the current datetime in ISO format with timezone (America/Lima) for ERP.

    Returns:
      str: Current datetime in ISO format with timezone, formatted for ERP systems.
    """
    tz                  = pytz.timezone ( 'America/Lima' )
    dateNow             = datetime.now ()
    loc_dt              = tz.localize ( dateNow )
    dateIsoFormat       = loc_dt.isoformat ()
    dateIsoFormatReturn = dateIsoFormat [ 0 : 23 ] + dateIsoFormat [ 26 : ]

    return dateIsoFormatReturn


  @staticmethod
  def getNow ( timezone = 'UTC' ) -> datetime :
    """
    Get the current system time for the specified timezone.

    Args:
      timezone: Timezone name (default: 'UTC').

    Returns:
      datetime: Current datetime in the specified timezone.
    """

    return datetime.now ( pytz.timezone ( timezone ) )


  @staticmethod
  def getDuration ( data_decrypt ) -> int :
    """
    Calculate the duration in seconds until the end date.

    Args:
      data_decrypt: Dictionary containing 'end_date' key with datetime string.

    Returns:
      int: Duration in seconds until the end date.
    """
    due_date  = datetime.strptime (
      data_decrypt [ 'end_date' ], "%Y-%m-%dT%H:%M:%S.%f%z"
    )
    now_local = datetime.now ( due_date.tzinfo )
    duration  = round ( ( due_date - now_local ).total_seconds () )

    return duration
    