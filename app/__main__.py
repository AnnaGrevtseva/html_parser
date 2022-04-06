"""Application entry point"""

import typer

import app.weather_manager as wm
import app.world_weather_source as ws


def main(city: str = typer.Option(..., help='Name of the city')):
    """Show current weather"""

    weather_source = ws.WorldWeatherSource()
    weather_manager = wm.WeatherManager(weather_source)
    temperature = weather_manager.get_temperature(city)

    if temperature is not None:
        typer.echo(f'Current weather in {city.capitalize()}: {temperature}')


typer.run(main)
