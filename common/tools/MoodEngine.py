# Python Libraries / Librerías Python
from datetime import datetime
import random

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class MoodEngine () :
  """
  Mood engine for generating contextual messages based on the day of the week.

  Provides humorous messages that reflect the mood of the framework
  depending on the current day.
  """

  moods = {
    0: [  # Lunes
      "It's Monday... not even the framework wants to raise its head 🥱",
      "Why does it work if it's Monday? I should be sleeping!",
      "The week has just begun and we're already compiling excuses..."
    ],
    1: [  # Martes
      "Tuesday: That existential limbo between not knowing whether to continue or give up 😶",
      "Today is Tuesday... or as we call it in the framework: 'Monday Part 2''."
    ],
    2: [  # Miércoles
      "Wednesday. We're halfway through... another unnecessary refactoring. 🧩",
      "The day of the emotional breakpoint 😵‍💫"
    ],
    3: [  # Jueves
      "Thursday: Official 'just one more thing before deployment' day' 👀",
      "We're not in production, but it feels like we are..."
    ],
    4: [  # Viernes
      "Friday. Everything compiles, no one tests. Long live the faith! 🙏",
      "The framework is already with a beer in hand 🍺"
    ],
    5: [  # Sábado
      "Code on Saturday? You're a tireless soldier. 🫡",
      "You could have been sleeping... but you decided to debug. Maximum respect."
    ],
    6: [  # Domingo
      "Sunday. A day of rest... except for your CPU. 😅",
      "Running a framework on a Sunday? Clearly, this is devotion."
    ],
  }

  @classmethod
  def get_today_mood ( cls ) -> str :
    """
    Get the mood message for the current day of the week.

    Returns:
      str: A mood message corresponding to the current weekday.
    """
    today = datetime.today ().weekday ()
    return random.choice ( cls.moods.get ( today, [ "I have no emotions today... I'm just code." ] ) )
