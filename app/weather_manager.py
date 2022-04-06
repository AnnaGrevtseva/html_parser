"""Module for get temperature from weather sources """
from bs4 import BeautifulSoup

from app.iweather_source import IWeatherSource


def get_temperature_from_html(page: str):
    """Method getting temperature from html page"""

    soup = BeautifulSoup(page, 'html.parser')
    return soup.find(id='weather-now-number').get_text()


# pylint: disable=too-few-public-methods
class WeatherManager:
    """Weather manager for work with weather source"""

    def __init__(self, weather_source: IWeatherSource):
        self.__weather_source = weather_source

    def get_temperature(self, city: str):
        """Method returning temperature if status code = ok or returning """

        weather_html_str = self.__weather_source.get_current_weather(city)
        if weather_html_str:
            return get_temperature_from_html(weather_html_str)

        return None
