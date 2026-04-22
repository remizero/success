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

# Success Libraries / Librerías Success
from success.engine.infrastructure.SuccessHook import SuccessHook

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class JwtHook ( SuccessHook ) :


  def __init__ ( self ) :
    super ().__init__ ()


  def execute ( self, context : dict ) -> None :
    print ( f"{self.__class__} ha recibido el context {context}" )
