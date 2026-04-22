# Copyright [2026] [Filiberto Zaá Avila "remizero"]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Python Libraries / Librerías Python
from flask import Response as FlaskResponse

# Success Libraries / Librerías Success
from success.engine.io.SuccessRestfulAction import SuccessRestfulAction

# Application Libraries / Librerías de la Aplicación
from apps.app1.services.restful.simple_api.v1.api.public.get.Input    import Input
from apps.app1.services.restful.simple_api.v1.api.public.get.Output   import Output
from apps.app1.services.restful.simple_api.v1.api.public.get.Response import Response
from apps.app1.modules.app1.v1.view.controllers.PublicApi            import PublicApi

# Preconditions / Precondiciones


class Action ( SuccessRestfulAction ) :


  def __init__ ( self ) -> None :
    super ().__init__ ( Input (), Output (), Response (), PublicApi () )
    self._controllerMethod = "fetch"


  def get ( self ) -> FlaskResponse :
    return self.execute ( self._controllerMethod )
