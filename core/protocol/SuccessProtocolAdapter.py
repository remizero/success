# Python Libraries / Librerías Python
from abc   import abstractmethod
from flask import Blueprint

# Success Libraries / Librerías Success
from success.common.base.SuccessClass import SuccessClass
from success.core.SuccessBuildContext import SuccessBuildContext

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessProtocolAdapter ( SuccessClass ) :
    """
    Base adapter for endpoint protocols.

    Defines the common interface for all protocol adapters
    (view, restful, default). Each adapter is responsible for registering
    endpoints in a Flask blueprint according to its specific protocol.

    Usage:
        class CustomProtocolAdapter(SuccessProtocolAdapter):
            def register(self, buildContext, blueprint, options):
                # Custom implementation
                pass
    """


    def __init__ ( self ) -> None :
        """
        Initialize the protocol adapter.

        Note:
            Adapters are stateless and can be reused.
        """
        super ().__init__ ()


    @abstractmethod
    def register ( self, buildContext : SuccessBuildContext, blueprint : Blueprint, options : dict ) -> None :
        """
        Register an endpoint in the blueprint according to the specific protocol.

        Args:
            buildContext: Build context with application configuration.
            blueprint: Flask blueprint where the endpoint will be registered.
            options: Dictionary with specific endpoint configuration.

        Raises:
            NotImplementedError: Must be implemented by subclasses.
        """
        raise NotImplementedError ()
