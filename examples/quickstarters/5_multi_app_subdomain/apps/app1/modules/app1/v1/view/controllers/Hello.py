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
from success.engine.infrastructure.SuccessController import SuccessController

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Hello ( SuccessController ) :


  def load ( self, payload : dict ) -> dict :
    return {
      "status"        : 200,
      "hello_message" : "Hello World desde Success View",
      "api_endpoint"  : "/public/",
      "app"           : "app1"
    }
