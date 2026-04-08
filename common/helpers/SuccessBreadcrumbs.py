# Python Libraries / Librerías Python
from flask     import session
from flask     import current_app
from flask     import url_for
from flask     import g
from flask     import request
from flask     import render_template
from flask     import Flask
from functools import wraps
import requests
import json
import inspect

# Application Libraries / Librerías de la Aplicación
from success.core.SuccessContext import SuccessContext

# Preconditions / Precondiciones
BREADCRUMB_REGISTRY = {}


class SuccessBreadcrumbs () :


  @staticmethod
  def _decorator ( label, Action = None, parent = None, params = None ) :
    def decorator ( view_func ) :
      # Obtén nombre del Action para usarlo como clave
      ep = Action or f"{view_func.__module__}.{view_func.__name__}"
      ep = Action or f"{view_func.__module__}.{view_func.__name__}"
      lbl = label or view_func.__name__.replace ( '_', ' ' ).title ()
      prnt = parent or SuccessBreadcrumbs.guessParent ( ep )
      # prnt = parent or SuccessContext.breadcrumb_current

      # parent = parent or getattr ( view_func.view_class, 'breadcrumb_parent', None )
      # label = label or f"{view_func.__name__.title ()} {{id}}"

      crumb =  {
        'label': lbl,
        'Action': ep,
        'params': params or [],
        'parent': prnt
      }

      if ep not in BREADCRUMB_REGISTRY :
          BREADCRUMB_REGISTRY [ ep ] = []

      if crumb not in BREADCRUMB_REGISTRY [ ep ] :
        BREADCRUMB_REGISTRY [ ep ].append ( crumb )

      return view_func

    return decorator


  @staticmethod
  def build () :
    breadcrumb = []
    current_ep = request.endpoint  # p.ej. 'tenants.index'
    while current_ep:
      crumb_list = BREADCRUMB_REGISTRY.get ( current_ep, [] )
      if not crumb_list :
        break
      # Usa el primero por convención (1 crumb por Action)
      crumb = crumb_list [ 0 ]
      label = crumb [ 'label' ]
      url = None
      if crumb [ 'Action' ] :
        try :
          params = {
            key: request.view_args [ key ]
            for key in crumb.get ( 'params', [] )
            if key in request.view_args
          }
          url = url_for ( crumb [ 'Action' ], **params )

        except Exception as e :
          current_app.logger.debug ( f"Breadcrumb URL error: {e}" )

      breadcrumb.append (
        {
          'label': label.format ( **( request.view_args or {} ) ),
          'url': url
        }
      )

      current_ep = crumb.get ( 'parent' )

    # El padre va primero
    breadcrumb.reverse ()
    return breadcrumb


  @staticmethod
  def guessParent ( ep ) :
    # Si módulo termina en .Detail o .Show → reemplaza por .Index
    if ep.endswith ( '.Detail' ) or ep.endswith ( '.Show' ) :
      return re.sub ( r'(Detail|Show)$', 'Index', ep )

    # Si Action tiene .get → quítalo y pon .index por convención
    if '.get' in ep :
      base = ep.split ( '.get' ) [ 0 ]
      return f"{base}.index"

    return None
