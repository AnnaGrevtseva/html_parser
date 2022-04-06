import pytest
import requests
import requests_mock
from app.iweather_source import IWeatherSource


class WeatherSourceGood(IWeatherSource):

    def get_current_weather(self, city: str):
        with requests_mock.Mocker() as m:
            m.get('http://test.com', text='''"""<div id='weather-now-number'>-5<span>°</span></div>"""''')
            response = requests.get(f'http://test.com')
            return response.text


class WeatherSourceBad(IWeatherSource):

    def get_current_weather(self, city: str):
        with requests_mock.Mocker() as m:
            m.get('http://test.com', text='')
            response = requests.get(f'http://test.com')
            return response.text


@pytest.fixture()
def weather_source_good():
    return WeatherSourceGood()


@pytest.fixture()
def weather_source_bad():
    return WeatherSourceBad()
