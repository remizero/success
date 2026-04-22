# Python Libraries / Librerías Python
from flask             import Flask
from flask_apscheduler import APScheduler

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension

# Preconditions / Precondiciones


class SuccessAPSchedulerExtension ( SuccessExtension ) :
  """
  APScheduler extension for the Success framework.

  Integrates Flask-APScheduler for scheduled task management
  and background job processing.
  """


  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the APScheduler extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = APScheduler ()
