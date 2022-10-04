# Python Libraries / Librerías Python
from importlib import import_module
from pkgutil import iter_modules


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones


class Importer () :

  #adopted from mock.mock._dot_lookup
  @staticmethod
  def _dot_lookup ( obj : object, attribute : str, importModule : str ) :
    '''
      Recursively import packages (if needed) by dotes.
    '''
    try :

      return getattr ( obj, attribute )

    except AttributeError :

      import_module ( importModule )
      Importer._walk_modules ( importModule )
      return getattr ( obj, attribute )

  #adopted from scrapy
  @staticmethod
  def _walk_modules ( importModule ) :
    """
      Loads a module and all its submodules from the given module path and
      returns them. If *any* module throws an exception while importing, that
      exception is thrown back.
    """

    # Support for namespace packages is added. See PEP 420.
    # Namespace packages are a mechanism for splitting a single Python package across multiple directories on disk.
    # When interpreted encounter with non-empty __path__ attribute it adds modules found in those locations
    # to the current package.

    mods = []
    mod = import_module ( importModule )
    mods.append ( mod )
    if hasattr ( mod, '__path__' ) :
      for _, subpath, ispkg in iter_modules ( mod.__path__ ) :
        fullpath = importModule + '.' + subpath
        if ispkg :
          mods += Importer._walk_modules ( fullpath )
        else:
          submod = import_module ( fullpath )
          mods.append ( submod )
    return mods

  #adopted from mock.mock._importer
  @staticmethod
  def importer ( target ) :
    '''
      Convert str to Python construct that target is represented.
      This method will recursively import packages (if needed)
      Following dot notation from left to right. If the component
      exists in packagage (is defined and imported) it will be used,
      otherwrise, it will be imported.
      This method supports PEP 420 (implicit Namespace Packages).
      Note: only compile-time construct is supported.
      Note: no instances will be returned from here, only classes.
      :param target: str to lookup
      :return: function/module/class, etc
    '''

    components = target.split ( '.' )
    importModule = components.pop ( 0 )
    obj = import_module ( importModule )
    Importer._walk_modules ( importModule )

    for attribute in components :
      importModule += f".{ attribute }"
      obj = Importer._dot_lookup ( obj, attribute, importModule )
    return obj