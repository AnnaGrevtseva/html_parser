"""Module for get current weather from world-weather.ru"""
import http.client
from http import HTTPStatus

import requests
import tenacity
import typer

from app.iweather_source import IWeatherSource


def print_error_message(error_code):
    """Method print error code for bad response"""

    typer.echo(f'Bad response, error {error_code} ({http.client.responses[error_code]})')


@tenacity.retry(stop=(tenacity.stop_after_delay(30) | tenacity.stop_after_attempt(10)))
def get_world_weather_response(city: str):
    """Method get request on https://world-weather.ru/pogoda/russia/ several times"""

    response = requests.get(f'https://world-weather.ru/pogoda/russia/{city.lower()}')

    if response.status_code != HTTPStatus.OK:
        raise Exception

    return response


# pylint: disable=too-few-public-methods
class WorldWeatherSource(IWeatherSource):
    """World weather source for request from https://world-weather.ru/pogoda/russia/"""

    def get_current_weather(self, city: str) -> str:

        try:
            response = get_world_weather_response(city)
        except tenacity.RetryError:
            typer.echo("Couldn't get response from server")
            return str()

        if response.status_code == HTTPStatus.OK:
            return response.text

        print_error_message(response.status_code)
        return str()
