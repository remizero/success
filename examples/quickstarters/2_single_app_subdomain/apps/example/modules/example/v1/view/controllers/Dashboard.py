# Python Libraries / Librerías Python

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Dashboard () :


  def get ( self, data : dict ) -> dict :
    return {
      "status"          : 200,
      "msg"             : "SUCCESSFUL",
      "type"            : "INFO",
      "url"             : "/example/view/simple_view/v1/render/dashboard",
      "path_endpoint"   : "/example/services/view/simple_view/v1/render/dashboard/Action.py",
      "path_controller" : "/example/modules/example/v1/view/controllers/Dashboard.py",
      "app"             : "example",
      "protocol"        : "view",
      "service"         : "simple_view",
      "version"         : "v1",
      "module"          : "render",
      "action"          : "dashboard"
    }
