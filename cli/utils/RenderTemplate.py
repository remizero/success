# Python Libraries / Librerías Python
from jinja2 import Environment
from jinja2 import FileSystemLoader

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class RenderTemplate () :


  @staticmethod
  def toString ( template_dir, template_file, context ) :
    env = Environment ( loader = FileSystemLoader ( template_dir ) )
    template = env.get_template ( template_file )
    return template.render ( context )


  @staticmethod
  def toFile ( template_dir, template_file, target_path, context ) :
    rendered = RenderTemplate.toString ( template_dir, template_file, context )
    with open ( target_path, "w" ) as f :
      f.write ( rendered )


  from pathlib import Path
  def ensure_init_py(path: Path):
    """Crea __init__.py recursivamente hasta la raíz del paquete"""
    for parent in reversed(path.parents):
      init_path = parent / "__init__.py"
      if not init_path.exists():
        init_path.touch()