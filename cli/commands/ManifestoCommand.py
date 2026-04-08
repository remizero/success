# Python Libraries / Librerías Python

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones
MANIFESTO_TEXT = """
  SUCCESS CLI • FILOSOFÍA
  -----------------------------------

  1. Las herramientas no limitan, liberan.
  2. Lo que hacemos no es solo código, es legado.
  3. El futuro no se copia. Se imagina. Y se escribe.
  4. La mentoría no es egolatría. Es responsabilidad.
  5. Self-hosting no es arquitectura, es autonomía.

  Success es arquitectura. Es visión. Es comunidad.
  No es una solución. Es una forma de pensar.

  -----------------------------------
"""


class ManifestoCommand () :

  @staticmethod
  def show ( args : list = None ) -> None :
    print ( "\n==== SUCCESS CLI: MANIFIESTO ====" )
    print ( MANIFESTO_TEXT )
    print ( "================================\n" )
