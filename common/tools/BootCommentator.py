# Python Libraries / Librerías Python
import random

# Application Libraries / Librerías de la Aplicación
from success.common.tools.MoodEngine import MoodEngine

# Preconditions / Precondiciones


class BootCommentator () :

  @staticmethod
  def show ( appsLoaded : list ) :
    appsCount = len ( appsLoaded )

    if appsCount == 0 :
      BootCommentator._noApps ()

    elif appsCount == 1 and BootCommentator._isEmpty ( appsLoaded [ 0 ] ) :
      BootCommentator._emptyApp ()
    # Si hay más apps o no aplica sarcasmo, se queda en silencio... por ahora 😈

    print ( "\n─────────────────────────────────────────────────────────────" )
    print ( f"[MOOOD 🎭] {MoodEngine.get_today_mood ()}" )
    print ( "─────────────────────────────────────────────────────────────\n" )

  @staticmethod
  def _noApps () :
    message = f"""
[BOOT] Framework ready for battle...

   ░░░░░░░░░░░░░░░░░░░░░░
  ░░  ⚙️   NO APPS FOUND   ░░
   ░░░░░░░░░░░░░░░░░░░░░░

ÑAÑAÑA 😜 I don't have anything loaded... but I'm still running!
Who needs logic when you can just *exist*?

Suggestion: You might want to stop lazing around and create an apps. 🫠
"""
    print ( message )

  @staticmethod
  def _emptyApp () :
    sarcasms = [
      "Was that an apps or just an empty container with illusions of grandeur?",
      "A loaded apps... emptier than the fridge at the end of the month.",
      "Hey, at least you tried... but that doesn't make it work. 😅",
      "That's an apps only because the system is generous with definitions. 😏",
    ]
    message = f"""
[INFO] Loaded 1 apps... technically.

{random.choice ( sarcasms )}

Come on, crack, give that poor thing life!
"""
    print ( message )

  @staticmethod
  def _isEmpty ( apps : dict ) -> bool :
    """
    Define si la apps está vacía. Acá puedes poner tu lógica real.
    Ejemplo: sin endpoints, sin modelos, sin rutas, etc.
    """
    return not apps.get ( "endpoints" ) and not apps.get ( "routes" ) and not apps.get ( "blueprints" )
