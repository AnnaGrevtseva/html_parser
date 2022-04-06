"""Module for weather source interface"""


# pylint: disable=too-few-public-methods
class IWeatherSource:
    """Weather source interface"""

    # pylint: disable=no-self-use
    def get_current_weather(self, _: str) -> str:
        """Method returning the current weather as requests.Response class object.
           Should be overridden for every class inherited from IWeatherSource"""

        return ''
