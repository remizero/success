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
from success.engine.io.SuccessViewAction import SuccessViewAction
from success.engine.io.SuccessOutput     import SuccessOutput

# Application Libraries / Librerías de la Aplicación
from apps.example.services.view.simple_view.v1.render.hello.Input    import Input
from apps.example.services.view.simple_view.v1.render.hello.Response import Response as ActionResponse
from apps.example.modules.example.v1.view.controllers.Hello          import Hello

# Preconditions / Precondiciones


class Action ( SuccessViewAction ) :


  def __init__ ( self ) -> None :
    super ().__init__ ( Input (), SuccessOutput (), ActionResponse (), Hello () )
    self._controllerMethod    = "load"
    self._outputSpec.template = "hello.html"


  def get ( self ) -> FlaskResponse :
    return self.execute ( self._controllerMethod )
