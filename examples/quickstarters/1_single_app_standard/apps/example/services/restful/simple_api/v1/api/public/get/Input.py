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
from marshmallow.exceptions import ValidationError

# Success Libraries / Librerías Success
from success.engine.io.SuccessInput import SuccessInput

# Application Libraries / Librerías de la Aplicación
from apps.example.services.restful.simple_api.v1.api.public.get.Schema import Schema

# Preconditions / Precondiciones


class Input ( SuccessInput ) :


  def __init__ ( self ) -> None :
    super ().__init__ ()
    self._schema = Schema ()


  def parse ( self ) -> SuccessInput :
    try :
      self._parseInput ()

    except Exception as e :
      self._logger.log ( f"Error al procesar el request data: {e}", "EXCEPTION" )

    return self


  def validate ( self ) -> None :
    try :
      self._validatedData = self._schema.load ( self._rawData )

    except ValidationError as e :
      self._logger.log ( f"Error al procesar el request data: {e}", "EXCEPTION" )
      self._errors.extend ( [ f"{k}: {', '.join ( v )}" for k, v in e.messages.items () ] )

    return self
